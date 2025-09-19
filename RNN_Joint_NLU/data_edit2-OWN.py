import re
import pandas as pd

# Load Excel
df = pd.read_excel("test.xlsx")

def parse_cs_parse(cs_parse):
    """
    Transforms a cs_parse string into two lists:
    - input_tokens: words with underscores for slot spans
    - output_labels: slot labels (B-XXX) or 'O'
    """

    # Stack to manage nested brackets
    stack = []
    input_tokens = []
    output_labels = []

    # Tokenize keeping brackets and words
    tokens = re.findall(r'\[|\]|[^\[\]\s]+', cs_parse)

    current_slot = None
    current_words = []

    def flush_words():
        """Flush current_words to input_tokens and output_labels"""
        if not current_words:
            return
        token = '_'.join(current_words)
        input_tokens.append(token)
        label = f'B-{current_slot}' if current_slot else 'O'
        output_labels.append(label)
        current_words.clear()

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == '[':
            # Check if this is a slot or intent
            if i + 1 < len(tokens):
                next_token = tokens[i + 1]
                if next_token.startswith("SL:"):
                    stack.append(('SL', current_slot))
                    current_slot = next_token[3:]
                    i += 1  # skip "SL:xxx"
                elif next_token.startswith("IN:"):
                    stack.append(('IN', current_slot))
                    current_slot = None  # skip intent slotting
                    i += 1
        elif token == ']':
            flush_words()
            if stack:
                kind, prev_slot = stack.pop()
                current_slot = prev_slot
        else:
            if current_slot:
                current_words.append(token)
            else:
                flush_words()
                input_tokens.append(token)
                output_labels.append('O')
        i += 1

    flush_words()
    return input_tokens, output_labels


# Prepare outputs
input_lines = []
output_lines = []

for idx, row in df.iterrows():
    cs_parse = row['cs_parse']
    input_tokens, output_labels = parse_cs_parse(cs_parse)
    input_lines.append(" ".join(input_tokens))
    output_lines.append(" ".join(output_labels))

# Write files
with open("input.txt", "w", encoding="utf-8") as f_in:
    f_in.write("\n".join(input_lines))

with open("output.txt", "w", encoding="utf-8") as f_out:
    f_out.write("\n".join(output_lines))
