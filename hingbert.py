import torch
from torch.utils.data import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.metrics import classification_report, accuracy_score
import os

# Load data from file
def load_file_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

# Custom Dataset class
class IntentDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, label2id):
        self.encodings = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        self.labels = [label2id[label.strip()] for label in labels]

    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# Load data
train_texts = load_file_lines("data/atis/train/seq.in")
train_labels = load_file_lines("data/atis/train/label")

val_texts = load_file_lines("data/atis/dev/seq.in")
val_labels = load_file_lines("data/atis/dev/label")

# Build label maps
# unique_labels = sorted(set(train_labels))
# label2id = {label: idx for idx, label in enumerate(unique_labels)}
# id2label = {idx: label for label, idx in label2id.items()}
# num_labels = len(label2id)
unique_labels = sorted(set(train_labels + val_labels))  # Combine train and val labels
label2id = {label: idx for idx, label in enumerate(unique_labels)}
id2label = {idx: label for label, idx in label2id.items()}
num_labels = len(label2id)

# Load model and tokenizer
model_name = "l3cube-pune/hing-bert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

# Datasets
train_dataset = IntentDataset(train_texts, train_labels, tokenizer, label2id)
val_dataset = IntentDataset(val_texts, val_labels, tokenizer, label2id)

# Evaluation metrics
def compute_metrics(p):
    preds = torch.argmax(torch.tensor(p.predictions), dim=1)
    labels = torch.tensor(p.label_ids)
    acc = accuracy_score(labels, preds)
    report = classification_report(labels, preds, output_dict=True, zero_division=0)
    return {
        "accuracy": acc,
        "precision": report["weighted avg"]["precision"],
        "recall": report["weighted avg"]["recall"],
        "f1": report["weighted avg"]["f1-score"]
    }

# Training setup
training_args = TrainingArguments(
    output_dir="./results_massive_hingbert",
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=50,
    weight_decay=0.01,
    load_best_model_at_end=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics,
)

# Train the model
trainer.train()

# Save model & label map
model.save_pretrained("hingbert_massive")
tokenizer.save_pretrained("hingbert_massive")

# Save label map for inference
with open("hingbert_massive/label_map.txt", "w") as f:
    for label, idx in label2id.items():
        f.write(f"{idx}\t{label}\n")
