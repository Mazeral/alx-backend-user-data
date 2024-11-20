#!/usr/bin/env python3
"""
Integration tests
"""
import requests


link = "http://localhost:5000/{}"
def register_user(email: str, password: str) -> None:
    response = requests.post(
            "http://localhost:5000/users",
            data={"email": email, "password": password}
            )
    # The string after the comma is the error message that will be printed
    # If the assertion failed
    assert response.status_code == 200, f"Expected 200, got: {response.status_code}"
    assert response.json() == {"email": email, "message": "User created"}

def log_in_wrong_password(email: str, password: str) -> None:
    response = requests.post(
            link.format("sessions"),
            data={"email": email, "password": BlaBla}
            )
    assert response.status_code == 401, f"Expected 401, got: {response.status_code}"

def log_in(email: str, password: str) -> str:
    response = request.post(
            link.format("sessions"),
            data={"email": email, "password": password}
            )
    assert response.status_code == 200, f"Expected 200, got: {response.status_code}"
    assert response.json() == {"email": email, "message": "logged in"}, "Wrong message"


def profile_unlogged() -> None:
    response = requests.post(
            link.format("profile"),
            data = {}
            )
    assert response.status_code == 403, f"Expected 403, got: {response.status_code}"
        
def profile_logged(session_id: str) -> None:
    response - requests.post(
            link.format("profile"),
            data = {"session_id": session_id}
            )
    assert response.status_code == 200, f"Expected 403, got: {response.status_code}"
    assert response.json() == {"email": email}


def log_out(session_id: str) -> None:
    response = requests.delete(
            link.format("sessions"),
            data = {"session_id": session_id}
            ) 
    assert response.status_code == 200, f"Expected 200, got: {response.status_code}"

def reset_password_token(email: str) -> str:
    response = requests.post(
            link.format("reset_password"),
            data = {"email": email}
            )
    assert response.status_code == 200, f"Expected 200, got: {response.status_code}"
    assert response.json() == {"email": email, "reset_token": reset_token}

def update_password(email: str, reset_token: str, new_password: str) -> None:
    response = requests.put(
            link.format("reset_password"),
            data = {"email": email, "reset_token": reset_token, "new_password": new_password}
            )
    assert response.status_code == 200, f"Expected 200, got: {response.status_code}"
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
