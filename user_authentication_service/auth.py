#!/usr/bin/env python3
""" Hash password module """


import bcrypt
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    
    def register_user(self, email: str, password: str) -> User:
        """ register a user in the DB """
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except Exception:
            pass

        hashed_password = self._hash_password(password)
        new_user = self._db.add_user(email=email, hashed_password=hashed_password)
        return new_user

def _hash_password(self, password: str) -> bytes:
    """
    hash a pass using bcrypt and
    return salted hash as bytes
    """
    if not isinstance(password, str):
        raise TypeError("Password must be string")

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
