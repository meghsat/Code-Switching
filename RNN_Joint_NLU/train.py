import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.optim as optim
import torch.nn.functional as F
import os
import pickle
import random
import argparse
import numpy as np
from data import *
from model import Encoder, Decoder
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
import json

USE_CUDA = torch.cuda.is_available()

def prepare_sequence_test(seq, to_ix, is_tag=False):
    """
    Modified prepare_sequence for test data that handles unknown tokens properly
    """
    if is_tag:
        # For tags, use PAD for unknown tags instead of UNK
        idxs = list(map(lambda w: to_ix[w] if w in to_ix.keys() else to_ix["<PAD>"], seq))
    else:
        # For words, use UNK for unknown words
        idxs = list(map(lambda w: to_ix[w] if w in to_ix.keys() else to_ix["<UNK>"], seq))
    
    tensor = Variable(torch.LongTensor(idxs)).cuda() if USE_CUDA else Variable(torch.LongTensor(idxs))
    return tensor

def preprocessing_test(file_path, length, word2index, tag2index, intent2index):
    """
    Process test data using existing vocabularies
    """
    try:
        test_data = open(file_path, "r").readlines()
        print(f"Successfully loaded test data. # of examples: {len(test_data)}")
    except:
        print("No test file found!")
        return None
    
    test_data = [t[:-1] for t in test_data]
    test_data = [[t.split("\t")[0].split(" "), t.split("\t")[1].split(" ")[:-1], t.split("\t")[1].split(" ")[-1]] for t in test_data]
    #print("test_data 1", test_data)
    test_data = [[t[0][1:-1], t[1][1:], t[2]] for t in test_data]
    #print("test_data 2",test_data)
    seq_in, seq_out, intent = list(zip(*test_data))
    
    sin = []
    sout = []
    
    for i in range(len(seq_in)):
        temp = seq_in[i]
        if len(temp) < length:
            temp.append('<EOS>')
            while len(temp) < length:
                temp.append('<PAD>')
        else:
            print("exceeded limit")
            temp = temp[:length]
            temp[-1] = '<EOS>'
        sin.append(temp)

        temp = seq_out[i]
        if len(temp) < length:
            while len(temp) < length:
                temp.append('<PAD>')
        else:
            temp = temp[:length]
            temp[-1] = '<PAD>'  # Changed from '<EOS>' to '<PAD>' for tags
        sout.append(temp)
    
    test_processed = []
    for tr in zip(sin, sout, intent):
        temp = prepare_sequence_test(tr[0], word2index, is_tag=False)
        temp = temp.view(1, -1)
        
        temp2 = prepare_sequence_test(tr[1], tag2index, is_tag=True)
        temp2 = temp2.view(1, -1)
        
        # Handle unknown intents
        if tr[2] in intent2index:
            intent_idx = intent2index[tr[2]]
        else:
            # Use the first intent as default for unknown intents
            intent_idx = 0
        
        temp3 = Variable(torch.LongTensor([intent_idx])).cuda() if USE_CUDA else Variable(torch.LongTensor([intent_idx]))
        
        test_processed.append((temp, temp2, temp3))
    
    return test_processed

