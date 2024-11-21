#!/usr/bin/env python3
"""
Integration tests
"""
import requests


link = "http://localhost:5000/{}"


def register_user(email: str, password: str) -> None:
    """
    Registers a new user.

    Args:
        email (str): Email address.
        password (str): Password.

    Returns:
        None
    """
    url = "http://localhost:5000/users"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    assert response.status_code == 200, f"Expected 200, got: \
            {response.status_code}"
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Attempts to log in with an incorrect password.

    Args:
        email (str): Email address.
        password (str): Incorrect password.

    Returns:
        None
    """
    url = link.format("sessions")
    data = {"email": email, "password": "BlaBla"}
    response = requests.post(url, data=data)
    assert response.status_code == 401, f"Expected 401, \
            got: {response.status_code}"


def log_in(email: str, password: str) -> str:
    """
    Logs in a user.

    Args:
        email (str): Email address.
        password (str): Password.

    Returns:
        str: Session ID.
    """
    url = link.format("sessions")
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    assert response.status_code == 200, f"Expected 200,\
            got: {response.status_code}"
    assert response.json() == {"email": email, "message": "logged in"}
    session_id = response.cookies.get("session_id")
    if not session_id:
        raise ValueError("Session ID cookie is missing")
    return session_id


def profile_unlogged() -> None:
    """
    Attempts to access the profile without being logged in.

    Returns:
        None
    """
    url = link.format("profile")
    data = {"session_id": ""}
    response = requests.get(url, data=data)
    assert response.status_code == 403, f"Expected 403,\
            got: {response.status_code}"


def profile_logged(session_id: str) -> None:
    """
    Attempts to access the profile while logged in.

    Args:
        session_id (str): Session ID.

    Returns:
        None
    """
    url = link.format("profile")
    data = {"session_id": session_id}
    response = requests.get(url, data=data)
    assert response.status_code == 200, f"Expected 200,\
            got: {response.status_code}"
    assert response.json() == {"email": EMAIL}


def log_out(session_id: str) -> None:
    """
    Logs out a user.

    Args:
        session_id (str): Session ID.

    Returns:
        None
    """
    url = link.format("sessions")
    data = {"session_id": session_id}
    response = requests.delete(url, data=data)
    assert response.status_code == 200, f"Expected 200,\
            got: {response.status_code}"


def reset_password_token(email: str) -> str:
    """
    Requests a password reset token.

    Args:
        email (str): Email address.

    Returns:
        str: Reset token.
    """
    url = link.format("reset_password")
    data = {"email": email}
    response = requests.post(url, data=data)
    assert response.status_code == 200, f"Expected 200,\
            got: {response.status_code}"
    response_data = response.json()
    assert "reset_token" in response_data
    reset_token = response_data["reset_token"]
    assert response_data == {"email": email, "reset_token": reset_token}
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Updates a user's password.

    Args:
        email (str): Email address.
        reset_token (str): Reset token.
        new_password (str): New password.

    Returns:
        None
    """
    url = link.format("reset_password")
    data = {"email": email, "reset_token": reset_token,
            "new_password": new_password}
    response = requests.put(url, data=data)
    assert response.status_code == 200, f"Expected 200,\
            got: {response.status_code}"
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
