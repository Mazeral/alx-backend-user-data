#!/usr/bin/env python3
"""
Flask app module.
"""

from flask import Flask, jsonify, request, abort
from auth import Auth

# Defining the Flask app instance
app = Flask(__name__)
auth = Auth()


@app.route("/")
def home():
    """
    Home route that returns a welcome message.

    This route handles GET requests to the root URL ("/") and responds with
    a JSON object containing a welcome message.

    Returns:
        Response: A Flask JSON response with a message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """
    Handles user registration via a POST request.

    This route retrieves the `email` and `password` from the request form data,
    and attempts to register a new user using the `auth.register_user` method.
    If the registration is successful, it returns a JSON response indicating
    the user has been created. If the email is already registered, it returns
    an error response with status code 400.

    Returns:
        Response: A JSON response with a success message and the email on
                  successful registration, or an error message if the
                  registration fails.

    Raises:
        Exception: Any exception raised during user registration is caught
                   and handled, returning an appropriate error message.
    """
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        # Attempt to register the user, error generates here if any
        user = auth.register_user(email, password)

        # Return success response
        return jsonify({
            "email": email,
            "message": "user created"
        })
    except Exception as e:
        # Return error response if email is already registered
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=["POST"])
def login():
    """
    Handles user login by validating credentials and creating a session.

    This route receives user login credentials via a POST request, validates
    the email and password, and creates a session for the user if the
    credentials are correct. If the login is successful, it returns a JSON
    response indicating success. If the credentials are invalid, it aborts
    with a 401 status code.

    Methods:
        POST

    Returns:
        Response: A JSON response with the user's email and a success message
                  if login is successful.

    Raises:
        401 Unauthorized: If the provided credentials are invalid.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    login_validation = auth.valid_login(email=email, password=password)
    if login_validation:
        auth.create_session(email=email)
        return jsonify({"email": email, "message": "logged in"})

    abort(401)


# Running the Flask app
if __name__ == "__main__":
    """
    Entry point of the Flask application.

    This block runs the Flask app on host 0.0.0.0 and port 5000, making it
    accessible on all network interfaces.
    """
    app.run(host="0.0.0.0", port="5000")