def evaluate_model(encoder, decoder, test_data, config, word2index, tag2index, intent2index):
    """
    Evaluate the model on test data
    """
    encoder.eval()
    decoder.eval()
    
    intent_preds = []
    intent_labels = []
    slot_preds = []
    slot_labels = []
    total_loss = 0.0
    num_batches = 0
    
    loss_function_1 = nn.CrossEntropyLoss(ignore_index=0)
    loss_function_2 = nn.CrossEntropyLoss()
    
    with torch.no_grad():
        for batch in getBatch(config.batch_size, test_data):
            x, y_1, y_2 = zip(*batch)
            x = torch.cat(x)
            tag_target = torch.cat(y_1)
            intent_target = torch.cat(y_2)
            
            x_mask = torch.cat([Variable(torch.BoolTensor(tuple(map(lambda s: s == 0, t.data)))).cuda() if USE_CUDA else Variable(torch.BoolTensor(tuple(map(lambda s: s == 0, t.data)))) for t in x]).view(config.batch_size, -1)
            
            output, hidden_c = encoder(x, x_mask)
            start_decode = Variable(torch.LongTensor([[word2index['<SOS>']]*config.batch_size])).cuda().transpose(1, 0) if USE_CUDA else Variable(torch.LongTensor([[word2index['<SOS>']]*config.batch_size])).transpose(1, 0)
            
            tag_score, intent_score = decoder(start_decode, hidden_c, output, x_mask)
            
            loss_1 = loss_function_1(tag_score, tag_target.view(-1))
            loss_2 = loss_function_2(intent_score, intent_target)
            loss = loss_1 + loss_2
            
            total_loss += loss.item()
            num_batches += 1
            
            # Get predictions
            intent_pred = torch.argmax(intent_score, dim=1)
            slot_pred = torch.argmax(tag_score, dim=1)
            
            intent_preds.extend(intent_pred.cpu().numpy())
            intent_labels.extend(intent_target.cpu().numpy())
            
            # Process slot predictions (reshape to match target format)
            slot_pred = slot_pred.view(config.batch_size, -1)
            for i in range(config.batch_size):
                pred_slots = []
                true_slots = []
                for j in range(slot_pred.size(1)):
                    if tag_target[i][j].item() != 0:  # Ignore padding
                        pred_slots.append(slot_pred[i][j].item())
                        true_slots.append(tag_target[i][j].item())
                slot_preds.append(pred_slots)
                slot_labels.append(true_slots)
    eval_log_path = os.path.join(config.model_dir, 'eval_output_debug.json')
    example_logs = []

    for i in range(len(intent_preds)):
        example_logs.append({
            'input_tokens': test_data[i][0].cpu().tolist() if USE_CUDA else test_data[i][0].tolist(),
            'input_words': [list(word2index.keys())[list(word2index.values()).index(ix)] if ix in word2index.values() else "<UNK>" for ix in test_data[i][0].view(-1).tolist()],
            'true_slots': [list(tag2index.keys())[list(tag2index.values()).index(ix)] for ix in slot_labels[i]],
            'predicted_slots': [list(tag2index.keys())[list(tag2index.values()).index(ix)] for ix in slot_preds[i]],
            'true_intent': list(intent2index.keys())[list(intent2index.values()).index(intent_labels[i])],
            'predicted_intent': list(intent2index.keys())[list(intent2index.values()).index(intent_preds[i])]
        })

    with open(eval_log_path, 'w', encoding='utf-8') as f:
        json.dump(example_logs, f, indent=2, ensure_ascii=False)
    encoder.train()
    decoder.train()
    
    # Calculate metrics
    avg_loss = total_loss / num_batches
    intent_accuracy = accuracy_score(intent_labels, intent_preds)
    
    # Flatten slot predictions and labels for metric calculation
    flat_slot_preds = [item for sublist in slot_preds for item in sublist]
    flat_slot_labels = [item for sublist in slot_labels for item in sublist]
    
    slot_precision, slot_recall, slot_f1, _ = precision_recall_fscore_support(
        flat_slot_labels, flat_slot_preds, average='weighted', zero_division=0
    )
    
    return {
        'loss': avg_loss,
        'intent_accuracy': intent_accuracy,
        'slot_precision': slot_precision,
        'slot_recall': slot_recall,
        'slot_f1': slot_f1
    }

