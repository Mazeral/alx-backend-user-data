#!/usr/bin/env python3
"""Basic auth model
"""

from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Basic Auth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts base64 string
            Return None if authorization_header is None

            Return None if authorization_header is not a string

            Return None if authorization_header doesn’t start by Basic
            (with a space at the end)

            Otherwise, return the value after Basic (after the space)
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith("Basic "):
            return authorization_header[6:]
        else:
            return None

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """returns the decoded value of a Base64 string
        base64_authorization_header

        Return None if base64_authorization_header is None
        Return None if base64_authorization_header is not a string
        Return None if base64_authorization_header is not a valid Base64
        Otherwise, return the decoded value as UTF8 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            s = base64_authorization_header
            decoded_bytes = base64.b64decode(s, validate=True)
            decoded = decoded_bytes.decode('utf-8')
            return decoded
        except (base64_authorization_header.binascii.Error, TypeError):
            # If decoding fails, it's not a valid Base64 string
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """Returns the user email and password from Base64

        Return None, None if decoded_base64_authorization_header is None

        Return None, None if decoded_base64_authorization_header is not
        a string

        Return None, None if decoded_base64_authorization_header
        doesn’t contain :

        Otherwise, return the user email and the user password - these 2
        values must be separated by a :"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Return None if user_email is None or not a string

            Return None if user_pwd is None or not a string

            Return None if your database (file) doesn’t contain
            any User instance with email equal to user_email -
            you should use the class method search of the User to
            lookup the list of users based on their email. Don’t forget
            to test all cases: “what if there is no user in DB?”, etc.

            Return None if user_pwd is not the password of the User
            instance found - you must use the method is_valid_password of User
            Otherwise, return the User instance
        """
        if user_email is None or not isinstance(user_email, str) or\
                user_pwd is None or not isinstance(user_pwd, str):
            return None
        users = User.search({"email": user_email})
        if not users:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        else:
            return user

    def current_user(
            self,
            request=None) -> TypeVar('User'):
        """returns the current user if exists
        """
        auth_header = super().authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(
                auth_header)
        if base64_auth_header is None:
            return None

        decoded_header = self.decode_base64_authorization_header(
                base64_auth_header)
        if decoded_header is None:
            return None

        user_creds = self.extract_user_credentials(decoded_header)
        if user_creds is None:
            return None

        user_email, user_pwd = user_creds
        user_obj = self.user_object_from_credentials(user_email, user_pwd)
        return user_obj
