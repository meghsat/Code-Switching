import csv
from collections import Counter

SEQ_OUT_FILE = "slots_all.txt"

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


with open("slots_count.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["slot", "count"])
    for slot, count in slot_counts.items():
        writer.writerow([slot, count])

