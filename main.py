from flask import Flask, send_file
import json
from os.path import join, dirname
from os import listdir
from random import choices

app = Flask(__name__)

IMG_DIR = join(dirname(__file__), 'data', 'img')


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


@app.route('/title_img/<int:cook_id>')
def get_title_img(cook_id):
    filename = join(IMG_DIR, str(cook_id), 'title.jpg')
    return send_file(filename, mimetype='image/jpg')


@app.route('/step_img/<int:cook_id>/<img_name>')
def get_step_img(cook_id, img_name):
    filename = join(IMG_DIR, str(cook_id), img_name)
    return send_file(filename, mimetype='image/jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
