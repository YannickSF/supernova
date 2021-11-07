
import os
from flask import Flask, request
from flask_cors import CORS
from nosql import Table, where, PROJECT_PATH, DATABASE_PATH


HOST = '0.0.0.0'
PORT = 5000


app = Flask(__name__)
cors = CORS(app)
session = {}


def _upload():
    tables = os.listdir(os.path.join(PROJECT_PATH, DATABASE_PATH))
    for table in tables:
        session[table.split('.')[0]] = Table(table.split('.')[0])


def table_exist(table):
    return len([t for t in session.keys() if t == table]) > 0


@app.route("/")
def index():
    return {
        'supernova': 200,
        'tables': len(session.keys())
    }


def read(table_name, item=None):
    if not table_exist(table_name):
        return {'error': 'unknown table name.'}

    if item is None:
        return {'table': session[table_name].all()}

    return {'item': session[table_name].search(where('primary') == item)}


def upsert(table_name, item, **kwargs):
    if not table_exist(table_name):
        session[table_name] = Table(table_name)

    kwargs['primary'] = item
    return {
        'index': session[table_name].upsert(kwargs, where('primary') == item),
        'item': read(table_name, item)['item']
    }


def delete(table_name, item):
    if not table_exist(table_name):
        return {'error': 'unknown table name.'}

    return {'item': session[table_name].remove(where('primary') == item)}


@app.route("/<string:table>", methods=['GET'])
def read_table(table):
    if request.method == 'GET':
        return read(table)

    return {'error': 'method not allow.'}


@app.route("/<string:table>/<string:item>", methods=['GET', 'PUT', 'DELETE'])
def read_upsert_delete(table, item):
    if request.method == 'GET':
        return read(table, item)

    if request.method == 'PUT':
        return upsert(table, item, **request.get_json())

    if request.method == 'DELETE':
        return delete(table, item)

    return {'error': 'method not allow'}


if __name__ == '__main__':
    _upload()
    app.run(host=HOST, port=PORT)
