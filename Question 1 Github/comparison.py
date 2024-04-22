import os
import csv
import torch
from collections import Counter
import pandas as pd
from transformers import AutoModel, AutoTokenizer
import spacy
import re
import pandas as pd
import csv

def read_csv_with_skipping(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for line_num, row in enumerate(reader, 1):
            try:
                if len(row) == 2: 
                    data.append(row)
                else:
                    print(f"Skipping row {line_num} with unexpected number of fields: {row}")
            except csv.Error as e:
                print(f"Error in row {line_num}: {e}")
    return data


def get_most_common_words(text, top_n=100):
    words = text.split()
    word_counts = Counter(words)
    return dict(word_counts.most_common(top_n))


def get_total_entities(entity_file):
    entities_df = pd.DataFrame(read_csv_with_skipping(entity_file), columns=['Column1', 'Column2'])
    total_entities = len(entities_df)   
    return total_entities

total_entities_sci = get_total_entities('spacy_entities.csv')
total_entities_bc5cdr = get_total_entities('bc5cdr_entities.csv')
total_entities_biobert = get_total_entities('biobert_entities.csv')


print(f'Total Entities (spaCy Sci): {total_entities_sci}')
print(f'Total Entities (spaCy BC5CDR): {total_entities_bc5cdr}')
print(f'Total Entities (BioBERT): {total_entities_biobert}')


def compare_most_common_words(model_words, other_model_words, model_name, other_model_name):
    common_words = set(model_words) & set(other_model_words)
    unique_model_words = set(model_words) - set(other_model_words)
    unique_other_model_words = set(other_model_words) - set(model_words)

    max_length = max(len(common_words), len(unique_model_words), len(unique_other_model_words))

    common_words = list(common_words)[:max_length] + [''] * (max_length - len(common_words))
    unique_model_words = list(unique_model_words)[:max_length] + [''] * (max_length - len(unique_model_words))
    unique_other_model_words = list(unique_other_model_words)[:max_length] + [''] * (max_length - len(unique_other_model_words))

    total_entities_model = [len(model_words)] * max_length
    total_entities_other_model = [len(other_model_words)] * max_length

    comparison_result = {
        f'{model_name} Unique Words': unique_model_words,
        f'{other_model_name} Unique Words': unique_other_model_words,
        'Common Words': common_words,
        f'Total {model_name} Entities': total_entities_model,
        f'Total {other_model_name} Entities': total_entities_other_model,
    }

    return pd.DataFrame(comparison_result, columns=[f'{model_name} Unique Words', f'{other_model_name} Unique Words', 'Common Words'])

spacy_entities_sci = pd.read_csv('spacy_entities.csv')
spacy_entities_bc5cdr = pd.read_csv('bc5cdr_entities.csv')
biobert_entities = pd.read_csv('biobert_entities.csv')

cleaned_entities = [str(entity) for entity in spacy_entities_sci['Entity']]
most_common_words_sci = get_most_common_words(' '.join(cleaned_entities))
most_common_words_bc5cdr = get_most_common_words(' '.join(spacy_entities_bc5cdr['Entity']))
most_common_words_biobert = get_most_common_words(' '.join(biobert_entities['Entity']))


comparison_sci_bc5cdr = compare_most_common_words(most_common_words_sci, most_common_words_bc5cdr, 'spaCy (Sci)', 'spaCy (BC5CDR)')
comparison_sci_biobert = compare_most_common_words(most_common_words_sci, most_common_words_biobert, 'spaCy (Sci)', 'BioBERT')
comparison_bc5cdr_biobert = compare_most_common_words(most_common_words_bc5cdr, most_common_words_biobert, 'spaCy (BC5CDR)', 'BioBERT')


comparison_sci_bc5cdr.to_csv('sci_bc5cdr_comparison.csv', index=False)
comparison_sci_biobert.to_csv('sci_biobert_comparison.csv', index=False)
comparison_bc5cdr_biobert.to_csv('bc5cdr_biobert_comparison.csv', index=False)

print('Comparison of 3 models done.')
