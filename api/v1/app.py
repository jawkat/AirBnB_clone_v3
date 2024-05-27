#!/usr/bin/python
import os
from flask import Flask
from flask_cors import CORS
from api.v1.views import app_views
from models import storage


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown_appcontext(exception):
    """comments """
    storage.close()

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
