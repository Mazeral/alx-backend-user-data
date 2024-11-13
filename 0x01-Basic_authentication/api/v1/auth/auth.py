#!/usr/bin/env python3
"""Auth model
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class
    """
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        normalized_path = path.rstrip('/')
        normalized_excluded_path = [path.rstrip('/') for path in excluded_paths]
        if normalized_path in normalized_excluded_path:
            return False
        for endpoint in excluded_paths:
            if endpoint.startswith(path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header method
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method
        """
        return None
