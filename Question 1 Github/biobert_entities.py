import csv
import torch
import os
import tensorflow as tf 

os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"
from transformers import AutoTokenizer, AutoModelForTokenClassification


tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-v1.1")


with open("merged.txt", "r") as file:
    text = file.read()
tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

with torch.no_grad():
    outputs = model(**tokens)

predictions = outputs.logits.argmax(-1).squeeze().tolist()
tokens = tokens["input_ids"].squeeze().tolist()

entity_labels = {
    4: "B-Disease", 5: "I-Disease", 6: "B-Drug", 7: "I-Drug"
}

current_entity = ""
entities = {
    "Diseases": [],
    "Drugs": []
}

for token, prediction in zip(tokens, predictions):
    token = tokenizer.decode(token, skip_special_tokens=True)
    label = entity_labels.get(prediction, "O")
    
    if label == "B-Disease" or label == "B-Drug":
        if current_entity:
            entities[current_entity].append(current_text)
        current_entity = "Diseases" if label == "B-Disease" else "Drugs"
        current_text = token
    elif label == "I-Disease" or label == "I-Drug":
        current_text += " " + token


if current_entity and current_text:
    entities[current_entity].append(current_text)

output_file = "biobert_entities.csv"

with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["Entity", "Label"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for disease in entities["Diseases"]:
        writer.writerow({"Entity": disease, "Label": "Disease"})

    for drug in entities["Drugs"]:
        writer.writerow({"Entity": drug, "Label": "Drug"})

print(f"Extracted entities saved to {output_file}")
