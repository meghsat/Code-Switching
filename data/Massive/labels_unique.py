# Input and output file names
input_file = "labels.txt"
output_file = "intent_label.txt"

# Read all lines and remove duplicates
with open(input_file, "r", encoding="utf-8") as f:
    labels = {line.strip() for line in f if line.strip()}

# Write unique labels (sorted for consistency)
with open(output_file, "w", encoding="utf-8") as f:
    for label in sorted(labels):
        f.write(label + "\n")

print(f"Extracted {len(labels)} unique labels into {output_file}")
