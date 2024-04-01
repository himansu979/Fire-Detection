from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
#CORS(app)


@app.route('/')
def hello_world():
    return "<p>Hello, World 2!</p>"


if __name__ == '__main__':
    app.run(port=8000)


