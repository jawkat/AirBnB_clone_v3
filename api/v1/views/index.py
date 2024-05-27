#!/usr/bin/python
""" comments """
from flask import jsonify
from . import app_views

@app_views.route('/status', methods=['GET'])
def status():
    """ comments """
    return jsonify({"status": "OK"})
