import csv
from transformers import AutoTokenizer
from collections import Counter


def count_unique_tokens(text_file_path, model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    with open(text_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    tokens = tokenizer.tokenize(text)

    token_counts = Counter(tokens)

    return token_counts

def get_top_30_tokens(token_counts):
    return token_counts.most_common(30)

def write_to_csv(output_file, top_tokens):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['tokens', 'count']) 
        for token, count in top_tokens:
            writer.writerow([token, count])

text_file_path = "merged.txt"
model_name = "dmis-lab/biobert-v1.1"

output_csv_file = "30_top_tokens_count.csv"
token_counts = count_unique_tokens(text_file_path, model_name)

top_30_tokens = get_top_30_tokens(token_counts)
write_to_csv(output_csv_file, top_30_tokens)

print("Top 30 tokens and their counts saved to", output_csv_file)
