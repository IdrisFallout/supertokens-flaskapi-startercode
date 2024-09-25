# v1.py

from flask import Flask, abort, g, jsonify, Blueprint
from supertokens_python.recipe.session.framework.flask import verify_session
from supertokens_python.recipe.multitenancy.syncio import list_all_tenants

# Create a blueprint
v1 = Blueprint("v1", __name__)

@v1.route("/sessioninfo", methods=["GET"])  # type: ignore
@verify_session()
def get_session_info():
    session_ = g.supertokens
    return jsonify(
        {
            "sessionHandle": session_.get_handle(),
            "userId": session_.get_user_id(),
            "accessTokenPayload": session_.get_access_token_payload(),
        }
    )

@v1.route("/tenants", methods=["GET"])  # type: ignore
def get_tenants():
    tenant_response = list_all_tenants()

    tenants_list = [tenant.to_json() for tenant in tenant_response.tenants]

    return jsonify({
        "status": "OK",
        "tenants": tenants_list,
    })

@v1.route("/", defaults={"u_path": ""})  # type: ignore

@v1.route("/<path:u_path>")  # type: ignore
def catch_all(u_path: str):  # pylint: disable=unused-argument
    abort(404)
