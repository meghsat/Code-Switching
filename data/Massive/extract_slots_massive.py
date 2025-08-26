import re

# Input and output file names
input_file = "output_processed.txt"
output_file = "slot_label.txt"

# Regex to match [SL:SLOT_NAME ...]
slot_pattern = re.compile(r"\[SL:([A-Za-z_]+)")

slot_names = set()

# Read file and extract slot names
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        matches = slot_pattern.findall(line)
        slot_names.update(matches)

# Write unique slot names with B- prefix
with open(output_file, "w", encoding="utf-8") as f:
    for slot in sorted(slot_names):
        f.write("B-" + slot + "\n")

print(f"Extracted {len(slot_names)} unique slot names into {output_file}")
