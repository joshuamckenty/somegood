"""
SomeGood's main flask app.

This is a placeholder for now.

"""

import os
from porc import Client
from flask import Flask

app = Flask(__name__)

client = Client(os.environ['ORCHESTRATE_KEY'])
client.ping().raise_for_status()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
