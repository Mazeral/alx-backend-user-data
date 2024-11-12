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
