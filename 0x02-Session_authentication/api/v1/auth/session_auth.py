#!/usr/bin/env python3
"""Session auth model
"""
from .auth import Auth
import uuid
from typing import TypeVar


class SessionAuth(Auth):
    """SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(
            self,
            user_id: str = None
            ) -> str:
        """Creating a session for the user
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(
            self,
            session_id: str = None
            ) -> str:
        """returns a User ID based on a Session ID
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns a User instance based on a cookie value
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        user = User.get(user_id)
        if user is None:
            return None
        return user
