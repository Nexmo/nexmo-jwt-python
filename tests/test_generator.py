from unittest import TestCase
from nexmo_jwt import JWTokenGenerator


class nexmojwtest(TestCase):

    # Failure scenario - invalid constructor, this test pass because expected error found
    def test_invalid_constructor(self):
        try:
            JWTokenGenerator()
            self.assertTrue(False)
        except TypeError as e:
            # print(str(e))
            self.assertTrue(
                str(e)
                == "__init__() missing 2 required positional arguments: 'application_id' and 'private_key'"
            )

    # Failure scenarios - invalid private key path. The test pass when invalid path is passed to constructor
    def test_invalid_private_key_path(self):
        try:
            JWTokenGenerator("valid-application-id", "invalid-private-key-path")
            self.assertTrue(False)
        except FileNotFoundError as e:
            # print(str(e))
            self.assertTrue(
                "No such file or directory: 'invalid-private-key-path'" in str(e)
            )

    # Failure scenarios - This test pass when generator retrieves a deserialize key data error
    def test_invalid_generation_with_private_key_contents(self):
        try:
            fake_application_id = "0x4ab4x1-abc8-4xx8-a46a-6xx14x5fabc6"
            fake_private_key = "invalid\nprivate\nkey"
            generator = JWTokenGenerator(fake_application_id, fake_private_key)
            token = generator.generate_token()
        except ValueError as e:
            self.assertTrue("Could not deserialize key data" in str(e))

    # Success scenario, the test pass when generator retrieves a token
    def test_valid_generation_with_private_key_contents(self):
        fake_application_id = "0x4ab4x1-abc8-4xx8-a46a-6xx14x5fabc6"
        fake_private_key = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDQdAHqJHs/a+Ra
2ubvSd1vz/aWlJ9BqnMUtB7guTlyggdENAbleIkzep6mUHepDJdQh8Qv6zS3lpUe
K0UkDfr1/FvsvxurGw/YYPagUEhP/HxMbs2rnQTiAdWOT+Ux9vPABoyNYvZB90xN
IVhBDRWgkz1HPQBRNjFcm3NOol83h5Uwp5YroGTWx+rpmIiRhQj3mv6luk102d95
4ulpPpzcYWKIpJNdclJrEkBZaghDZTOpbv79qd+ds9AVp1j8i9cG/owBJpsJWxfw
StMDpNeEZqopeQWmA121sSEsxpAbKJ5DA7F/lmckx74sulKHX1fDWT76cRhloaEQ
VmETdj0VAgMBAAECggEAZ+SBtchz8vKbsBqtAbM/XcR5Iqi1TR2eWMHDJ/65HpSm
+XuyujjerN0e6EZvtT4Uxmq8QaPJNP0kmhI31hXvsB0UVcUUDa4hshb1pIYO3Gq7
Kr8I29EZB2mhndm9Ii9yYhEBiVA66zrNeR225kkWr97iqjhBibhoVr8Vc6oiqcIP
nFy5zSFtQSkhucaPge6rW00JSOD3wg2GM+rgS6r22t8YmqTzAwvwfil5pQfUngal
oywqLOf6CUYXPBleJc1KgaIIP/cSvqh6b/t25o2VXnI4rpRhtleORvYBbH6K6xLa
OWgg6B58T+0/QEqtZIAn4miYtVCkYLB78Ormc7Q9ewKBgQDuSytuYqxdZh/L/RDU
CErFcNO5I1e9fkLAs5dQEBvvdQC74+oA1MsDEVv0xehFa1JwPKSepmvB2UznZg9L
CtR7QKMDZWvS5xx4j0E/b+PiNQ/tlcFZB2UZ0JwviSxdd7omOTscq9c3RIhFHar1
Y38Fixkfm44Ij/K3JqIi2v2QMwKBgQDf8TYOOmAr9UuipUDxMsRSqTGVIY8B+aEJ
W+2aLrqJVkLGTRfrbjzXWYo3+n7kNJjFgNkltDq6HYtufHMYRs/0PPtNR0w0cDPS
Xr7m2LNHTDcBalC/AS4yKZJLNLm+kXA84vkw4qiTjc0LSFxJkouTQzkea0l8EWHt
zRMv/qYVlwKBgBaJOWRJJK/4lo0+M7c5yYh+sSdTNlsPc9Sxp1/FBj9RO26JkXne
pgx2OdIeXWcjTTqcIZ13c71zhZhkyJF6RroZVNFfaCEcBk9IjQ0o0c504jq/7Pc0
gdU9K2g7etykFBDFXNfLUKFDc/fFZIOskzi8/PVGStp4cqXrm23cdBqNAoGBAKtf
A2bP9ViuVjsZCyGJIAPBxlfBXpa8WSe4WZNrvwPqJx9pT6yyp4yE0OkVoJUyStaZ
S5M24NocUd8zDUC+r9TP9d+leAOI+Z87MgumOUuOX2mN2kzQsnFgrrsulhXnZmSx
rNBkI20HTqobrcP/iSAgiU1l/M4c3zwDe3N3A9HxAoGBAM2hYu0Ij6htSNgo/WWr
IEYYXuwf8hPkiuwzlaiWhD3eocgd4S8SsBu/bTCY19hQ2QbBPaYyFlNem+ynQyXx
IOacrgIHCrYnRCxjPfFF/MxgUHJb8ZoiexprP/FME5p0PoRQIEFYa+jVht3hT5wC
9aedWufq4JJb+akO6MVUjTvs
-----END PRIVATE KEY-----"""
        generator = JWTokenGenerator(fake_application_id, fake_private_key)
        token = generator.generate_token()
        assert isinstance(token, bytes)

    # Success scenario, the test pass when generator retrieves a token
    def test_valid_generation_with_private_key_path(self):
        fake_application_id = "0x4ab4x1-abc8-4xx8-a46a-6xx14x5fabc6"
        fake_private_key = "nexmojwt/tests/private_key.txt"
        generator = JWTokenGenerator(fake_application_id, fake_private_key)
        token = generator.generate_token()
        assert isinstance(token, bytes)
