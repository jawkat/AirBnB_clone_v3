#!/usr/bin/python3
"""Module app.py documentation.
this app.py file is about to :
1. Strict Slashes Configuration
2. Teardown Function
3. Custom 404 Error Handler
4. Configurable Host and Port
"""
from flask import Flask, jsonify
from os import getenv
from api.v1.views import app_views
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """Teardown function to close the storage session."""
    storage.close()


@app.errorhandler(404)
def page_not_fount(err):
    """Handle 404 errors and return a JSON response with a 404 status code."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host=host, port=int(port), threaded=True)
