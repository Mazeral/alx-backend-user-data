# README.md

## Table of Contents

1. [User Model](#user-model)
2. [Create User](#create-user)
3. [Find User](#find-user)
4. [Update User](#update-user)
5. [Hash Password](#hash-password)
6. [Register User](#register-user)
7. [Basic Flask App](#basic-flask-app)
8. [Register User End-point](#register-user-end-point)
9. [Credentials Validation](#credentials-validation)
10. [Generate UUIDs](#generate-uuids)
11. [Get Session ID](#get-session-id)
12. [Log in](#log-in)
13. [Find User by Session ID](#find-user-by-session-id)
14. [Destroy Session](#destroy-session)
15. [Log out](#log-out)
16. [User Profile](#user-profile)
17. [Generate Reset Password Token](#generate-reset-password-token)
18. [Get Reset Password Token](#get-reset-password-token)
19. [Update Password](#update-password)
20. [Update Password End-point](#update-password-end-point)
21. [End-to-end Integration Test](#end-to-end-integration-test)

## User Model

The User model is defined in the `user.py` file. It has the following attributes:

* `id`: the integer primary key
* `email`: a non-nullable string
* `hashed_password`: a non-nullable string
* `session_id`: a nullable string
* `reset_token`: a nullable string

## Create User

The `add_user` method is implemented in the `db.py` file. It takes two required string arguments: `email` and `hashed_password`, and returns a User object.

## Find User

The `find_user_by` method is implemented in the `db.py` file. It takes arbitrary keyword arguments and returns the first row found in the users table as filtered by the method’s input arguments.

## Update User

The `update_user` method is implemented in the `db.py` file. It takes a required `user_id` integer argument and arbitrary keyword arguments, and returns None.

## Hash Password

The `_hash_password` method is implemented in the `auth.py` file. It takes a password string argument and returns bytes.

## Register User

The `register_user` method is implemented in the `auth.py` file. It takes mandatory `email` and `password` string arguments and returns a User object.

## Basic Flask App

The basic Flask app is implemented in the `app.py` file. It has a single GET route ("/") and returns a JSON payload of the form {"message": "Bienvenue"}.

## Register User End-point

The `users` function is implemented in the `app.py` file. It responds to the POST /users route and expects two form data fields: "email" and "password".

## Credentials Validation

The `valid_login` method is implemented in the `auth.py` file. It takes `email` and `password` required arguments and returns a boolean.

## Generate UUIDs

The `_generate_uuid` function is implemented in the `auth.py` file. It returns a string representation of a new UUID.

## Get Session ID

The `create_session` method is implemented in the `auth.py` file. It takes an `email` string argument and returns the session ID as a string.

## Log in

The `login` function is implemented in the `app.py` file. It responds to the POST /sessions route and expects form data with "email" and "password" fields.

## Find User by Session ID

The `get_user_from_session_id` method is implemented in the `auth.py` file. It takes a single `session_id` string argument and returns the corresponding User or None.

## Destroy Session

The `destroy_session` method is implemented in the `auth.py` file. It takes a single `user_id` integer argument and returns None.

## Log out

The `logout` function is implemented in the `app.py` file. It responds to the DELETE /sessions route and expects the session ID as a cookie with key "session_id".

## User Profile

The `profile` function is implemented in the `app.py` file. It responds to the GET /profile route and expects a session_id cookie.

## Generate Reset Password Token

The `get_reset_password_token` method is implemented in the `auth.py` file. It takes an `email` string argument and returns a string.

## Get Reset Password Token

The `get_reset_password_token` function is implemented in the `app.py` file. It responds to the POST /reset_password route and expects form data with the "email" field.

## Update Password

The `update_password` method is implemented in the `auth.py` file. It takes `reset_token` string argument and a `password` string argument and returns None.

## Update Password End-point

The `update_password` function is implemented in the `app.py` file. It responds to the PUT /reset_password route and expects form data with fields "email", "reset_token" and "new_password".

## End-to-end Integration Test

The end-to-end integration test is implemented in the `main.py` file. It tests the following tasks:

* register_user
* log_in_wrong_password
* log_in
* profile_unlogged
* profile_logged
* log_out
* reset_password_token
* update_password
