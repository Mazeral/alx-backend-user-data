README
======

Project: 0x02-Session_authentication
---------------------------

### Table of Contents

1. [Project Description](#project-description)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Documentation](#api-documentation)
6. [Testing](#testing)
7. [Contributing](#contributing)
8. [License](#license)

### Project Description

This project implements a Session-based authentication system for a Flask API. It allows users to log in and log out, and uses a Session ID stored in a cookie to authenticate requests.

### Requirements

* Python 3.7
* Flask
* Flask-RESTful
* Flask-SQLAlchemy
* Flask-HTTPAuth
* Werkzeug
* uuid
* base64
* os
* sys

### Installation

To install the project, run the following commands:

```bash
git clone https://github.com/alx-backend-user-data/0x02-Session_authentication.git
cd 0x02-Session_authentication
pip install -r requirements.txt
```

### Usage

To run the API, execute the following command:

```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
```

You can then use a tool like `curl` to test the API endpoints.

### API Documentation

The API has the following endpoints:

* `GET /api/v1/status`: Returns the status of the API.
* `GET /api/v1/users`: Returns a list of all users.
* `POST /api/v1/users`: Creates a new user.
* `GET /api/v1/users/<user_id>`: Returns a user by ID.
* `PUT /api/v1/users/<user_id>`: Updates a user by ID.
* `DELETE /api/v1/users/<user_id>`: Deletes a user by ID.
* `GET /api/v1/users/me`: Returns the current user.
* `POST /api/v1/auth_session/login`: Logs in a user and returns a Session ID.
* `DELETE /api/v1/auth_session/logout`: Logs out a user and deletes the Session ID.

### Testing

To run the tests, execute the following command:

```bash
python3 -m unittest discover -s tests
```

### Contributing

Contributions are welcome! Please submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
