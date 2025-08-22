input_file = "data/atis/test/seq.out"
output_file = "data/atis/test/seq.out"

# Read the file
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Replace all tokens with 'O'
processed_lines = []
for line in lines:
    tokens = line.strip().split()
    processed_lines.append(" ".join("O" for _ in tokens))

# Write to the output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(processed_lines))

print(f"Processed file saved to {output_file}")
