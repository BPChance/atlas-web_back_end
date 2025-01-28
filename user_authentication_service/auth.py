#!/usr/bin/env python3
""" Hash password module """


import bcrypt


def _hash_password(password: str) -> bytes:
    """
    hash a pass using bcrypt and
    return salted hash as bytes
    """
    if not isinstance(password, str):
        raise TypeError("Password must be string")

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
