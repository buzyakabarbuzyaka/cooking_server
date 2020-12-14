import csv
from typing import List
from pprint import pprint

FIND_ARR = []
with open("index.csv", encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=";")
    for dict_line in reader:
        FIND_ARR.append((dict_line['id'], dict_line['title'].lower()))
pprint(FIND_ARR)


def find(substr: str) -> List[str]:
    substr = substr.lower()
    id_arr = []
    for data_id, title in FIND_ARR:
        if substr in title:
            id_arr.append(data_id)
    return id_arr
