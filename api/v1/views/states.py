#!/usr/bin/python3
""" File's module Documentation """

from flask import Flask, jsonify, request, abort
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states', methods=['GET'])
def get_states():
    """Get method to retrieve all State objects"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app.route('/states', methods=['GET'])
def get_state(state_id):
    """Get method check if state_id is linked to
    Rest Actions"""
    if not storage.get(State, state_id):
        abort(404)
    return jsonify(storage.get(State, state_id).to_dict())


@app.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app.route('/states', methods=['POST'])
def post_states():
    req_http = request.get_json()
    if not req_http:
        abort(400, "Not a JSON")
    if not req_http.get('name'):
        abort(400, "Missing a name")
    new = State(**req_http)
    new.save()
    return jsonify(), 201
