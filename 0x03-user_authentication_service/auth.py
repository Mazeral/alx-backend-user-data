#!/usr/bin/env python3
"""hashing module
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hashes a plaintext password using bcrypt.

    This method generates a salt and then hashes the given password with
    the salt using bcrypt's hashing algorithm. The resulting hash is returned
    as a byte string.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        bytes: The hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user in the authentication database.

        This method hashes the provided password and adds a new user with
        the given email and hashed password to the database. If a user with
        the same email already exists, a ValueError is raised.

        Args:
            email (str): The email address of the user to register.
            password (str): The plaintext password of the user.

        Returns:
            User: The newly created User object.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is None:
                return self._db.add_user(email, _hash_password(password))
            else:
                raise ValueError(f"User {email} already exists")
        except ValueError as e:
            raise e
            return None
