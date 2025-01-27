#!/usr/bin/env python3
""" Encrypting passwords """


import bcrypt


def hash_password(password: str) -> bytes:
    """ function that salt and hash pass """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ checks if password matches """
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
