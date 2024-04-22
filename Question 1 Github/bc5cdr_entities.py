import spacy 
import os

from count_words import read_text_in_chunks


nlp = spacy.load("C:/Users/Prasa/OneDrive/Desktop/Assignment-2/Question 1/Question 1/en_ner_bc5cdr_md-0.5.4/en_ner_bc5cdr_md-0.5.4/en_ner_bc5cdr_md/en_ner_bc5cdr_md-0.5.4")

text_chunks = read_text_in_chunks('merged.txt', window_size=100000, overlap=20000)

all_entities_spacy = []
for chunk in text_chunks:
    doc_spacy = nlp(chunk)
    entities_spacy = [(ent.text, ent.label_) for ent in doc_spacy.ents]
    all_entities_spacy.extend(entities_spacy)

with open('bc5cdr_entities.csv', 'w') as spacy_file:
    spacy_file.write('Entity,Label\n')
    for entity in all_entities_spacy:
        spacy_file.write(f'{entity[0]},{entity[1]}\n')

print ('bc5cdr entities done')