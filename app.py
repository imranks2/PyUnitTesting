from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'hello': 'world'})


if __name__ == 'main':
    app.run(debug=True)