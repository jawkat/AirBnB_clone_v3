#!/usr/bin/python3
"""
Application setup and entry point.
"""
from os import getenv
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage

# Initialize the Flask application
app = Flask(__name__)

# Register the blueprint with the Flask app
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """
    Teardown function to close the storage session
    """
    storage.close()

<<<<<<< HEAD

@app.errorhandler(404)
def page_not_fount(err):
    """ page not fount and header must return 404 """
    return jsonify({"error": "Not found"}), 404


=======
>>>>>>> refs/remotes/origin/master
if __name__ == "__main__":
    """
    Main entry point for the application.
    Retrieves host and port from environment variables and runs the Flask app.
    """
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    # Run the Flask app
    app.run(host=host, port=int(port), threaded=True)
