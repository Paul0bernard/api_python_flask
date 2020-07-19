from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
import requests
from error import InvalidUsage

app = Flask(__name__)
api = Api(app)

languages = [{}]
@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
    
@app.route('/create', methods= ['POST'])
def addCurriculo():

    payload = request.get_json()
    
    ret = requests.post('https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume',data =None, json=  payload)
    print('retorno', ret)

    if ret.status_code == 200:
        return ret.json()
    if ret.status_code == 500:
        raise  InvalidUsage('Dados não podem ser vazios', status_code=400)


if __name__ == '__main__':
    app.run(debug=True, port=8080)