from collections import Counter

# Read file
with open("intents_all.txt", "r") as f:
    words = [line.strip() for line in f if line.strip()]

# Count each word
counts = Counter(words)

# Sort by descending count
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

# Print result
for word, count in sorted_counts:
    print(word, count)
