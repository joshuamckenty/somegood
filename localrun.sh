#!/usr/bin/env bash

export SOMEGOOD_CONFIG="config.py"
gunicorn somegood:app
