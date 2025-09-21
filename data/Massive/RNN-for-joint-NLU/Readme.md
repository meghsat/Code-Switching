**train folder: input/ 100 to 300, 500 to 1300, 1500 to 2400, 2900 to 3900, 4000 to 4300, 4800 to 5017, 2700 to 2800, 4500 to 4600, 2600 to 2699 <br>
test folder: input/ 301 to 499, 1301 to 1499, 2401 to 2500, 4301 to 4400, 4601 to 4799, 3901 to 3999, 2801–2899, 4401–4499, 2501 to 2599 <br>

**Logs:** 

(base) PS C:\Users\SDEVINEN\Downloads\projects\pers\RNN-for-Joint-NLU-master\RNN-for-Joint-NLU-master> python train.py
processed_data_path : C:\Users\SDEVINEN\Downloads\projects\pers\RNN-for-Joint-NLU-master\RNN-for-Joint-NLU-master\data/
Successfully load data. # of set : 3823 
# of vocab : 2584, # of slot_tag : 46, # of intent_tag : 81
Preprocessing complete!
Successfully loaded test data. # of examples: 1194
Starting training...
Step 0, epoch 0: 8.2470
Step 0, epoch 100: 4.2006
Epoch 0 Evaluation Results:
  Loss: 3.0682
  Intent Accuracy: 0.2584
  Slot F1: 0.8397
  Slot Precision: 0.7940
  Slot Recall: 0.8911
  *** New best model! (intent accuracy: 0.2584) ***
--------------------------------------------------
Step 1, epoch 0: 2.8804
Step 1, epoch 100: 2.6931
Epoch 1 Evaluation Results:
  Loss: 2.0750
  Intent Accuracy: 0.5498
  Slot F1: 0.8394
  Slot Precision: 0.7936
  Slot Recall: 0.8908
  *** New best model! (intent accuracy: 0.5498) ***
--------------------------------------------------
Step 2, epoch 0: 1.9213
Step 2, epoch 100: 1.8872
Epoch 2 Evaluation Results:
  Loss: 1.6488
  Intent Accuracy: 0.6976
  Slot F1: 0.8393
  Slot Precision: 0.7934
  Slot Recall: 0.8907
  *** New best model! (intent accuracy: 0.6976) ***
--------------------------------------------------
Step 3, epoch 0: 1.2331
Step 3, epoch 100: 1.3554
Epoch 3 Evaluation Results:
  Loss: 1.3695
  Intent Accuracy: 0.7686
  Slot F1: 0.8384
  Slot Precision: 0.7924
  Slot Recall: 0.8900
  *** New best model! (intent accuracy: 0.7686) ***
--------------------------------------------------
Step 4, epoch 0: 1.3345
Step 4, epoch 100: 1.0353
Epoch 4 Evaluation Results:
  Loss: 1.2413
  Intent Accuracy: 0.8032
  Slot F1: 0.8409
  Slot Precision: 0.8045
  Slot Recall: 0.8910
  *** New best model! (intent accuracy: 0.8032) ***
--------------------------------------------------
Step 5, epoch 0: 0.5966
Step 5, epoch 100: 0.8435
Epoch 5 Evaluation Results:
  Loss: 1.1890
  Intent Accuracy: 0.8125
  Slot F1: 0.8397
  Slot Precision: 0.7972
  Slot Recall: 0.8907
  *** New best model! (intent accuracy: 0.8125) ***
--------------------------------------------------
Step 6, epoch 0: 0.5682
Step 6, epoch 100: 0.6982
Epoch 6 Evaluation Results:
  Loss: 1.1750
  Intent Accuracy: 0.8345
  Slot F1: 0.8513
  Slot Precision: 0.8320
  Slot Recall: 0.8903
  *** New best model! (intent accuracy: 0.8345) ***
--------------------------------------------------
Step 7, epoch 0: 0.6052
Step 7, epoch 100: 0.6482
Epoch 7 Evaluation Results:
  Loss: 1.1472
  Intent Accuracy: 0.8361
  Slot F1: 0.8510
  Slot Precision: 0.8367
  Slot Recall: 0.8928
  *** New best model! (intent accuracy: 0.8361) ***
--------------------------------------------------
Step 8, epoch 0: 0.4541
Step 8, epoch 100: 0.5253
Epoch 8 Evaluation Results:
  Loss: 1.1353
  Intent Accuracy: 0.8378
  Slot F1: 0.8594
  Slot Precision: 0.8611
  Slot Recall: 0.8982
  *** New best model! (intent accuracy: 0.8378) ***
--------------------------------------------------
Step 9, epoch 0: 0.4412
Step 9, epoch 100: 0.4071
Epoch 9 Evaluation Results:
  Loss: 1.0509
  Intent Accuracy: 0.8530
  Slot F1: 0.9067
  Slot Precision: 0.9026
  Slot Recall: 0.9191
  *** New best model! (intent accuracy: 0.8530) ***
--------------------------------------------------
Step 10, epoch 0: 0.3427
Step 10, epoch 100: 0.2913
Epoch 10 Evaluation Results:
  Loss: 1.0891
  Intent Accuracy: 0.8353
  Slot F1: 0.9133
  Slot Precision: 0.9112
  Slot Recall: 0.9224
  No improvement in intent accuracy. Patience: 1/10
