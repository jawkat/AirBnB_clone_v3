#!/usr/bin/python3
"""File Doc"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status')
def status():
    """status doc method."""
    return jsonify({"status": "OK"}), 200


@app_views.route('/stats')
def stats():
    """retrieves the number of each objects by type."""
    classes = {"amenities": "Amenity",
               "cities": "City", "places": "Place", "reviews": "Review",
               "states": "State", "users": "User"}

    num_objs = {}
    for key, value in classes.items():
        num_objs[key] = storage.count(value)
    return jsonify(num_objs)
