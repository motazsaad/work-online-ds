from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/')
def home():
    return '<h1> Hello from flask </h1>'

@app.route('/fruitdetect')
def classify_fruit():
    return jsonify({'label': 'apple'})

# 5. run the app in main
if __name__ == '__main__':
    app.run()
