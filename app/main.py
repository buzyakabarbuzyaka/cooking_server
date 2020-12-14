from flask import Flask, send_file
import json
from os.path import join, dirname
from os import listdir
from random import choices
from math import ceil
from app.index import index, find

app = Flask(__name__)

IMG_DIR = join(dirname(__file__), '..', 'data', 'img')
index(IMG_DIR)


@app.route('/', methods=['GET'])
@app.route('/<int:num>', methods=['GET'])
def get_id_list(num=5):
    id_list = sorted(listdir(IMG_DIR))
    return {'list': choices(id_list, k=num)}


@app.route('/recipe/<int:cook_id>', methods=['GET'])
def get_json(cook_id):
    with open(join(IMG_DIR, str(cook_id), 'data.json')) as f:
        data = json.load(f)
    return data


@app.route('/title_img/<int:cook_id>', methods=['GET'])
def get_title_img(cook_id):
    filename = join(IMG_DIR, str(cook_id), 'title.jpg')
    return send_file(filename, mimetype='image/jpg')


@app.route('/step_img/<int:cook_id>/<img_name>', methods=['GET'])
def get_step_img(cook_id, img_name):
    filename = join(IMG_DIR, str(cook_id), img_name)
    return send_file(filename, mimetype='image/jpg')


@app.route('/find/page_count/<substr>', methods=['GET'])
@app.route('/find/page_count/<substr>/<int:items_on_page>', methods=['GET'])
def get_page_count(substr, items_on_page=10):
    result = find(substr)
    page_count = ceil(len(result)/items_on_page)
    return {'page_count': page_count}


@app.route('/find/list/<substr>', methods=['GET'])
@app.route('/find/list/<substr>/<int:page>', methods=['GET'])
@app.route('/find/list/<substr>/<int:items_on_page>/<int:page>', methods=['GET'])
def get_page_array(substr, items_on_page=10, page=1):
    result = find(substr)
    page_list = result[(page-1)*items_on_page:page*items_on_page]
    return {"items": page_list}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
