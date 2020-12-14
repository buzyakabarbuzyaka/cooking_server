import os
import json
from os.path import dirname, join


def index(path):
    with open('index.csv', 'w', encoding='utf-8') as f:
        f.write('id;title\n')
        folder_list = os.listdir(path)
        for folder in folder_list:
            tmp_path = join(path, folder, 'data.json')
            with open(tmp_path, 'r', encoding="utf-8") as file_data:
                data = json.load(file_data)
            data_id = data['id']
            title = data['title']
            tmp_string = f"{data_id};{title}\n"

            f.write(tmp_string)
