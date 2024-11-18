#!/usr/bin/env python3
"""hashing module
"""
import bcrypt


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
