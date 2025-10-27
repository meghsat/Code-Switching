import pandas as pd
import re

# Load Excel file
df = pd.read_excel("data/MASSIVE.xlsx")  # change filename here

output_lines = []
input_lines = []
labels = []

for row in df["cs_parse"]:
    sentence = row.strip()
    output_lines.append(sentence)  # direct dump for output.txt

    # --- Extract intent ---
    intent_match = re.match(r"\[IN:([^\s]+)", sentence)
    if intent_match:
        intent = intent_match.group(1).strip()
        labels.append(intent)
    else:
        intent = ""
        labels.append("")

    # --- Remove outer [IN:...] and trailing bracket ---
    cleaned = re.sub(r"^\[IN:[^\s]+\s*", "", sentence)  # remove leading [IN:intent
    cleaned = cleaned.rstrip(" ]")  # remove trailing ]

    # --- Replace slot phrases [SL:SLOT_NAME ... ] ---
    def slot_replacer(match):
        slot_text = match.group(1).strip().split()
        return "_".join(slot_text)

    cleaned = re.sub(r"\[SL:[^\s]+\s+([^\]]+)\]", slot_replacer, cleaned)

    input_lines.append(cleaned.strip())

# --- Write to files ---
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

with open("input.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(input_lines))

with open("labels.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(labels))
