#!/usr/bin/python3
'''File Doc.'''
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def status():
    '''status doc method.'''
    return jsonify({"status": "OK"}), 200


@app_views.route('/stats')
def stats():
    '''retrieves the number of each objects by type.'''
    # lasses = [amenities, City, Place, Review, State, User]
    # names = ["", "cities", "places", "reviews", "states", "users"]
    # test dictionary
    classes = {"amenities": Amenity,
               "cities": City, "places": Place, "reviews": Review,
               "states": State, "users": User}

    num_objs = {}
    for key, value in classes.items():
        num_objs[key] = storage.count(value)
    return jsonify(num_objs)