--------------------------------------------------
Step 11, epoch 0: 0.3010
Step 11, epoch 100: 0.2477
Epoch 11 Evaluation Results:
  Loss: 1.1017
  Intent Accuracy: 0.8522
  Slot F1: 0.9231
  Slot Precision: 0.9228
  Slot Recall: 0.9289
  No improvement in intent accuracy. Patience: 2/10
--------------------------------------------------
Step 12, epoch 0: 0.1930
Step 12, epoch 100: 0.1979
Epoch 12 Evaluation Results:
  Loss: 1.1237
  Intent Accuracy: 0.8471
  Slot F1: 0.9214
  Slot Precision: 0.9190
  Slot Recall: 0.9269
  No improvement in intent accuracy. Patience: 3/10
--------------------------------------------------
Step 13, epoch 0: 0.1561
Step 13, epoch 100: 0.1698
Epoch 13 Evaluation Results:
  Loss: 1.1054
  Intent Accuracy: 0.8522
  Slot F1: 0.9273
  Slot Precision: 0.9280
  Slot Recall: 0.9308
  No improvement in intent accuracy. Patience: 4/10
--------------------------------------------------
Step 14, epoch 0: 0.1002
Step 14, epoch 100: 0.1429
Epoch 14 Evaluation Results:
  Loss: 1.0910
  Intent Accuracy: 0.8573
  Slot F1: 0.9270
  Slot Precision: 0.9275
  Slot Recall: 0.9324
  *** New best model! (intent accuracy: 0.8573) ***
--------------------------------------------------
Step 15, epoch 0: 0.1012
Step 15, epoch 100: 0.1180
Epoch 15 Evaluation Results:
  Loss: 1.1466
  Intent Accuracy: 0.8480
  Slot F1: 0.9292
  Slot Precision: 0.9310
  Slot Recall: 0.9335
  No improvement in intent accuracy. Patience: 1/10
--------------------------------------------------
Step 16, epoch 0: 0.0776
Step 16, epoch 100: 0.0972
Epoch 16 Evaluation Results:
  Loss: 1.1425
  Intent Accuracy: 0.8530
  Slot F1: 0.9285
  Slot Precision: 0.9319
  Slot Recall: 0.9303
  No improvement in intent accuracy. Patience: 2/10
--------------------------------------------------
Step 17, epoch 0: 0.0314
Step 17, epoch 100: 0.0813
Epoch 17 Evaluation Results:
  Loss: 1.1332
  Intent Accuracy: 0.8556
  Slot F1: 0.9285
  Slot Precision: 0.9277
  Slot Recall: 0.9341
  No improvement in intent accuracy. Patience: 3/10
--------------------------------------------------
Step 18, epoch 0: 0.0391
Step 18, epoch 100: 0.0694
Epoch 18 Evaluation Results:
  Loss: 1.1743
  Intent Accuracy: 0.8547
  Slot F1: 0.9299
  Slot Precision: 0.9326
  Slot Recall: 0.9325
  No improvement in intent accuracy. Patience: 4/10
--------------------------------------------------
Step 19, epoch 0: 0.0280
Step 19, epoch 100: 0.0617
Epoch 19 Evaluation Results:
  Loss: 1.2143
  Intent Accuracy: 0.8556
  Slot F1: 0.9293
  Slot Precision: 0.9292
  Slot Recall: 0.9329
  No improvement in intent accuracy. Patience: 5/10
--------------------------------------------------
Step 20, epoch 0: 0.0146
Step 20, epoch 100: 0.0487
Epoch 20 Evaluation Results:
  Loss: 1.2013
  Intent Accuracy: 0.8539
  Slot F1: 0.9322
  Slot Precision: 0.9323
  Slot Recall: 0.9349
  No improvement in intent accuracy. Patience: 6/10
--------------------------------------------------
Step 21, epoch 0: 0.0375
Step 21, epoch 100: 0.0435
Epoch 21 Evaluation Results:
  Loss: 1.2652
  Intent Accuracy: 0.8573
  Slot F1: 0.9317
  Slot Precision: 0.9299
  Slot Recall: 0.9362
  No improvement in intent accuracy. Patience: 7/10
--------------------------------------------------
Step 22, epoch 0: 0.0101
Step 22, epoch 100: 0.0566
Epoch 22 Evaluation Results:
  Loss: 1.2341
  Intent Accuracy: 0.8556
  Slot F1: 0.9290
  Slot Precision: 0.9284
  Slot Recall: 0.9325
  No improvement in intent accuracy. Patience: 8/10
Step 23, epoch 0: 0.0253
Step 23, epoch 100: 0.0585
Epoch 23 Evaluation Results:
  Loss: 1.1927
  Intent Accuracy: 0.8556
  Slot F1: 0.9294
  Slot Precision: 0.9304
  Slot Recall: 0.9343
  No improvement in intent accuracy. Patience: 9/10
--------------------------------------------------
Step 24, epoch 0: 0.0235
Step 24, epoch 100: 0.0516
Epoch 24 Evaluation Results:
  Loss: 1.2986
  Intent Accuracy: 0.8311
  Slot F1: 0.9289
  Slot Precision: 0.9299
  Slot Recall: 0.9312
  No improvement in intent accuracy. Patience: 10/10
Early stopping triggered after 25 epochs!
Best eval loss: 0.8573
Restored best model weights.
Saved best model with eval loss: 0.8573
Train Complete!
