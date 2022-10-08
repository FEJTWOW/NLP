from typing import Dict
import regex
import os

def normalize_content(content : str) -> str:
    content = content.lower()
    # remove everything that is not a word or space 
    content = regex.sub(r'[^\w\s]','', content)
    # remove extra spaces
    content = regex.sub(r'\s+',' ', content)
    return content

def read_bills(path : str) -> Dict[str, str]:
    bills_dict = {}
    for filename in filter(lambda p: p.endswith("txt"), os.listdir(path)):
        filepath = os.path.join(path, filename)
        with open(filepath, mode='r') as f:
            bills_dict[filename] = normalize_content(f.read())
    return bills_dict

if __name__ == '__main__':
    bills_dict = read_bills("/Users/kamil/Documents/NLP/data/first_ex_data/ustawy")
    for filename, content in bills_dict.items():
        print(f"{filename} ---- {content}")