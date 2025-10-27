import re

def parse_slots(tagged_line):
    # Extract slot-value pairs
    slots = re.findall(r"\[SL:(\w+)\s+([^\]]+)\]", tagged_line)
    return {value: slot for slot, value in slots}

def convert_to_bio(input_line, slot_map):
    tokens = input_line.strip().split()
    labels = []
    for token in tokens:
        if token in slot_map:
            labels.append(f"B-{slot_map[token]}")
        else:
            labels.append("O")
    return tokens, labels

with open("data/massive/input.txt", "r", encoding="utf-8") as f_in, \
     open("data/massive/output_processed.txt", "r", encoding="utf-8") as f_out, \
     open("bio.txt", "w", encoding="utf-8") as f_bio:

    for input_line, output_line in zip(f_in, f_out):
        slot_map = parse_slots(output_line)
        tokens, labels = convert_to_bio(input_line, slot_map)
        f_bio.write(" ".join(labels) + "\n")
