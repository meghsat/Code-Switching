import re

def process_slots(text):
    pattern = re.compile(r"\[SL:[A-Z_]+ (.*?)\]")
    
    def replacer(match):
        content = match.group(1)  # slot value
        new_content = content.strip().replace(" ", "_")
        return match.group(0).replace(content, new_content)
    
    return pattern.sub(replacer, text)

# Read input file
with open("output.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Process each line
processed_lines = [process_slots(line.strip()) for line in lines]

# Write back to new file
with open("output_processed.txt", "w", encoding="utf-8") as f:
    for line in processed_lines:
        f.write(line + "\n")

