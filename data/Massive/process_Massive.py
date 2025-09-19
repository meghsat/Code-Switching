import pandas as pd

def process_parse(cs_parse, cs_query):
    # Remove outer [ and ] if present
    if cs_parse.startswith('[') and cs_parse.endswith(']'):
        cs_parse = cs_parse[1:-1].strip()
    
    # Extract intent
    if not cs_parse.startswith('IN:'):
        raise ValueError("Invalid format: cs_parse must start with 'IN:'", cs_query)
    
    # Find the end of the intent name (first space after IN:)
    intent_start = 3  # After 'IN:'
    intent_space = cs_parse.find(' ', intent_start)
    if intent_space == -1:
        raise ValueError("No space after intent name ", cs_query)
    
    intent = cs_parse[intent_start:intent_space]
    sentence_str = cs_parse[intent_space + 1:].strip()
    
    # Parse sentence_str to build labels and collect replacements
    labels = []
    replacements = []
    pos = 0
    while pos < len(sentence_str):
        if sentence_str[pos].isspace():
            pos += 1
            continue
        
        if sentence_str[pos:pos + 4] == '[SL:':
            # Extract slot_name
            slot_start = pos + 4
            slot_space = sentence_str.find(' ', slot_start)
            if slot_space == -1:
                raise ValueError("No space after slot_name{cs_query}")
            
            slot_name = sentence_str[slot_start:slot_space]
            phrase_start = slot_space + 1
            close_pos = sentence_str.find(']', phrase_start)
            if close_pos == -1:
                raise ValueError("No closing ] ", cs_query)
            
            phrase = sentence_str[phrase_start:close_pos].strip()
            if phrase:
                underscored = phrase.replace(' ', '_')
                replacements.append((phrase, underscored))
                labels.append(slot_name)
            
            pos = close_pos + 1
        else:
            # Normal word
            word_end = sentence_str.find(' ', pos)
            if word_end == -1:
                word_end = len(sentence_str)
            
            word = sentence_str[pos:word_end].strip()
            if word:
                labels.append('O')
            
            pos = word_end
    
    # Apply replacements to cs_query
    modified_query = cs_query
    for orig, under in replacements:
        modified_query = modified_query.replace(orig, under)
    
    labels_str = ' '.join(labels)
    return modified_query, labels_str, intent

# Load the Excel file
df = pd.read_excel('Massive.xlsx')

# Add new columns
df['modified_query'] = ''
df['labels'] = ''
df['intent'] = ''

# Process each row
for i in range(len(df)):
    cs_query = df.loc[i, 'cs_query']
    cs_parse = df.loc[i, 'cs_parse']
    try:
        mod_q, labs, intt = process_parse(cs_parse, cs_query)
        df.loc[i, 'modified_query'] = mod_q
        df.loc[i, 'labels'] = labs
        df.loc[i, 'intent'] = intt
    except ValueError as e:
        print(f"Error processing row {i}: {e}")
        df.loc[i, 'modified_query'] = cs_query
        df.loc[i, 'labels'] = ''
        df.loc[i, 'intent'] = ''

# Save the processed DataFrame to a new Excel file
df.to_excel('Processed_Massive.xlsx', index=False)
