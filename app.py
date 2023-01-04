''' Starting point of the app '''
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    ''' Index '''
    return jsonify({'hello': 'world'})


@app.route('/about')
def about():
    ''' About '''
    return jsonify({'About': 'Us'})


if __name__ == 'main':
    app.run(debug=True)
