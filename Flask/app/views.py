from flask import Blueprint, jsonify, request
from .utils import save, getAll
from .models import WebAPI
main = Blueprint('main', __name__)

@main.route('/add', methods = ['GET','POST'])
def add():
    if request.method == 'GET':
        
        data_test =  WebAPI.query.all()
        print(data_test)
        datas = []

        for data in data_test:
            print(data.id," - ",data.data)
            data = {
                'id' : data.id,
                'data' : data.data 
            }
            datas.append(data)
        print(datas)
        print(type(data_test))
        return jsonify(datas)
    else:
        data = request.get_json()
        query = data.get("query")
        save(query)
    return jsonify(data)

# @main.route('/add', methods = ['GET'])
# def get():
#     query = 'test'
#     save(query)
#     return jsonify(query)