import os

from flask import Flask, jsonify
from flask_cors import CORS
from supertokens_python import (
    get_all_cors_headers,
    init,
)
from supertokens_python.framework.flask import Middleware

from api import config, v1

init(
    supertokens_config=config.supertokens_config,
    app_info=config.app_info,
    framework=config.framework,
    recipe_list=config.recipe_list,
)

app = Flask(__name__)
# TODO: should middlware be after or before cors?
Middleware(app)
CORS(
    app=app,
    supports_credentials=True,
    origins=os.getenv("FRONTEND_URI"),
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)

app.register_blueprint(v1.v1, url_prefix="/")

@app.errorhandler(Exception)
def handle_error(error):
    response = {
        'responseType': 'error',
        'message': str(error)
    }
    return jsonify(response), getattr(error, 'code', 500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
