"""
SomeGood's main flask app.

This is a placeholder for now.

"""

import os
from porc import Client
from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy, models_committed
# from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('somegood.config')
app.config.from_envvar('SOMEGOOD_SETTINGS', silent=True)

# mail = Mail(app)
# db = SQLAlchemy(app)


# client = Client(os.environ.get('ORCHESTRATE_KEY', 'foo'))
# client.ping().raise_for_status()

import somegood.views


if __name__ == '__main__':
    app.run()
