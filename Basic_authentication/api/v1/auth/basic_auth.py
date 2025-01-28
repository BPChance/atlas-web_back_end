#!/usr/bin/env python3
""" authentication module """


import base64
from .auth import Auth
from typing import Tuple
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth class that
    inherits all methods from Auth
    """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        returns the Base64 part of the
        Authorization header for BasicAuth
        """
        if (
            authorization_header is None
            or not isinstance(authorization_header, str)
        ):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ decodes a base64 str to a utf-8 str """
        if (
            base64_authorization_header is None
            or not isinstance(base64_authorization_header, str)
        ):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> Tuple[str, str]:
        """
        returns the user email and password
        from the Base64 decoded value
        """
        if (
            decoded_base64_authorization_header is None
            or not isinstance(decoded_base64_authorization_header, str)
        ):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        # splitting the str into email and pw
        user_email, user_pw = decoded_base64_authorization_header.split(
            ':', 1)
        return user_email, user_pw

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """ return user email and pw """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
        except KeyError:
            return None

        if not users or len(users) == 0:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user
