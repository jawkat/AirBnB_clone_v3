#!/usr/bin/python3
"""Module app.py Documentation"""
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import Flask, jsonify


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(exception):
    """Teardown function to close the storage session."""
    storage.close()


@app.errorhandler(404)
def page_not_found(err):
    """Handle 404 errors and return a JSON response with a 404 status code."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host=host, port=int(port), threaded=True)
