#!/usr/bin/env python3
"""Basic auth model
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth class
    """
    pass

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
            # Try to decode the string using base64
            decoded = base64_authorization_header.b64decode(s, validate=True)
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
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        if not (":" in decoded_base64_authorization_header):
            return None
        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, passwor
