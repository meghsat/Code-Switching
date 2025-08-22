# Read intent labels from 'label' file and extract unique words
input_file = "data/Hinglish Dataset/train/label"
output_file = "data/Hinglish Datasetintent_label.txt"

unique_words = set()

# Read input file line by line
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        # Strip newline and split into words
        words = line.strip().split()
        unique_words.update(words)

# Write unique words to output file, one per line
with open(output_file, "w", encoding="utf-8") as f:
    for word in sorted(unique_words):
        f.write(word + "\n")

print(f"Unique words written to {output_file}")
