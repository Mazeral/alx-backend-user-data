#!/usr/bin/env python3
""" Module of session auth views
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route(
        '/auth_session/login',
        methods=['POST'],
        strict_slashes=False
        )
def login():
    """POST /auth_session/login
    Handles session-based login.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if email or password is missing
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    # Search for the user by email
    try:
        users = User.search({"email": email})
    except Exception as e:
        return jsonify({"error": "no user found for this email"}), 404

    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    # Check if password is valid
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a session for the user
    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    # Set the session ID as a cookie
    response = jsonify(user.to_json())
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)

    return response



@app_views.route(
        'auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False
        )
def destroy_session():
    """Destroying session
    """
    from api.v1.auth import auth
    auth = Auth()
    result = auth.destroy_session(request)
    if result == False:
        abort(404)
    return jsonify({}), 200
