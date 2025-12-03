import re
import pandas as pd

input_xlsx = "data/snips/snips_test.xlsx"
seq_in_file = "seq.in"
seq_out_file = "seq.out"
label_file = "label"     # new domain file


def process_cs_parse(parse_str):
    if not isinstance(parse_str, str):
        return "", ""

    # Remove `[IN:<intent>`
    parse_str = re.sub(r"\[IN:[^\s]+\s*", "", parse_str).strip()

    # Remove trailing "]"
    if parse_str.endswith("]"):
        parse_str = parse_str[:-1].strip()

    tokens_in = []
    labels = []

    i = 0
    n = len(parse_str)

    while i < n:
        if parse_str[i] == "[":
            end = parse_str.find("]", i)
            if end == -1:
                break

            inner = parse_str[i+1:end].strip()
            parts = inner.split()

            if len(parts) >= 2 and parts[0].startswith("SL:"):
                slot_name = parts[0].replace("SL:", "")
                slot_words = parts[1:]

                merged = "_".join(slot_words)
                tokens_in.append(merged)
                labels.append(f"B-{slot_name}")
            else:
                # malformed → skip
                pass

            i = end + 1

        else:
            j = parse_str.find("[", i)
            if j == -1:
                j = n

            text = parse_str[i:j].strip()

            if text:
                for w in text.split():
                    tokens_in.append(w)
                    labels.append("O")

            i = j

    return " ".join(tokens_in), " ".join(labels)


# -------- MAIN PROCESS ---------

df = pd.read_excel(input_xlsx)

with open(seq_in_file, "w", encoding="utf-8") as f_in, \
     open(seq_out_file, "w", encoding="utf-8") as f_out, \
     open(label_file, "w", encoding="utf-8") as f_label:

    for _, row in df.iterrows():

        cs_parse = str(row["cs_parse"]).strip()
        domain = str(row["domain"]).strip()

        # Process parse
        seq_in_processed, seq_out_processed = process_cs_parse(cs_parse)

        # Write outputs
        f_in.write(seq_in_processed + "\n")
        f_out.write(seq_out_processed + "\n")
        f_label.write(domain + "\n")
