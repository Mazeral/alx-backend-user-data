#!/usr/bin/env python3
"""Session auth model
"""
from .auth import Auth


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
        if user_id not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        if user_id in self.user_id_by_session_id:
            self.user_id_by_session_id[user_id].append(session_id)
        else:
            self.user_id_by_session_id[user_id] = session_id
        return session_id
