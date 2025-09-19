import pandas as pd
import re
from typing import List, Tuple

def extract_label_from_parse(cs_parse: str) -> str:
    """Extract the label after IN: from cs_parse string"""
    match = re.search(r'\[IN:([^\s\]]+)', cs_parse)
    return match.group(1) if match else ""

def is_time_token(token: str) -> bool:
    """Check if a token is part of a time expression"""
    # Match patterns like: 9:30, 9 : 30, 9: 30, etc.
    time_patterns = [
        r'^\d+:\d+$',          # 9:30
        r'^\d+\s*:\s*\d+$',    # 9 : 30, 9: 30
        r'^\d+$',              # single digit that might be part of time
        r'^:$',                # colon
    ]
    
    for pattern in time_patterns:
        if re.match(pattern, token, re.IGNORECASE):
            return True
    return False

def group_time_tokens(tokens: List[str]) -> List[Tuple[str, bool]]:
    """Group consecutive time-related tokens together"""
    grouped = []
    i = 0
    
    while i < len(tokens):
        if is_time_token(tokens[i]):
            # Start of a time group
            time_group = [tokens[i]]
            j = i + 1
            
            # Continue collecting time tokens
            while j < len(tokens) and is_time_token(tokens[j]):
                time_group.append(tokens[j])
                j += 1
            
            # Add the entire time group as one token
            grouped.append((' '.join(time_group), True))
            i = j
        else:
            grouped.append((tokens[i], False))
            i += 1
    
    return grouped

def process_cs_parse_to_tags(cs_parse: str) -> str:
    """Convert cs_parse format to BIO tagged format"""
    # Remove outer brackets and IN:LABEL
    content = cs_parse.strip()
    if content.startswith('[') and content.endswith(']'):
        content = content[1:-1]
    
    # Remove IN:LABEL part
    content = re.sub(r'IN:[^\s\]]+\s*', '', content)
    
    # Find all slot labels and their content
    slot_pattern = r'\[SL:([^\s\]]+)\s+([^\]]+)\]'
    slots = re.findall(slot_pattern, content)
    
    # Remove all slot markup to get the clean text
    clean_text = content
    for match in re.finditer(slot_pattern, content):
        clean_text = clean_text.replace(match.group(0), match.group(2))
    
    # Split into tokens
    tokens = clean_text.split()
    
    # Group time-related tokens
    grouped_tokens = group_time_tokens(tokens)
    
    # Create mapping of text to slot labels
    slot_mapping = {}
    for slot_label, slot_text in slots:
        slot_tokens = slot_text.split()
        grouped_slot_tokens = group_time_tokens(slot_tokens)
        
        for token, is_time_group in grouped_slot_tokens:
            slot_mapping[token] = slot_label
    
    # Generate BIO tags
    tags = []
    for token, is_time_group in grouped_tokens:
        if token in slot_mapping:
            slot_label = slot_mapping[token]
            # For the first occurrence of this slot type, use B-
            # For subsequent tokens of the same slot, use I-
            if not tags or not any(tag.endswith(slot_label) for tag in tags[-3:]):
                tags.append(f"B-{slot_label}")
            else:
                tags.append(f"I-{slot_label}")
        else:
            tags.append("O")
    
    return ' '.join(tags)

def process_xlsx_file(file_path: str):
    """Main function to process the XLSX file and create output files"""
    try:
        # Read the XLSX file
        df = pd.read_excel(file_path)
        
        # Check if required columns exist
        if 'cs_query' not in df.columns or 'cs_parse' not in df.columns:
            raise ValueError("Required columns 'cs_query' and 'cs_parse' not found in the file")
        
        # Extract data
        cs_queries = df['cs_query'].dropna().tolist()
        cs_parses = df['cs_parse'].dropna().tolist()
        
        # Ensure both lists have the same length
        min_length = min(len(cs_queries), len(cs_parses))
        cs_queries = cs_queries[:min_length]
        cs_parses = cs_parses[:min_length]
        
        # Process each cs_parse to extract labels and create tagged output
        labels = []
        tagged_outputs = []
        
        for cs_parse in cs_parses:
            # Extract label
            label = extract_label_from_parse(str(cs_parse))
            labels.append(label)
            
            # Convert to tagged format
            tagged_output = process_cs_parse_to_tags(str(cs_parse))
            tagged_outputs.append(tagged_output)
        
        # Write to files
        # Write cs_queries to input.txt
        with open('input.txt', 'w', encoding='utf-8') as f:
            for query in cs_queries:
                f.write(str(query) + '\n')
        
        # Write labels to label.txt
        with open('label.txt', 'w', encoding='utf-8') as f:
            for label in labels:
                f.write(label + '\n')
        
        # Write tagged outputs to output.txt
        with open('output.txt', 'w', encoding='utf-8') as f:
            for tagged_output in tagged_outputs:
                f.write(tagged_output + '\n')
        
        print(f"Successfully processed {len(cs_queries)} sentences")
        print("Files created:")
        print("- input.txt: Contains cs_query sentences")
        print("- label.txt: Contains extracted labels from IN:")
        print("- output.txt: Contains BIO tagged sentences")
        
        # Show a sample of the processing
        if cs_queries:
            print("\nSample processing:")
            print(f"Original query: {cs_queries[0]}")
            print(f"Original parse: {cs_parses[0]}")
            print(f"Extracted label: {labels[0]}")
            print(f"Tagged output: {tagged_outputs[0]}")
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace 'your_file.xlsx' with the actual path to your XLSX file
    file_path = "data/Hinglish Dataset/test/test.xlsx"
    process_xlsx_file(file_path)
    
    # Test with the provided example
    print("\nTesting with provided example:")
    test_cs_parse = "[IN:CREATE_ALARM [SL:DATE_TIME 9 : 30 am ko ] [SL:ALARM_NAME Sunday Brunch ] ke liye ek naya [SL:PERIOD weekly ] reminder add karen ]"
    
    label = extract_label_from_parse(test_cs_parse)
    tagged = process_cs_parse_to_tags(test_cs_parse)
    
    print(f"Label: {label}")
    print(f"Tagged: {tagged}")