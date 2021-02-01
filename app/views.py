import datetime
import json

import requests
from flask import render_template, redirect, request

from app import app

# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

@app.route('/')
def index():
    return render_template('index.html',
                           title='Startup Documents')

@app.route('/submitstartup', methods=['POST'])
def submit_textarea1():
    """
    Endpoint to create a new transaction via our application.
    """
    post_content = request.form["content"]
    post_content2 = request.form["content2"]
    author = request.form["author"]

    post_object = {
        'author': author,
        'content': post_content,
        'content2': post_content2,
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/searchfunders')

@app.route('/submitfunder', methods=['POST'])
def submit_textarea2():
    """
    Endpoint to create a new transaction via our application.
    """
    post_content = request.form["content"]
    post_content2 = request.form["content2"]
    author = request.form["author"]

    post_object = {
        'author': author,
        'content': post_content,
        'content2': post_content2,
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/searchstartup')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')

@app.route('/searchfunders',methods=['POST','GET'])
def searchfunders():
    return render_template('search.html')

@app.route('/searchstartup',methods=['POST','GET'])
def searchstartup():
    return render_template('searchstartup.html')


