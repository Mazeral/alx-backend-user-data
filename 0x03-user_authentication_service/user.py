#!/usr/bin/env python3
"""
This module defines the SQLAlchemy ORM model for the User table.
It handles user-related data including email, hashed password,
session ID, and reset token.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy ORM model for the users table.

    Attributes:
        id (int): The primary key of the user.
        email (str): The user's email address.
        hashed_password (str): The user's hashed password.
        session_id (str | None): The session ID for the user
        (nullable).

        reset_token (str | None): The token used for resetting
        the password (nullable).
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))  # Default nullable=True
    reset_token = Column(String(250))  # Default nullable=True
