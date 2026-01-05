import re
input_file = "predictions.txt"   # your input file name
intent_file = "intents.txt"                    # output file for intents
slots_file = "slots.txt"                       # output file for slot sequences

def process_block(block_lines):
    """Return (intent, [slot_tags]) from one example block"""
    intent = None
    slot_tags = []

    for line in block_lines:
        line = line.strip()

        # extract intent
        if line.startswith("intent="):
            intent = line.replace("intent=", "").strip().strip(";")
            continue

        # split on semicolon OR whitespace
        tokens = re.split(r"[;\s]+", line)

        for tok in tokens:
            if "=" in tok:
                key, tag = tok.rsplit("=", 1)
                # skip accidental intent tokens
                if key == "intent":
                    continue
                slot_tags.append(tag)

    return intent, slot_tags

with open(input_file, "r", encoding="utf-8") as f:
    raw_lines = [ln.rstrip("\n") for ln in f]

# Build example blocks: start a new block whenever we see a line that begins with "intent="
blocks = []
current = []
for ln in raw_lines:
    if not ln.strip():
        # blank line ends a block
        if current:
            blocks.append(current)
            current = []
        continue

    if ln.lstrip().startswith("intent="):
        # if we already have a current block, treat this as start of a new example
        if current:
            blocks.append(current)
            current = []
        current.append(ln.strip())
    else:
        # continuation line for current example
        current.append(ln.strip())

# append last block
if current:
    blocks.append(current)

with open(intent_file, "w", encoding="utf-8") as f_intent, \
     open(slots_file, "w", encoding="utf-8") as f_slots:

    for block in blocks:
        intent, slot_tags = process_block(block)
        # write even when slot_tags empty? usually you want a line per example regardless.
        if intent is None:
            # skip malformed block
            continue
        f_intent.write(intent + "\n")
        # if there are no tags, write an empty line so counts align
        f_slots.write(" ".join(slot_tags) + "\n")

print("✅ Files created: intents.txt and slots.txt")
