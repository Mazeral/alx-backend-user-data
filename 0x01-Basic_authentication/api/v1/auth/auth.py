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
        normalized_path = path if path.endswith('/') else path + '/'
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header method
        """
        if request is None:
            return None
        if not request.Authorization:
            return None
        return request.Authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method
        """
        return None
