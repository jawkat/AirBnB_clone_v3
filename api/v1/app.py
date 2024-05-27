#!/usr/bin/python3
""" comments """
from os import getenv
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """comments """
    storage.close()


@app.errorhandler(404)
def page_not_fount(err):
    """ page not fount and header must return 404 """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":

    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host, port, threaded=True)
