import json
import random

# Input files
slots_file = "slots_all.txt"
sentences_file = "input_sentences_all.txt"
output_json = "slots_words.json"

# Initialize dictionary
slot_dict = {}

# Read both files line by line
with open(slots_file, "r", encoding="utf-8") as f_slots, open(sentences_file, "r", encoding="utf-8") as f_sents:
    for slot_line, sent_line in zip(f_slots, f_sents):
        slot_tags = slot_line.strip().split()
        words = sent_line.strip().split()

        if len(slot_tags) != len(words):
            print("⚠️ Mismatch in line length, skipping line.")
            continue

        for tag, word in zip(slot_tags, words):
            if tag != "O":
                slot_dict.setdefault(tag, set()).add(word)

# Convert sets to lists for JSON and sampling
slot_dict = {k: sorted(list(v)) for k, v in slot_dict.items()}

# Save to JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(slot_dict, f, ensure_ascii=False, indent=4)

print(f"\n✅ Extracted {len(slot_dict)} slot categories → saved to '{output_json}'\n")

# Print unique keys and random 5 samples per key
for key, values in slot_dict.items():
    samples = random.sample(values, min(5, len(values)))
    print(f"{key}: {samples}")