def train(config):
    
    train_data, word2index, tag2index, intent2index = preprocessing(config.file_path, config.max_length)
    
    if train_data == None:
        print("Please check your data or its path")
        return
    
    # Load test data
    test_file_path = config.file_path.replace('train', 'test')
    test_data = preprocessing_test(test_file_path, config.max_length, word2index, tag2index, intent2index)
    
    if test_data == None:
        print("Test data not found, continuing without evaluation")
    
    encoder = Encoder(len(word2index), config.embedding_size, config.hidden_size)
    decoder = Decoder(len(tag2index), len(intent2index), len(tag2index)//3, config.hidden_size*2)
    
    if USE_CUDA:
        encoder = encoder.cuda()
        decoder = decoder.cuda()

    encoder.init_weights()
    decoder.init_weights()

    loss_function_1 = nn.CrossEntropyLoss(ignore_index=0)
    loss_function_2 = nn.CrossEntropyLoss()
    enc_optim = optim.Adam(encoder.parameters(), lr=config.learning_rate)
    dec_optim = optim.Adam(decoder.parameters(), lr=config.learning_rate)
    
    best_intent_acc = 0.0
    patience_counter = 0
    best_encoder_state = None
    best_decoder_state = None

    print("Starting training...")
    for step in range(config.step_size):
        losses = []
        for i, batch in enumerate(getBatch(config.batch_size, train_data)):
            x, y_1, y_2 = zip(*batch)
            x = torch.cat(x)
            tag_target = torch.cat(y_1)
            intent_target = torch.cat(y_2)
            x_mask = torch.cat([Variable(torch.BoolTensor(tuple(map(lambda s: s == 0, t.data)))).cuda() if USE_CUDA else Variable(torch.BoolTensor(tuple(map(lambda s: s == 0, t.data)))) for t in x]).view(config.batch_size, -1)
            y_1_mask = torch.cat([Variable(torch.BoolTensor(tuple(map(lambda s: s == 0, t.data)))).cuda() if USE_CUDA else Variable(torch.BoolTensor(tuple(map(lambda s: s == 0, t.data)))) for t in tag_target]).view(config.batch_size, -1)

            encoder.zero_grad()
            decoder.zero_grad()

            output, hidden_c = encoder(x, x_mask)
            start_decode = Variable(torch.LongTensor([[word2index['<SOS>']]*config.batch_size])).cuda().transpose(1, 0) if USE_CUDA else Variable(torch.LongTensor([[word2index['<SOS>']]*config.batch_size])).transpose(1, 0)

            tag_score, intent_score = decoder(start_decode, hidden_c, output, x_mask)

            loss_1 = loss_function_1(tag_score, tag_target.view(-1))
            loss_2 = loss_function_2(intent_score, intent_target)

            loss = loss_1 + loss_2
            losses.append(loss.item())

            loss.backward()

            torch.nn.utils.clip_grad_norm_(encoder.parameters(), 5.0)
            torch.nn.utils.clip_grad_norm_(decoder.parameters(), 5.0)

            enc_optim.step()
            dec_optim.step()

            if i % 100 == 0:
                print(f"Step {step}, epoch {i}: {np.mean(losses):.4f}")
                losses = []
        
        if test_data:
            eval_results = evaluate_model(encoder, decoder, test_data, config, word2index, tag2index, intent2index)
            current_eval_loss = eval_results['loss']
            
            print(f"Epoch {step} Evaluation Results:")
            print(f"  Loss: {current_eval_loss:.4f}")
            print(f"  Intent Accuracy: {eval_results['intent_accuracy']:.4f}")
            print(f"  Slot F1: {eval_results['slot_f1']:.4f}")
            print(f"  Slot Precision: {eval_results['slot_precision']:.4f}")
            print(f"  Slot Recall: {eval_results['slot_recall']:.4f}")
            
            if eval_results['intent_accuracy'] > best_intent_acc:
                best_intent_acc = eval_results['intent_accuracy']
                patience_counter = 0
                best_encoder_state = encoder.state_dict().copy()
                best_decoder_state = decoder.state_dict().copy()
                print(f"  *** New best model! (intent accuracy: {best_intent_acc:.4f}) ***")
            else:
                patience_counter += 1
                print(f"  No improvement in intent accuracy. Patience: {patience_counter}/{config.patience}")
                
                if patience_counter >= config.patience:
                    print(f"Early stopping triggered after {step + 1} epochs!")
                    print(f"Best eval loss: {best_intent_acc:.4f}")
                    if best_encoder_state and best_decoder_state:
                        encoder.load_state_dict(best_encoder_state)
                        decoder.load_state_dict(best_decoder_state)
                        print("Restored best model weights.")
                    break
            
            print("-" * 50)
    
    if not os.path.exists(config.model_dir):
        os.makedirs(config.model_dir)
    
    if best_encoder_state and best_decoder_state:
        torch.save(best_decoder_state, os.path.join(config.model_dir, 'jointnlu-decoder.pkl'))
        torch.save(best_encoder_state, os.path.join(config.model_dir, 'jointnlu-encoder.pkl'))
        print(f"Saved best model with eval loss: {best_intent_acc:.4f}")
    else:
        torch.save(decoder.state_dict(), os.path.join(config.model_dir, 'jointnlu-decoder.pkl'))
        torch.save(encoder.state_dict(), os.path.join(config.model_dir, 'jointnlu-encoder.pkl'))
        print("Saved final model")
    
    print("Train Complete!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, default='./data/Massive/train/Massive.train.w-intent.iob',
                        help='path of train data')
    parser.add_argument('--model_dir', type=str, default='./models/',
                        help='path for saving trained models')

    # Model parameters - adjusted for better performance
    parser.add_argument('--max_length', type=int, default=50,
                        help='max sequence length')
    parser.add_argument('--embedding_size', type=int, default=128,
                        help='dimension of word embedding vectors')
    parser.add_argument('--hidden_size', type=int, default=128,
                        help='dimension of lstm hidden states')
    parser.add_argument('--num_layers', type=int, default=2,
                        help='number of layers in lstm')
    
    parser.add_argument('--step_size', type=int, default=100)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--learning_rate', type=float, default=0.001)
    parser.add_argument('--patience', type=int, default=10, 
                        help='number of epochs to wait before early stopping')
    config = parser.parse_args()
    train(config)