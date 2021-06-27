from flask import Flask, jsonify, render_template, request
import os
from os import path
from api import api_routes

TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('../static')
global_base_dir = path.join(path.dirname(path.realpath(__file__)))
db_dir = path.join(global_base_dir, 'db')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/about')
def test_temp():
    return render_template('about.html')


@app.route('/invoice')
def invoice():
    print('Opened invoice')
    return render_template('invoice.html')

# API routes are below

@app.route('/api/submit_info_request', methods=['POST'])
def submit_info_request():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    print(name, email, phone)
    return {'name': name, 'email': email, 'phone': phone}

if __name__ == '__main__':
    app.run()
