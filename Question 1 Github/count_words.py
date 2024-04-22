import os
import csv
import torch
from collections import Counter
import pandas as pd
from transformers import AutoModel, AutoTokenizer
import spacy
import re


def read_text_in_chunks(file_path, window_size=512, overlap=100):
    with open(file_path, 'r') as f:
        long_text = f.read()
        for i in range(0, len(long_text), window_size - overlap):
            chunk = long_text[i:i + window_size]
            yield chunk


    print ('chunked')
    
    
def count_words(text_file):
    word_counts = Counter()
    for chunk in read_text_in_chunks(text_file):
        words = chunk.split()
        word_counts.update(words)

    top_30_words = word_counts.most_common(30)

    with open('30_top_words_count.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        writer.writerows(top_30_words)

    print ('words counting done')
    
    
count_words('merged.txt')