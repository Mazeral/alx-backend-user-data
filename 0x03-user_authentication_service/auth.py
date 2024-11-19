#!/usr/bin/env python3
"""hashing module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


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


def _generate_uuid() -> str:
    """
    Generates a new UUID (Universally Unique Identifier) as a string.

    This function creates a version 4 UUID, which is randomly generated,
    and converts it to a string representation.

    Returns:
        str: A string representation of the generated UUID.
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates a user's login credentials.

        This method checks whether the provided email and password match a user
        record in the database. The password is verified against the stored
        hashed password using bcrypt.

        Args:
            email (str): The email address of the user attempting to log in.
            password (str): The plaintext password provided by the user.

        Returns:
            bool: True if the credentials are valid (email exists and password
                  matches), False otherwise.

        Raises:
            NoResultFound: If no user with the specified email is found in the
                           database.
        """
        try:
            # Fetch the user by email from the database
            user = self._db.find_user_by(email=email)

            # Check if the user exists and verify the password
            if user is not None:
                password_bytes = password.encode('utf-8')  # Convert to bytes
                if bcrypt.checkpw(password_bytes, user.hashed_password):
                    return True
            return False
        except NoResultFound:
            # Return False if no user is found
            return False

    def create_session(self, email: str) -> str:
        """
        Creates a new session for a user and saves it in the database.

        This method generates a unique session ID for a user identified by
        their email, assigns it to the user's `session_id` field, and commits
        the change to the database. The generated session ID is then returned.

        Args:
            email (str): The email address of the user for whom the session is
                         being created.

        Returns:
            str: The generated session ID.

        Raises:
            Exception: If an error occurs while querying the database or
            updating the user's session information.
        """
        try:
            # Find the user by email
            user = self._db.find_user_by(email=email)

            # Generate a unique session ID
            session_id = _generate_uuid()

            # Assign the session ID to the user
            user.session_id = session_id

            # updates the user
            session_dict = {"session_id": session_id}
            self._db.update_user(user.id, **session_dict)

            # Return the generated session ID
            return session_id
        except Exception as e:
            # Raise any exception that occurs
            raise e
