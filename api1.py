'''
RESTFul API in flask
1. flask jsonify
2. flask_restful
'''

# method 1
# step 1 import
from flask import Flask, jsonify, request
import random

# step 2 define obj from Flask class
app = Flask(__name__)


# step 3 define web page
@app.route('/')
# step 4 define function for this page
def home():
    return '<h1> Hello from flask </h1>'


def dummy_classifier(features):
    print(features)
    labels = ['apple', 'banana', 'orange']
    mylabel = random.sample(labels, 1)
    return {'label': mylabel[0]}


@app.route('/fruitdetect')
def classify_fruit():
    features = request.args.get('features')
    print(features)
    return jsonify(dummy_classifier(features))


# 5. run the app in main
if __name__ == '__main__':
    app.run()
