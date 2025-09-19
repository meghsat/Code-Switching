import torch
from torch.autograd import Variable
import argparse
import pickle
import os
from model import Encoder, Decoder

USE_CUDA = torch.cuda.is_available()

def prepare_sequence(seq, to_ix):
    idxs = [to_ix[w] if w in to_ix else to_ix["<UNK>"] for w in seq]
    tensor = Variable(torch.LongTensor(idxs)).view(1, -1)
    return tensor.cuda() if USE_CUDA else tensor

def load_vocab_from_pkl(pkl_path):
    _, word2index, tag2index, intent2index = pickle.load(open(pkl_path, "rb"))
    return word2index, tag2index, intent2index

def predict(sentence, encoder, decoder, word2index, tag2index, intent2index, max_length=50):
    index2tag = {v: k for k, v in tag2index.items()}
    index2intent = {v: k for k, v in intent2index.items()}

    tokens = sentence.strip().split()

    # Preprocess sentence: truncate + pad
    if len(tokens) >= max_length:
        tokens = tokens[:max_length - 1]
    tokens.append('<EOS>')
    while len(tokens) < max_length:
        tokens.append('<PAD>')

    input_tensor = prepare_sequence(tokens, word2index)
    input_mask = (input_tensor == word2index['<PAD>'])
    if USE_CUDA:
        input_mask = input_mask.cuda()

    with torch.no_grad():
        encoder.eval()
        decoder.eval()

        output, hidden_c = encoder(input_tensor, input_mask)

        start_decode = torch.LongTensor([[word2index['<SOS>']]]).cuda() if USE_CUDA else torch.LongTensor([[word2index['<SOS>']]])
        tag_scores, intent_scores = decoder(start_decode.transpose(1, 0), hidden_c, output, input_mask)

        pred_intent_idx = torch.argmax(intent_scores, dim=1).item()
        pred_intent = index2intent[pred_intent_idx]

        pred_tags = torch.argmax(tag_scores, dim=1).view(-1).tolist()
        pred_tags = [index2tag[idx] for idx in pred_tags[:len(tokens)]]

        return tokens, pred_tags, pred_intent

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sentence", type=str, required=True)
    parser.add_argument("--model_dir", type=str, default="./models/")
    parser.add_argument("--data_pkl", type=str, default="./data/processed_train_data.pkl")
    parser.add_argument("--embedding_size", type=int, default=128)
    parser.add_argument("--hidden_size", type=int, default=128)
    parser.add_argument("--max_length", type=int, default=50)
    args = parser.parse_args()

    # Load vocab
    word2index, tag2index, intent2index = load_vocab_from_pkl(args.data_pkl)

    # Load models
    encoder = Encoder(len(word2index), args.embedding_size, args.hidden_size)
    decoder = Decoder(len(tag2index), len(intent2index), len(tag2index) // 3, args.hidden_size * 2)

    encoder.load_state_dict(torch.load(os.path.join(args.model_dir, "jointnlu-encoder.pkl"), map_location="cuda" if USE_CUDA else "cpu"))
    decoder.load_state_dict(torch.load(os.path.join(args.model_dir, "jointnlu-decoder.pkl"), map_location="cuda" if USE_CUDA else "cpu"))

    if USE_CUDA:
        encoder = encoder.cuda()
        decoder = decoder.cuda()

    tokens, tags, intent = predict(args.sentence, encoder, decoder, word2index, tag2index, intent2index, args.max_length)

    print(f"\nInput Sentence: {' '.join(tokens)}")
    print(f"Predicted Intent: {intent}")
    print("Predicted Slots:")
    for tok, tag in zip(tokens, tags):
        if tok != '<PAD>':
            print(f"  {tok:10} --> {tag}")
