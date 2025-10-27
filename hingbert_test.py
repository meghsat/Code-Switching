import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn.utils.multiclass import unique_labels
import torch.nn.functional as F
import os

# === Paths ===
model_dir = "hingmbert_massive"
test_seq_path = "data/atis/test/seq.in"
test_label_path = "data/atis/test/label"

# === Load test data ===
def load_file_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

test_texts = load_file_lines(test_seq_path)
true_labels = load_file_lines(test_label_path)

# === Load label mapping ===
label2id = {}
id2label = {}
with open(os.path.join(model_dir, "label_map.txt"), "r", encoding="utf-8") as f:
    for i, line in enumerate(f,1):
        try:
            idx, label = line.strip().split("\t")
            label2id[label] = int(idx)
            id2label[int(idx)] = label
        except ValueError as e:
            print(f"Error on line {i}: '{line.strip()}'")
            raise

# === Load tokenizer and model ===
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir)
model.eval()

# === Inference and Evaluation ===
true_ids = []
pred_ids_filtered = []
losses = []
ignored_count = 0

loss_fn = torch.nn.CrossEntropyLoss()

for text, true_label in zip(test_texts, true_labels):
    if true_label not in label2id:
        ignored_count += 1
        continue  # skip unknown or untrained label

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        pred_id = torch.argmax(logits, dim=1).item()

        target = torch.tensor([label2id[true_label]])
        loss = loss_fn(logits, target)
        losses.append(loss.item())

        true_ids.append(label2id[true_label])
        pred_ids_filtered.append(pred_id)

# === Metrics ===
precision = precision_score(true_ids, pred_ids_filtered, average='weighted', zero_division=0)
recall = recall_score(true_ids, pred_ids_filtered, average='weighted', zero_division=0)
f1 = f1_score(true_ids, pred_ids_filtered, average='weighted', zero_division=0)
accuracy = accuracy_score(true_ids, pred_ids_filtered)
avg_loss = sum(losses) / len(losses) if losses else 0.0

# === Get only used labels for report ===
used_labels = sorted(set(true_ids + pred_ids_filtered))
used_target_names = [id2label[lid] for lid in used_labels]

# === Print Evaluation ===
print("\n🧪 Classification Report:")
print(classification_report(
    true_ids,
    pred_ids_filtered,
    labels=used_labels,
    target_names=used_target_names,
    zero_division=0
))

print(f"\n✅ Accuracy: {accuracy:.4f}")
print(f"📊 Precision: {precision:.4f}")
print(f"📈 Recall:    {recall:.4f}")
print(f"🎯 F1 Score:  {f1:.4f}")
print(f"📉 Avg. Loss: {avg_loss:.4f}")
print(f"⚠️ Ignored {ignored_count} samples with unseen labels.")

# === Optional: Save predictions ===
with open("test_predictions.txt", "w", encoding="utf-8") as f:
    for text, pred_id in zip(test_texts, pred_ids_filtered):
        f.write(f"{text}\t{id2label[pred_id]}\n")
