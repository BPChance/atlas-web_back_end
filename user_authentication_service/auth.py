#!/usr/bin/env python3
""" Hash password module """


import bcrypt
from db import DB
from user import User
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

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

    def valid_login(self, email: str, password: str) -> bool:
        """ checks that user login is valid """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return False

        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def _generate_uuid(self) -> str:
        """ return a string representation of a new UUID """
        return str(uuid.uuid4())

    def create_session(self, email: str) -> str:
        """
        find user by email, generate new UUID and store in DB
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return None

        session_id = self._generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id
    
    def get_user_from_session_id(self, session_id: str) -> User:
        """ get user based on session id """
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except Exception:
            return None
