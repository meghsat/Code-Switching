input_file = "data/Hinglish Dataset/train/seq.out"
output_file = "data/Hinglish Dataset/slot_label.txt"

slot_labels = set()

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        tokens = line.strip().split()
        for token in tokens:
            if token.startswith("B-"):
                slot_labels.add(token)

# Write sorted unique slot labels to the output file
with open(output_file, "w", encoding="utf-8") as f:
    for label in sorted(slot_labels):
        f.write(label + "\n")

print(f"Slot labels written to {output_file}")
