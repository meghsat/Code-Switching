# unique_words.py

# Input and output file paths
input_file = "intents_all.txt"
output_file = "unique_words.txt"

# Read the file and extract unique words
with open(input_file, "r", encoding="utf-8") as f:
    words = {line.strip() for line in f if line.strip()}  # remove duplicates & blank lines

# Sort them (optional)
unique_words = sorted(words)

# Write back to a new file
with open(output_file, "w", encoding="utf-8") as f:
    for word in unique_words:
        f.write(word + "\n")

print(f"Extracted {len(unique_words)} unique words to '{output_file}'")
