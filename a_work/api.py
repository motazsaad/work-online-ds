from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class MLClassifier(Resource):
    def get(self):
        return {'label':'apple'}

class Home(Resource):
    def get(self):
        return 'Haha'


api.add_resource(MLClassifier,'/classifier')
api.add_resource(Home,'/')

#@app.route('/')
#def home():
#    return 'hi man'

#@app.route('/fruitdetect')
#def classify_fruit():
#    return jsonify({'label':'apple'})


if __name__ == '__main__':
    app.run()