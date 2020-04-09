import jwt, sys, time

from uuid import uuid4
from typing import Tuple

if sys.version_info[0] == 3:
    string_types: Tuple = (str, bytes)
    from urllib.parse import urlparse

else:
    string_types: Tuple = (unicode, str)
    from urlparse import urlparse


class JWTokGenException(Exception):
    """Defines exceptions thrown by the Token generator.
    """

    pass


class JWTokenGenerator:
    """
    Generate a JSON Web Token
    """

    application_id: str
    private_key: str
    expiration_from_iat: int

    def __init__(self, application_id: str, private_key: str, expiration=None):
        """
        application_id is a mandatory field.
        expiration by default is 15 minutes (after iat) if not provided. If provided you can pass that as timestamp or datetime
        private_key is mandatory and should be provided as string or as path to private key
        """
        self.application_id = application_id

        self.private_key = private_key

        if self.application_id is None or self.private_key is None:
            raise JWTokGenException(
                u("Error: application_id and private_key are required")
            )

        # If path is found then read the file and assign content to private_key field
        if isinstance(self.private_key, string_types) and "\n" not in self.private_key:
            with open(self.private_key, "rb") as key_file:
                self.private_key = key_file.read()

        # Expiration timestamp or datetime
        self.expiration = expiration

        # when expiration is not provided, this value is used to calculate expiration, by default 450 seconds = 15 minutes
        self.expiration_from_iat = 450

    # change the expiration
    def set_expiration_iat(self, seconds: int):
        self.expiration_from_iat = seconds

    def generate_token(self, payload: dict = {}, issued_at=None) -> bytes:
        # issued_at could be provided here but is optional
        iat: int = int(issued_at if issued_at is not None else time.time())
        # If expiration was provided then use it, if not calculate with de default value
        exp: int = int(self.expiration) if self.expiration is not None else (
            iat + self.expiration_from_iat
        )
        # define the jti
        jti: str = str(uuid4())

        # Preparing the payload
        payload: dict = dict(payload)
        payload.setdefault("application_id", self.application_id)
        payload.setdefault("iat", iat)
        payload.setdefault("exp", exp)
        payload.setdefault("jti", jti)

        return jwt.encode(payload, self.private_key, algorithm="RS256")
