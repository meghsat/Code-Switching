import csv
from collections import Counter

# ---- FILE PATHS ----
LABEL_FILE = "data/Massive/Base/Main_Dataset/train/label"
SEQ_OUT_FILE = "data/Massive/Base/Main_Dataset/train/seq.out"

# ---- READ LABELS ----
with open(LABEL_FILE, "r", encoding="utf-8") as f:
    labels = [line.strip() for line in f if line.strip()]

label_counts = Counter(labels)

# ---- READ SEQ.OUT & EXTRACT SLOT TYPES ----
slot_counts = Counter()

with open(SEQ_OUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        for tag in parts:
            # Skip O
            if tag == "O":
                continue
            # Extract after B- or I-
            if "-" in tag:
                prefix, slot = tag.split("-", 1)
                slot_counts[slot] += 1

# ---- WRITE LABEL COUNTS CSV ----
with open("labels_count.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["label", "count"])
    for label, count in label_counts.items():
        writer.writerow([label, count])

# ---- WRITE SLOT COUNTS CSV ----
with open("slots_count.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["slot", "count"])
    for slot, count in slot_counts.items():
        writer.writerow([slot, count])

print("CSV files created: labels_count.csv, slots_count.csv")
