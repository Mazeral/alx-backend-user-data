#!/usr/bin/env python3
"""
Flask app module.
"""

from flask import Flask, jsonify, request
from auth import Auth

# Defining the Flask app instance
app = Flask(__name__)


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
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        auth = Auth()
        user = auth.register_user(email, password)
    return jsonify({"email" : email,
                    "message": "user created"})
    except Exception as e:
            return jsonify({"message": "email already registered"}), 400


# Running the Flask app
if __name__ == "__main__":
    """
    Entry point of the Flask application.

    This block runs the Flask app on host 0.0.0.0 and port 5000, making it
    accessible on all network interfaces.
    """
    app.run(host="0.0.0.0", port="5000")
