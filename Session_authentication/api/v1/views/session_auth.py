#!/usr/bin/env python3
""" session authentication module """


from flask import request, jsonify, abort
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ handles user login """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # import here cuz i dont want no problems
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(auth.session_cookie_name(), session_id)
    session_name = os.getenv('SESSION_NAME')
    return response

@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """ logs out user by destroying session """
    from api.v1.app import auth
    destroyed = auth.destroy_session(request)
    if not destroyed:
        abort(404)
    return jsonify({}), 200
