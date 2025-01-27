#!/usr/bin/env python3
""" module with class to manage the API authentication """


from flask import request
from typing import List
from typing import TypeVar


User = TypeVar('User')


class Auth:
    """ class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if authentication is required for path """
        return False

    def authorization_header(self, request=None) -> str:
        """ get the auth header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ get the auth user """
        return None
