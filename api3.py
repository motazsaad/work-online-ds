from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class MLClassifier(Resource):
    def get(self):
        return {'label': 'apple'}


api.add_resource(MLClassifier, '/classifer')

if __name__ == '__main__':
    app.run()