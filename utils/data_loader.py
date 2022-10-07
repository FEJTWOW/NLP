from typing import Dict
import os

def read_bills(path : str) -> Dict[str, str]:
    bills_dict = {}
    for filename in filter(lambda p: p.endswith("txt"), os.listdir(path)):
        filepath = os.path.join(path, filename)
        with open(filepath, mode='r') as f:
            bills_dict[filename] = f.read()
    return bills_dict

if __name__ == '__main__':
    bills_dict = read_bills("/Users/kamil/Documents/NLP/data/first_ex_data/ustawy")
    for filename, content in bills_dict.items():
        print(f"{filename} ---- {content}")