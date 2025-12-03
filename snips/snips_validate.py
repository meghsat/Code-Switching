seq_in_file = "data/snips/test/seq.in"
seq_out_file = "data/snips/test/seq.out"

mismatches = []

with open(seq_in_file, "r", encoding="utf-8") as f_in, \
     open(seq_out_file, "r", encoding="utf-8") as f_out:

    seq_in_lines = [line.strip() for line in f_in.readlines()]
    seq_out_lines = [line.strip() for line in f_out.readlines()]

# Ensure same number of lines
total_lines = min(len(seq_in_lines), len(seq_out_lines))

for idx in range(total_lines):
    tokens_in = seq_in_lines[idx].split()
    tokens_out = seq_out_lines[idx].split()

    if len(tokens_in) != len(tokens_out):
        mismatches.append(
            (idx + 1, len(tokens_in), len(tokens_out), seq_in_lines[idx], seq_out_lines[idx])
        )

# ----- Results -----

print(f"Total lines checked: {total_lines}")
print(f"Total mismatches: {len(mismatches)}\n")

if mismatches:
    print("MISMATCH DETAILS:\n")
    for line_no, in_count, out_count, sin, sout in mismatches[:50]:  # show first 50 only
        print(f"Line {line_no}: seq.in={in_count} tokens, seq.out={out_count} tokens")
        print(f"  IN : {sin}")
        print(f"  OUT: {sout}")
        print()
else:
    print("All lines match correctly! 🎉")
