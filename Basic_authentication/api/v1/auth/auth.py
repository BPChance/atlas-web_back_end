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
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        normalized_path = path if path.endswith('/') else path + '/'
        return normalized_path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ get the auth header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ get the auth user """
        return None
