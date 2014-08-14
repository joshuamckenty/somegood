"""
Views for the somegood app
"""

from somegood import app
from flask import render_template, url_for
import requests
#import models

PHAXIO_URL = "https://api.phaxio.com/v1/send"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/faxdata.txt')
def faxdata():
    return "This is my fax text.", 200

@app.route('/sendfax')
def send_fax():
    app.logger.debug(url_for('faxdata', _external=True))
    params = {
        "to" : "+16502836846",
        "api_key" : app.config['PHAXIO_KEY'],
        "api_secret" : app.config['PHAXIO_SECRET'],
        "tag[order_id]" : "1234",
        "string_data" : url_for('faxdata', _external=True),
        "string_data_type" : "url"
        # callback_url
    }
    r= requests.post(PHAXIO_URL, data=params)
    return r.text
