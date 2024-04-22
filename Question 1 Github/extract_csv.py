
import os
import re
import pandas as pd

def extract_text_from_csvs(folder_path):
    text_list = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            filepath = os.path.join(folder_path, filename)
            df = pd.read_csv(filepath)
            text_column = [col for col in df.columns if 'TEXT' in col][0]
            raw_text = ' '.join(df[text_column].tolist())

            cleaned_text = ' '.join(re.findall(r'\b[a-zA-Z]{4,}\b', raw_text))

            text_list.append(cleaned_text)

    with open('merged.txt', 'w') as f:
        f.write('\n'.join(text_list))

    print('Text extracted from CSV and converted into merged.txt.')

extract_text_from_csvs("C:/Users/Prasa/OneDrive/Desktop/Assignment-2/Question 1/Question 1")