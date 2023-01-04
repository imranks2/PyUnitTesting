from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'hello': 'world'})


@app.route('/about')
def about():
    return jsonify({'About': 'Us'})


if __name__ == 'main':
    app.run(debug=True)
