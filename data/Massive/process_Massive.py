import pandas as pd
import re

def process_parse(cs_parse, cs_query):
    # Remove outer [ and ] if present
    if cs_parse.startswith('[') and cs_parse.endswith(']'):
        cs_parse = cs_parse[1:-1].strip()
    
    # Extract intent
    if not cs_parse.startswith('IN:'):
        raise ValueError("Invalid format: cs_parse must start with 'IN:'")
    
    # Find the end of the intent name (first space after IN:)
    intent_start = 3  # After 'IN:'
    intent_space = cs_parse.find(' ', intent_start)
    if intent_space == -1:
        raise ValueError("No space after intent name")
    
    intent = cs_parse[intent_start:intent_space]
    sentence_str = cs_parse[intent_space + 1:].strip()
    
    # Normalize slot tags: remove colon and extra spaces after SL:<slot_name>
    normalized_sentence = re.sub(r'\[SL:([^\s:]+)(?:\s*:\s*)', r'[SL:\1 ', sentence_str)
    
    # Parse sentence_str to build labels, replacements, and modified parse
    labels = []
    replacements = []
    pos = 0
    modified_parse_parts = []
    while pos < len(normalized_sentence):
        if normalized_sentence[pos].isspace():
            modified_parse_parts.append(normalized_sentence[pos])
            pos += 1
            continue
        
        if normalized_sentence[pos:pos + 4] == '[SL:':
            # Extract slot_name
            slot_start = pos + 4
            slot_space = normalized_sentence.find(' ', slot_start)
            if slot_space == -1:
                raise ValueError("No space after slot_name")
            
            slot_name = normalized_sentence[slot_start:slot_space]
            phrase_start = slot_space + 1
            close_pos = normalized_sentence.find(']', phrase_start)
            if close_pos == -1:
                raise ValueError("No closing ]")
            
            phrase = normalized_sentence[phrase_start:close_pos].strip()
            if phrase:
                underscored = phrase.replace(' ', '_')
                replacements.append((phrase, underscored))
                labels.append(f"B-{slot_name}")
                # Add modified slot tag to modified_parse
                modified_parse_parts.append(f"[SL:{slot_name} {underscored}]")
            
            pos = close_pos + 1
        else:
            # Normal word
            word_end = normalized_sentence.find(' ', pos)
            if word_end == -1:
                word_end = len(normalized_sentence)
            
            word = normalized_sentence[pos:word_end].strip()
            if word:
                labels.append('O')
                modified_parse_parts.append(word)
            
            pos = word_end
    
    # Apply replacements to cs_query
    modified_query = cs_query
    for orig, under in replacements:
        modified_query = modified_query.replace(orig, under)
    
    # Construct modified_parse
    modified_parse = f"[IN:{intent} {' '.join(modified_parse_parts)}]"
    
    labels_str = ' '.join(labels)
    return modified_query, labels_str, intent, modified_parse

# Load the Excel file
df = pd.read_excel('Massive.xlsx')

# Add new columns
df['modified_query'] = ''
df['labels'] = ''
df['intent'] = ''
df['modified_parse'] = ''

# Process each row
for i in range(len(df)):
    cs_query = df.loc[i, 'cs_query']
    cs_parse = df.loc[i, 'cs_parse']
    try:
        mod_q, labs, intt, mod_p = process_parse(cs_parse, cs_query)
        df.loc[i, 'modified_query'] = mod_q
        df.loc[i, 'labels'] = labs
        df.loc[i, 'intent'] = intt
        df.loc[i, 'modified_parse'] = mod_p
    except ValueError as e:
        print(f"Error processing row {i}: {e}")
        df.loc[i, 'modified_query'] = cs_query
        df.loc[i, 'labels'] = ''
        df.loc[i, 'intent'] = ''
        df.loc[i, 'modified_parse'] = cs_parse

# Save the processed DataFrame to a new Excel file
df.to_excel('Processed_Massive.xlsx', index=False)
