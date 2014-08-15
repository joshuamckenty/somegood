#!/usr/bin/env bash

export SOMEGOOD_CONFIG="config.py"
# export SOMEGOOD_SERVER_NAME="somegood.org"
gunicorn somegood:app
