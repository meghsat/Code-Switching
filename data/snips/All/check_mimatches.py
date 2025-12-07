# File paths
file1_path = "final_predictions_slots.txt"
file2_path = "true_slots.txt"

# Read the files
with open(file1_path, "r", encoding="utf-8") as f1:
    lines1 = f1.read().splitlines()

with open(file2_path, "r", encoding="utf-8") as f2:
    lines2 = f2.read().splitlines()

# Compare line by line and print mismatches
for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
    if line1 != line2:
        print(f"Line {i} mismatch:")
        print(f"  File1: {line1}")
        print(f"  File2: {line2}")
        print()
