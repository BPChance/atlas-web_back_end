#!/usr/bin/env python3
""" Encrypting passwords """


import bcrypt


def hash_password(password: str) -> bytes:
    """ function that salt and hash pass """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed
