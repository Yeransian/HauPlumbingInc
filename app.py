from flask import Flask, jsonify, render_template
import os


TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('../static')
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/about')
def test_temp():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
