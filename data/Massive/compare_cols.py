import pandas as pd

df = pd.read_excel('Processed_Massive_new_new.xlsx')

df['modified_query_word_count'] = 0
df['labels_word_count'] = 0
df['word_count_match'] = False

for i in range(len(df)):
    mod_query = str(df.loc[i, 'modified_query'])
    labels = str(df.loc[i, 'labels'])
    
    mod_query_words = len(mod_query.split()) if mod_query else 0
    labels_words = len(labels.split()) if labels else 0
    
    df.loc[i, 'modified_query_word_count'] = mod_query_words
    df.loc[i, 'labels_word_count'] = labels_words
    
    df.loc[i, 'word_count_match'] = mod_query_words == labels_words

df.to_excel('Processed_Massive_With_Word_Count.xlsx', index=False)
