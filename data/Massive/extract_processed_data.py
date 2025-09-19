import pandas as pd

# Load the processed Excel file
df = pd.read_excel('Processed_Massive.xlsx')

# Extract the specified columns and save to text files
with open('output.txt', 'w', encoding='utf-8') as f:
    for label in df['labels']:
        f.write(f"{label}\n")

with open('input.txt', 'w', encoding='utf-8') as f:
    for query in df['modified_query']:
        f.write(f"{query}\n")

with open('labels.txt', 'w', encoding='utf-8') as f:
    for intent in df['intent']:
        f.write(f"{intent}\n")
