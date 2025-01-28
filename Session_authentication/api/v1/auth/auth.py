#!/usr/bin/env python3
""" module with class to manage the API authentication """


from flask import request
from typing import List
from typing import TypeVar
import os


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
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ get the auth user """
        return None
    
    def session_cookie(self, request=None):
        """ returns a cookie from a request """
        if request is None:
            return None

        cookie_name = os.getenv('SESSION_NAME')
        if cookie_name is None:
            return None

        return request.cookies.get(cookie_name)
