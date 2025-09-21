
Refer to the Main_dataset folder for the final version
train folder: 100 to 300, 500 to 1300, 1500 to 2400, 2700 to 2800, 2900 to 3900, 4000 to 4300, 4500 to 4600, 4800 to 5017 <br>

test folder: 301 to 499, 1301 to 1499, 2401 to 2500, 2801 to 2899, 3901 to 3999, 4301 to 4400, 4401–4499, 4601 to 4799 <br>

dev folder: 2501–2699 <br>


## Atis
(base) PS C:\Users\SDEVINEN\Downloads\projects\pers\JointBERT-master\JointBERT-master> python main.py --task atis --model_type bert --model_dir massive_model_bert_new --do_train --do_eval
09/20/2025 19:45:38 - INFO - data_loader -   Creating features from dataset file at ./data
09/20/2025 19:45:38 - INFO - data_loader -   LOOKING AT ./data\atis\train
09/20/2025 19:45:38 - INFO - data_loader -   Writing example 0 of 3724
09/20/2025 19:45:38 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:38 - INFO - data_loader -   guid: train-0
09/20/2025 19:45:38 - INFO - data_loader -   tokens: [CLS] mu ##j ##he is _ week sub ##ah pa ##an ##ch _ ba ##je ut ##ha do [SEP]
09/20/2025 19:45:38 - INFO - data_loader -   input_ids: 101 14163 3501 5369 2003 1035 2733 4942 4430 6643 2319 2818 1035 8670 6460 21183 3270 2079 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   intent_label: 48 (id = 48)
09/20/2025 19:45:38 - INFO - data_loader -   slot_labels: 0 2 0 0 11 0 0 2 0 40 0 0 0 0 0 2 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:38 - INFO - data_loader -   guid: train-1
09/20/2025 19:45:38 - INFO - data_loader -   tokens: [CLS] mu ##j ##he friday sub ##ah 9 _ ba ##je ut ##ha den ##a [SEP]
09/20/2025 19:45:38 - INFO - data_loader -   input_ids: 101 14163 3501 5369 5958 4942 4430 1023 1035 8670 6460 21183 3270 7939 2050 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   intent_label: 48 (id = 48)
09/20/2025 19:45:38 - INFO - data_loader -   slot_labels: 0 2 0 0 11 2 0 40 0 0 0 2 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:38 - INFO - data_loader -   guid: train-2
09/20/2025 19:45:38 - INFO - data_loader -   tokens: [CLS] ab _ se _ do _ g ##han ##te _ ba ##ad ka alarm set ka ##ro [SEP]
09/20/2025 19:45:38 - INFO - data_loader -   input_ids: 101 11113 1035 7367 1035 2079 1035 1043 4819 2618 1035 8670 4215 10556 8598 2275 10556 3217 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   intent_label: 48 (id = 48)
09/20/2025 19:45:38 - INFO - data_loader -   slot_labels: 0 40 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:38 - INFO - data_loader -   guid: train-3
09/20/2025 19:45:38 - INFO - data_loader -   tokens: [CLS] shan ##t ho ja ##ao [SEP]
09/20/2025 19:45:38 - INFO - data_loader -   input_ids: 101 17137 2102 7570 14855 7113 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   intent_label: 49 (id = 49)
09/20/2025 19:45:38 - INFO - data_loader -   slot_labels: 0 2 0 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:38 - INFO - data_loader -   guid: train-4
09/20/2025 19:45:38 - INFO - data_loader -   tokens: [CLS] ol ##ly , za ##ra shan ##t ho ja ##ao [SEP]
09/20/2025 19:45:38 - INFO - data_loader -   input_ids: 101 19330 2135 1010 23564 2527 17137 2102 7570 14855 7113 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0       
09/20/2025 19:45:38 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:38 - INFO - data_loader -   intent_label: 49 (id = 49)
09/20/2025 19:45:38 - INFO - data_loader -   slot_labels: 0 2 0 0 2 0 2 0 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   Saving features into cached file ./data\cached_train_atis_bert-base-uncased_50
09/20/2025 19:45:39 - INFO - data_loader -   Creating features from dataset file at ./data
09/20/2025 19:45:39 - INFO - data_loader -   LOOKING AT ./data\atis\dev
09/20/2025 19:45:39 - INFO - data_loader -   Writing example 0 of 199
09/20/2025 19:45:39 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:39 - INFO - data_loader -   guid: dev-0
09/20/2025 19:45:39 - INFO - data_loader -   tokens: [CLS] ky ##a ko ##i nay ##i environmental news hai [SEP]
09/20/2025 19:45:39 - INFO - data_loader -   input_ids: 101 18712 2050 12849 2072 29349 2072 4483 2739 15030 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   intent_label: 30 (id = 30)
09/20/2025 19:45:39 - INFO - data_loader -   slot_labels: 0 2 0 2 0 2 0 28 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:39 - INFO - data_loader -   guid: dev-1
09/20/2025 19:45:39 - INFO - data_loader -   tokens: [CLS] international news mein ky ##a cha ##l ra ##ha hai [SEP]
09/20/2025 19:45:39 - INFO - data_loader -   input_ids: 101 2248 2739 24182 18712 2050 15775 2140 10958 3270 15030 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0      
09/20/2025 19:45:39 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   intent_label: 30 (id = 30)
09/20/2025 19:45:39 - INFO - data_loader -   slot_labels: 0 32 2 2 2 0 2 0 2 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:39 - INFO - data_loader -   guid: dev-2
09/20/2025 19:45:39 - INFO - data_loader -   tokens: [CLS] mu ##j ##he international news ke ba ##are mein bat ##ao [SEP]
09/20/2025 19:45:39 - INFO - data_loader -   input_ids: 101 14163 3501 5369 2248 2739 17710 8670 12069 24182 7151 7113 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0    
09/20/2025 19:45:39 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   intent_label: 30 (id = 30)
09/20/2025 19:45:39 - INFO - data_loader -   slot_labels: 0 2 0 0 32 2 2 2 0 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:39 - INFO - data_loader -   guid: dev-3
09/20/2025 19:45:39 - INFO - data_loader -   tokens: [CLS] latest international news ky ##a hai [SEP]
09/20/2025 19:45:39 - INFO - data_loader -   input_ids: 101 6745 2248 2739 18712 2050 15030 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   intent_label: 30 (id = 30)
09/20/2025 19:45:39 - INFO - data_loader -   slot_labels: 0 2 32 2 2 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:39 - INFO - data_loader -   guid: dev-4
09/20/2025 19:45:39 - INFO - data_loader -   tokens: [CLS] mu ##j ##he ab ##hi coffee cha ##hi ##ye [SEP]
09/20/2025 19:45:39 - INFO - data_loader -   input_ids: 101 14163 3501 5369 11113 4048 4157 15775 4048 6672 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   intent_label: 18 (id = 18)
09/20/2025 19:45:39 - INFO - data_loader -   slot_labels: 0 2 0 0 2 0 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   Saving features into cached file ./data\cached_dev_atis_bert-base-uncased_50
09/20/2025 19:45:39 - INFO - data_loader -   Creating features from dataset file at ./data
09/20/2025 19:45:39 - INFO - data_loader -   LOOKING AT ./data\atis\test
09/20/2025 19:45:39 - INFO - data_loader -   Writing example 0 of 1094
09/20/2025 19:45:39 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:39 - INFO - data_loader -   guid: test-0
09/20/2025 19:45:39 - INFO - data_loader -   tokens: [CLS] mu ##j ##he su ##shi cha ##hi ##ye , ky ##a tu ##m lunch order ka ##r sa ##kt ##e ho [SEP]
09/20/2025 19:45:39 - INFO - data_loader -   input_ids: 101 14163 3501 5369 10514 6182 15775 4048 6672 1010 18712 2050 10722 2213 6265 2344 10556 2099 7842 25509 2063 7570 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   intent_label: 41 (id = 41)
09/20/2025 19:45:39 - INFO - data_loader -   slot_labels: 0 2 0 0 15 0 2 0 0 0 2 0 2 0 21 2 2 0 2 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:39 - INFO - data_loader -   guid: test-1
09/20/2025 19:45:39 - INFO - data_loader -   tokens: [CLS] alexa , mu ##j ##he su ##shi cha ##hi ##ye , ky ##a tu ##m lunch order ka ##r sa ##kt ##e ho [SEP]
09/20/2025 19:45:39 - INFO - data_loader -   input_ids: 101 24969 1010 14163 3501 5369 10514 6182 15775 4048 6672 1010 18712 2050 10722 2213 6265 2344 10556 2099 7842 25509 2063 7570 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   intent_label: 41 (id = 41)
09/20/2025 19:45:39 - INFO - data_loader -   slot_labels: 0 2 0 2 0 0 15 0 2 0 0 0 2 0 2 0 21 2 2 0 2 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:39 - INFO - data_loader -   guid: test-2
09/20/2025 19:45:39 - INFO - data_loader -   tokens: [CLS] take ##away sandwich au ##r soup italian ' s se order ka ##ro [SEP]
09/20/2025 19:45:39 - INFO - data_loader -   input_ids: 101 2202 9497 11642 8740 2099 11350 3059 1005 1055 7367 2344 10556 3217 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   intent_label: 41 (id = 41)
09/20/2025 19:45:39 - INFO - data_loader -   slot_labels: 0 30 0 15 2 0 15 2 0 0 2 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:39 - INFO - data_loader -   guid: test-3
09/20/2025 19:45:39 - INFO - data_loader -   tokens: [CLS] is sa ##al mein kit ##ne din bach ##e hai ##n [SEP]
09/20/2025 19:45:39 - INFO - data_loader -   input_ids: 101 2003 7842 2389 24182 8934 2638 11586 10384 2063 15030 2078 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0    
09/20/2025 19:45:39 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   intent_label: 12 (id = 12)
09/20/2025 19:45:39 - INFO - data_loader -   slot_labels: 0 2 2 0 2 2 0 2 2 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   *** Example ***
09/20/2025 19:45:39 - INFO - data_loader -   guid: test-4
09/20/2025 19:45:39 - INFO - data_loader -   tokens: [CLS] is sa ##al new year ' s eve ki ##s din hai [SEP]
09/20/2025 19:45:39 - INFO - data_loader -   input_ids: 101 2003 7842 2389 2047 2095 1005 1055 6574 11382 2015 11586 15030 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  
09/20/2025 19:45:39 - INFO - data_loader -   attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:39 - INFO - data_loader -   intent_label: 12 (id = 12)
09/20/2025 19:45:39 - INFO - data_loader -   slot_labels: 0 2 2 0 2 2 0 0 2 2 0 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
09/20/2025 19:45:40 - INFO - data_loader -   Saving features into cached file ./data\cached_test_atis_bert-base-uncased_50
Some weights of JointBERT were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['intent_classifier.linear.bias', 'intent_classifier.linear.weight', 'slot_classifier.linear.bias', 'slot_classifier.linear.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
09/20/2025 19:45:40 - INFO - trainer -   ***** Running training *****
09/20/2025 19:45:40 - INFO - trainer -     Num examples = 3724
09/20/2025 19:45:40 - INFO - trainer -     Num Epochs = 50
09/20/2025 19:45:40 - INFO - trainer -     Total train batch size = 32
09/20/2025 19:45:40 - INFO - trainer -     Gradient Accumulation steps = 1
09/20/2025 19:45:40 - INFO - trainer -     Total optimization steps = 5850
09/20/2025 19:45:40 - INFO - trainer -     Logging steps = 200
09/20/2025 19:45:40 - INFO - trainer -     Save steps = 200
Epoch:   0%|                                                                                                                                                                    | 0/50 [00:00<?, ?it/s]C:\Users\SDEVINEN\AppData\Local\miniforge3\Lib\site-packages\torch\nn\modules\module.py:1784: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [07:08<00:00,  3.66s/it]
09/20/2025 19:52:49 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [07:08<00:00,  2.76s/it] 
09/20/2025 19:52:49 - INFO - trainer -     Num examples = 199
09/20/2025 19:52:49 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.11s/it]
09/20/2025 19:52:53 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.07it/s]
09/20/2025 19:52:53 - INFO - trainer -     intent_acc = 0.5979899497487438
09/20/2025 19:52:53 - INFO - trainer -     loss = 2.05736380815506
09/20/2025 19:52:53 - INFO - trainer -     sementic_frame_acc = 0.4120603015075377
09/20/2025 19:52:53 - INFO - trainer -     slot_f1 = 0.6017699115044247
09/20/2025 19:52:53 - INFO - trainer -     slot_precision = 0.6710526315789473
09/20/2025 19:52:53 - INFO - trainer -     slot_recall = 0.5454545454545454
09/20/2025 19:52:53 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Epoch:   2%|███                                                                                                                                                      | 1/50 [07:13<5:53:58, 433.43s/it]09/20/2025 19:56:58 - INFO - trainer -   ***** Running evaluation on dev dataset *****████████████████████████████████████▏                                            | 82/117 [04:01<01:42,  2.92s/it] 
09/20/2025 19:56:58 - INFO - trainer -     Num examples = 199
09/20/2025 19:56:58 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.16s/it]
09/20/2025 19:57:02 - INFO - trainer -   ***** Eval results *****
09/20/2025 19:57:02 - INFO - trainer -     intent_acc = 0.7989949748743719███████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.04it/s] 
09/20/2025 19:57:02 - INFO - trainer -     loss = 1.153725266456604
09/20/2025 19:57:02 - INFO - trainer -     sementic_frame_acc = 0.507537688442211
09/20/2025 19:57:02 - INFO - trainer -     slot_f1 = 0.6647058823529411
09/20/2025 19:57:02 - INFO - trainer -     slot_precision = 0.738562091503268
09/20/2025 19:57:02 - INFO - trainer -     slot_recall = 0.6042780748663101
09/20/2025 19:57:03 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [06:02<00:00,  3.10s/it]
09/20/2025 19:58:55 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [06:02<00:00,  3.20s/it] 
09/20/2025 19:58:55 - INFO - trainer -     Num examples = 199
09/20/2025 19:58:55 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.21s/it]
09/20/2025 19:59:00 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.01s/it] 
09/20/2025 19:59:00 - INFO - trainer -     intent_acc = 0.7839195979899497
09/20/2025 19:59:00 - INFO - trainer -     loss = 1.0431800186634064
09/20/2025 19:59:00 - INFO - trainer -     sementic_frame_acc = 0.5276381909547738
09/20/2025 19:59:00 - INFO - trainer -     slot_f1 = 0.6855524079320112
09/20/2025 19:59:00 - INFO - trainer -     slot_precision = 0.7289156626506024
09/20/2025 19:59:00 - INFO - trainer -     slot_recall = 0.6470588235294118
09/20/2025 19:59:01 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [06:10<00:00,  3.17s/it]
09/20/2025 20:05:12 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [06:10<00:00,  2.78s/it] 
09/20/2025 20:05:12 - INFO - trainer -     Num examples = 199
09/20/2025 20:05:12 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.14s/it]
09/20/2025 20:05:16 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.05it/s] 
09/20/2025 20:05:16 - INFO - trainer -     intent_acc = 0.8442211055276382
09/20/2025 20:05:16 - INFO - trainer -     loss = 0.8402033448219299
09/20/2025 20:05:16 - INFO - trainer -     sementic_frame_acc = 0.6180904522613065
09/20/2025 20:05:16 - INFO - trainer -     slot_f1 = 0.7611111111111112
09/20/2025 20:05:16 - INFO - trainer -     slot_precision = 0.791907514450867
09/20/2025 20:05:16 - INFO - trainer -     slot_recall = 0.732620320855615
09/20/2025 20:05:16 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Epoch:   6%|█████████▏                                                                                                                                               | 3/50 [19:36<5:02:21, 385.99s/it]09/20/2025 20:08:31 - INFO - trainer -   ***** Running evaluation on dev dataset *****                                                                                 | 48/117 [03:10<04:28,  3.89s/it] 
09/20/2025 20:08:31 - INFO - trainer -     Num examples = 199
09/20/2025 20:08:31 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:06<00:00,  1.50s/it]
09/20/2025 20:08:37 - INFO - trainer -   ***** Eval results *****
09/20/2025 20:08:37 - INFO - trainer -     intent_acc = 0.8743718592964824███████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:06<00:00,  1.26s/it] 
09/20/2025 20:08:37 - INFO - trainer -     loss = 0.7152219712734222
09/20/2025 20:08:37 - INFO - trainer -     sementic_frame_acc = 0.678391959798995
09/20/2025 20:08:37 - INFO - trainer -     slot_f1 = 0.7978723404255319
09/20/2025 20:08:37 - INFO - trainer -     slot_precision = 0.7936507936507936
09/20/2025 20:08:37 - INFO - trainer -     slot_recall = 0.8021390374331551
09/20/2025 20:08:38 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [07:54<00:00,  4.06s/it]
09/20/2025 20:13:11 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [07:54<00:00,  3.41s/it] 
09/20/2025 20:13:11 - INFO - trainer -     Num examples = 199
09/20/2025 20:13:11 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:05<00:00,  1.50s/it]
09/20/2025 20:13:17 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:05<00:00,  1.25s/it] 
09/20/2025 20:13:17 - INFO - trainer -     intent_acc = 0.8793969849246231
09/20/2025 20:13:17 - INFO - trainer -     loss = 0.7245225012302399
09/20/2025 20:13:17 - INFO - trainer -     sementic_frame_acc = 0.6884422110552764
09/20/2025 20:13:17 - INFO - trainer -     slot_f1 = 0.8109589041095892
09/20/2025 20:13:17 - INFO - trainer -     slot_precision = 0.8314606741573034
09/20/2025 20:13:17 - INFO - trainer -     slot_recall = 0.7914438502673797
09/20/2025 20:13:18 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [07:49<00:00,  4.02s/it]
09/20/2025 20:21:08 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [07:49<00:00,  3.19s/it] 
09/20/2025 20:21:08 - INFO - trainer -     Num examples = 199
09/20/2025 20:21:08 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:05<00:00,  1.48s/it]
09/20/2025 20:21:14 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:05<00:00,  1.25s/it] 
09/20/2025 20:21:14 - INFO - trainer -     intent_acc = 0.8693467336683417
09/20/2025 20:21:14 - INFO - trainer -     loss = 0.5593768432736397
09/20/2025 20:21:14 - INFO - trainer -     sementic_frame_acc = 0.7035175879396985
09/20/2025 20:21:14 - INFO - trainer -     slot_f1 = 0.8319559228650136
09/20/2025 20:21:14 - INFO - trainer -     slot_precision = 0.8579545454545454
09/20/2025 20:21:14 - INFO - trainer -     slot_recall = 0.8074866310160428
09/20/2025 20:21:14 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Epoch:  10%|███████████████▎                                                                                                                                         | 5/50 [35:34<5:31:59, 442.65s/it]09/20/2025 20:22:15 - INFO - trainer -   ***** Running evaluation on dev dataset *****                                                                                 | 14/117 [00:56<06:55,  4.04s/it] 
09/20/2025 20:22:15 - INFO - trainer -     Num examples = 199
09/20/2025 20:22:15 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:06<00:00,  1.52s/it]
09/20/2025 20:22:21 - INFO - trainer -   ***** Eval results *****
09/20/2025 20:22:21 - INFO - trainer -     intent_acc = 0.8894472361809045███████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:06<00:00,  1.29s/it] 
09/20/2025 20:22:21 - INFO - trainer -     loss = 0.5182161256670952
09/20/2025 20:22:21 - INFO - trainer -     sementic_frame_acc = 0.6884422110552764
09/20/2025 20:22:21 - INFO - trainer -     slot_f1 = 0.8128342245989305
09/20/2025 20:22:21 - INFO - trainer -     slot_precision = 0.8128342245989305
09/20/2025 20:22:21 - INFO - trainer -     slot_recall = 0.8128342245989305
09/20/2025 20:22:21 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [07:57<00:00,  4.08s/it]
09/20/2025 20:29:12 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [07:57<00:00,  3.38s/it] 
09/20/2025 20:29:12 - INFO - trainer -     Num examples = 199
09/20/2025 20:29:12 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:05<00:00,  1.48s/it]
09/20/2025 20:29:18 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:05<00:00,  1.24s/it] 
09/20/2025 20:29:18 - INFO - trainer -     intent_acc = 0.8894472361809045
09/20/2025 20:29:18 - INFO - trainer -     loss = 0.5100032687187195
09/20/2025 20:29:18 - INFO - trainer -     sementic_frame_acc = 0.7035175879396985
09/20/2025 20:29:18 - INFO - trainer -     slot_f1 = 0.8228882833787466
09/20/2025 20:29:18 - INFO - trainer -     slot_precision = 0.8388888888888889
09/20/2025 20:29:18 - INFO - trainer -     slot_recall = 0.8074866310160428
09/20/2025 20:29:18 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Epoch:  12%|██████████████████▎                                                                                                                                      | 6/50 [43:38<5:34:58, 456.80s/it]09/20/2025 20:36:01 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████▎                         | 97/117 [06:38<01:22,  4.14s/it] 
09/20/2025 20:36:01 - INFO - trainer -     Num examples = 199
09/20/2025 20:36:01 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:06<00:00,  1.55s/it]
09/20/2025 20:36:07 - INFO - trainer -   ***** Eval results *****
09/20/2025 20:36:07 - INFO - trainer -     intent_acc = 0.914572864321608████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:06<00:00,  1.29s/it] 
09/20/2025 20:36:07 - INFO - trainer -     loss = 0.48275580257177353
09/20/2025 20:36:07 - INFO - trainer -     sementic_frame_acc = 0.7135678391959799
09/20/2025 20:36:07 - INFO - trainer -     slot_f1 = 0.8199445983379501
09/20/2025 20:36:07 - INFO - trainer -     slot_precision = 0.8505747126436781
09/20/2025 20:36:07 - INFO - trainer -     slot_recall = 0.7914438502673797
09/20/2025 20:36:08 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [08:03<00:00,  4.14s/it]
09/20/2025 20:37:22 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [08:03<00:00,  3.36s/it] 
09/20/2025 20:37:22 - INFO - trainer -     Num examples = 199
09/20/2025 20:37:22 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:06<00:00,  1.51s/it]
09/20/2025 20:37:28 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:06<00:00,  1.27s/it] 
09/20/2025 20:37:28 - INFO - trainer -     intent_acc = 0.9095477386934674
09/20/2025 20:37:28 - INFO - trainer -     loss = 0.507107175886631
09/20/2025 20:37:28 - INFO - trainer -     sementic_frame_acc = 0.7236180904522613
09/20/2025 20:37:28 - INFO - trainer -     slot_f1 = 0.825136612021858
09/20/2025 20:37:28 - INFO - trainer -     slot_precision = 0.8435754189944135
09/20/2025 20:37:28 - INFO - trainer -     slot_recall = 0.8074866310160428
09/20/2025 20:37:29 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [06:55<00:00,  3.55s/it]
09/20/2025 20:44:24 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [06:55<00:00,  2.54s/it] 
09/20/2025 20:44:24 - INFO - trainer -     Num examples = 199
09/20/2025 20:44:24 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.24s/it]
09/20/2025 20:44:29 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.04s/it] 
09/20/2025 20:44:29 - INFO - trainer -     intent_acc = 0.8844221105527639
09/20/2025 20:44:29 - INFO - trainer -     loss = 0.5262194611132145
09/20/2025 20:44:29 - INFO - trainer -     sementic_frame_acc = 0.7185929648241206
09/20/2025 20:44:29 - INFO - trainer -     slot_f1 = 0.8365650969529085
09/20/2025 20:44:29 - INFO - trainer -     slot_precision = 0.867816091954023
09/20/2025 20:44:29 - INFO - trainer -     slot_recall = 0.8074866310160428
09/20/2025 20:44:29 - INFO - trainer -   No improvement for 1 epochs
Epoch:  16%|████████████████████████▍                                                                                                                                | 8/50 [58:49<5:16:49, 452.61s/it]09/20/2025 20:47:46 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████▊                                                                     | 63/117 [03:13<02:44,  3.05s/it] 
09/20/2025 20:47:46 - INFO - trainer -     Num examples = 199
09/20/2025 20:47:46 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.25s/it]
09/20/2025 20:47:51 - INFO - trainer -   ***** Eval results *****
09/20/2025 20:47:51 - INFO - trainer -     intent_acc = 0.8793969849246231███████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.05s/it] 
09/20/2025 20:47:51 - INFO - trainer -     loss = 0.5956237092614174
09/20/2025 20:47:51 - INFO - trainer -     sementic_frame_acc = 0.7085427135678392
09/20/2025 20:47:51 - INFO - trainer -     slot_f1 = 0.8166666666666668
09/20/2025 20:47:51 - INFO - trainer -     slot_precision = 0.8497109826589595
09/20/2025 20:47:51 - INFO - trainer -     slot_recall = 0.786096256684492
09/20/2025 20:47:51 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [06:15<00:00,  3.21s/it]
09/20/2025 20:50:44 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [06:15<00:00,  3.05s/it] 
09/20/2025 20:50:44 - INFO - trainer -     Num examples = 199
09/20/2025 20:50:44 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:05<00:00,  1.39s/it]
09/20/2025 20:50:50 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:05<00:00,  1.16s/it] 
09/20/2025 20:50:50 - INFO - trainer -     intent_acc = 0.8793969849246231
09/20/2025 20:50:50 - INFO - trainer -     loss = 0.5459595955908298
09/20/2025 20:50:50 - INFO - trainer -     sementic_frame_acc = 0.7135678391959799
09/20/2025 20:50:50 - INFO - trainer -     slot_f1 = 0.8351648351648351
09/20/2025 20:50:50 - INFO - trainer -     slot_precision = 0.8587570621468926
09/20/2025 20:50:50 - INFO - trainer -     slot_recall = 0.8128342245989305
09/20/2025 20:50:50 - INFO - trainer -   No improvement for 2 epochs
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [05:51<00:00,  3.00s/it] 
09/20/2025 20:56:41 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [05:51<00:00,  2.38s/it] 
09/20/2025 20:56:41 - INFO - trainer -     Num examples = 199
09/20/2025 20:56:41 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.11s/it]
09/20/2025 20:56:46 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.07it/s] 
09/20/2025 20:56:46 - INFO - trainer -     intent_acc = 0.8592964824120602
09/20/2025 20:56:46 - INFO - trainer -     loss = 0.8039891123771667
09/20/2025 20:56:46 - INFO - trainer -     sementic_frame_acc = 0.6733668341708543
09/20/2025 20:56:46 - INFO - trainer -     slot_f1 = 0.8142076502732241
09/20/2025 20:56:46 - INFO - trainer -     slot_precision = 0.8324022346368715
09/20/2025 20:56:46 - INFO - trainer -     slot_recall = 0.7967914438502673
09/20/2025 20:56:46 - INFO - trainer -   No improvement for 3 epochs
Epoch:  20%|██████████████████████████████                                                                                                                        | 10/50 [1:11:05<4:31:28, 407.22s/it]09/20/2025 20:58:14 - INFO - trainer -   ***** Running evaluation on dev dataset *****                                                                                 | 29/117 [01:24<04:33,  3.11s/it] 
09/20/2025 20:58:14 - INFO - trainer -     Num examples = 199
09/20/2025 20:58:14 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.23s/it]
09/20/2025 20:58:19 - INFO - trainer -   ***** Eval results *****
09/20/2025 20:58:19 - INFO - trainer -     intent_acc = 0.8844221105527639███████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.03s/it] 
09/20/2025 20:58:19 - INFO - trainer -     loss = 0.6165452599525452
09/20/2025 20:58:19 - INFO - trainer -     sementic_frame_acc = 0.7286432160804021
09/20/2025 20:58:19 - INFO - trainer -     slot_f1 = 0.8435754189944135
09/20/2025 20:58:19 - INFO - trainer -     slot_precision = 0.8830409356725146
09/20/2025 20:58:19 - INFO - trainer -     slot_recall = 0.8074866310160428
09/20/2025 20:58:19 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [06:04<00:00,  3.12s/it]
09/20/2025 21:02:50 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [06:04<00:00,  2.63s/it] 
09/20/2025 21:02:50 - INFO - trainer -     Num examples = 199
09/20/2025 21:02:50 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.24s/it]
09/20/2025 21:02:55 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.04s/it] 
09/20/2025 21:02:55 - INFO - trainer -     intent_acc = 0.8894472361809045
09/20/2025 21:02:55 - INFO - trainer -     loss = 0.6620801836252213
09/20/2025 21:02:55 - INFO - trainer -     sementic_frame_acc = 0.6934673366834171
09/20/2025 21:02:55 - INFO - trainer -     slot_f1 = 0.8210526315789474
09/20/2025 21:02:55 - INFO - trainer -     slot_precision = 0.8082901554404145
09/20/2025 21:02:55 - INFO - trainer -     slot_recall = 0.8342245989304813
09/20/2025 21:02:55 - INFO - trainer -   No improvement for 4 epochs
Epoch:  22%|█████████████████████████████████                                                                                                                     | 11/50 [1:17:15<4:17:11, 395.69s/it]09/20/2025 21:08:39 - INFO - trainer -   ***** Running evaluation on dev dataset *****█████████████████████████████████████████████████████████████████████████▋      | 112/117 [05:40<00:15,  3.14s/it] 
09/20/2025 21:08:39 - INFO - trainer -     Num examples = 199
09/20/2025 21:08:39 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:05<00:00,  1.27s/it]
09/20/2025 21:08:44 - INFO - trainer -   ***** Eval results *****
09/20/2025 21:08:44 - INFO - trainer -     intent_acc = 0.8693467336683417███████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:05<00:00,  1.06s/it] 
09/20/2025 21:08:44 - INFO - trainer -     loss = 0.7030707150697708
09/20/2025 21:08:44 - INFO - trainer -     sementic_frame_acc = 0.7185929648241206
09/20/2025 21:08:44 - INFO - trainer -     slot_f1 = 0.8406593406593408
09/20/2025 21:08:44 - INFO - trainer -     slot_precision = 0.864406779661017
09/20/2025 21:08:44 - INFO - trainer -     slot_recall = 0.8181818181818182
09/20/2025 21:08:44 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [05:59<00:00,  3.07s/it]
09/20/2025 21:08:55 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [05:59<00:00,  2.94s/it] 
09/20/2025 21:08:55 - INFO - trainer -     Num examples = 199
09/20/2025 21:08:55 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.12s/it]
09/20/2025 21:08:59 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.07it/s] 
09/20/2025 21:08:59 - INFO - trainer -     intent_acc = 0.8693467336683417
09/20/2025 21:08:59 - INFO - trainer -     loss = 0.7187643796205521
09/20/2025 21:08:59 - INFO - trainer -     sementic_frame_acc = 0.7185929648241206
09/20/2025 21:08:59 - INFO - trainer -     slot_f1 = 0.839572192513369
09/20/2025 21:08:59 - INFO - trainer -     slot_precision = 0.839572192513369
09/20/2025 21:08:59 - INFO - trainer -     slot_recall = 0.839572192513369
09/20/2025 21:08:59 - INFO - trainer -   No improvement for 5 epochs
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [05:48<00:00,  2.98s/it] 
09/20/2025 21:14:48 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [05:48<00:00,  2.60s/it] 
09/20/2025 21:14:48 - INFO - trainer -     Num examples = 199
09/20/2025 21:14:48 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.23s/it]
09/20/2025 21:14:53 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.03s/it] 
09/20/2025 21:14:53 - INFO - trainer -     intent_acc = 0.8944723618090452
09/20/2025 21:14:53 - INFO - trainer -     loss = 0.7649261653423309
09/20/2025 21:14:53 - INFO - trainer -     sementic_frame_acc = 0.7135678391959799
09/20/2025 21:14:53 - INFO - trainer -     slot_f1 = 0.8268156424581006
09/20/2025 21:14:53 - INFO - trainer -     slot_precision = 0.8654970760233918
09/20/2025 21:14:53 - INFO - trainer -     slot_recall = 0.7914438502673797
09/20/2025 21:14:53 - INFO - trainer -   No improvement for 6 epochs
Epoch:  26%|███████████████████████████████████████                                                                                                               | 13/50 [1:29:13<3:52:01, 376.26s/it]09/20/2025 21:19:01 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████                                                  | 78/117 [04:04<02:04,  3.19s/it] 
09/20/2025 21:19:01 - INFO - trainer -     Num examples = 199
09/20/2025 21:19:01 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.22s/it]
09/20/2025 21:19:06 - INFO - trainer -   ***** Eval results *****
09/20/2025 21:19:06 - INFO - trainer -     intent_acc = 0.8894472361809045███████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.02s/it] 
09/20/2025 21:19:06 - INFO - trainer -     loss = 0.7758820056915283
09/20/2025 21:19:06 - INFO - trainer -     sementic_frame_acc = 0.6984924623115578
09/20/2025 21:19:06 - INFO - trainer -     slot_f1 = 0.8162162162162163
09/20/2025 21:19:06 - INFO - trainer -     slot_precision = 0.825136612021858
09/20/2025 21:19:06 - INFO - trainer -     slot_recall = 0.8074866310160428
09/20/2025 21:19:06 - INFO - trainer -   Saving model checkpoint to massive_model_bert_new
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [06:08<00:00,  3.15s/it]
09/20/2025 21:21:02 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [06:08<00:00,  2.57s/it] 
09/20/2025 21:21:02 - INFO - trainer -     Num examples = 199
09/20/2025 21:21:02 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.22s/it]
09/20/2025 21:21:07 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.01s/it] 
09/20/2025 21:21:07 - INFO - trainer -     intent_acc = 0.8844221105527639
09/20/2025 21:21:07 - INFO - trainer -     loss = 0.7883064150810242
09/20/2025 21:21:07 - INFO - trainer -     sementic_frame_acc = 0.7035175879396985
09/20/2025 21:21:07 - INFO - trainer -     slot_f1 = 0.821917808219178
09/20/2025 21:21:07 - INFO - trainer -     slot_precision = 0.8426966292134831
09/20/2025 21:21:07 - INFO - trainer -     slot_recall = 0.8021390374331551
09/20/2025 21:21:07 - INFO - trainer -   No improvement for 7 epochs
Iteration: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [06:00<00:00,  3.08s/it] 
09/20/2025 21:27:08 - INFO - trainer -   ***** Running evaluation on dev dataset *****███████████████████████████████████████████████████████████████████████████████| 117/117 [06:00<00:00,  2.55s/it] 
09/20/2025 21:27:08 - INFO - trainer -     Num examples = 199
09/20/2025 21:27:08 - INFO - trainer -     Batch size = 64
Evaluating: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.22s/it]
09/20/2025 21:27:12 - INFO - trainer -   ***** Eval results *****████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.02s/it] 
09/20/2025 21:27:12 - INFO - trainer -     intent_acc = 0.864321608040201
09/20/2025 21:27:12 - INFO - trainer -     loss = 0.7378927171230316
09/20/2025 21:27:12 - INFO - trainer -     sementic_frame_acc = 0.7085427135678392
09/20/2025 21:27:12 - INFO - trainer -     slot_f1 = 0.8409703504043127
09/20/2025 21:27:12 - INFO - trainer -     slot_precision = 0.8478260869565217
09/20/2025 21:27:12 - INFO - trainer -     slot_recall = 0.8342245989304813
09/20/2025 21:27:12 - INFO - trainer -   No improvement for 8 epochs
09/20/2025 21:27:12 - INFO - trainer -   Early stopping after 15 epochs
Epoch:  28%|██████████████████████████████████████████                                                                                                            | 14/50 [1:41:32<4:21:06, 435.19s/it] 
09/20/2025 21:27:13 - INFO - trainer -   ***** Model Loaded *****
09/20/2025 21:27:13 - INFO - trainer -   ***** Running evaluation on test dataset *****
09/20/2025 21:27:13 - INFO - trainer -     Num examples = 1094
09/20/2025 21:27:13 - INFO - trainer -     Batch size = 64
Evaluating: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 18/18 [00:27<00:00,  1.50s/it] 
09/20/2025 21:27:40 - INFO - trainer -   ***** Eval results *****
09/20/2025 21:27:40 - INFO - trainer -     intent_acc = 0.9149908592321755
09/20/2025 21:27:40 - INFO - trainer -     loss = 0.6299010862906774
09/20/2025 21:27:40 - INFO - trainer -     sementic_frame_acc = 0.716636197440585
09/20/2025 21:27:40 - INFO - trainer -     slot_f1 = 0.7957824639289678
09/20/2025 21:27:40 - INFO - trainer -     slot_precision = 0.7861842105263158
09/20/2025 21:27:40 - INFO - trainer -     slot_recall = 0.8056179775280898
