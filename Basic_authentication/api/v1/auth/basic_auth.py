#!/usr/bin/env python3
""" authentication module """


from .auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class that
    inherits all methods from Auth
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header for BasicAuth """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]
