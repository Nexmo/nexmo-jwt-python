# Nexmo Python JWT Generator

[![PyPI version](https://badge.fury.io/py/nexmo-jwt.svg)](https://badge.fury.io/py/nexmo-jwt) [![Python versions supported](https://img.shields.io/pypi/pyversions/nexmo-jwt.svg)](https://pypi.python.org/pypi/nexmo-jwt) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Downloads](https://pepy.tech/badge/nexmo-jwt)](https://pepy.tech/project/nexmo-jwt)

<img src="https://developer.nexmo.com/assets/images/Vonage_Nexmo.svg" height="48px" alt="Nexmo is now known as Vonage" />

Python class to assist with generating JWT tokens for use with the Nexmo API.

Learn more about [Authenticating with JSON Web Tokens](https://developer.nexmo.com/concepts/guides/authentication#json-web-tokens-jwt).

## Installation

To install, run:

```python
pip install nexmo-jwt
```

### Usage

**JWTokenGenerator** is a python class that receives the `application_id` and `private_key` as required parameters in the constructor. Then a token is generated
using the `generate_token()` method.

By default the generated token expires after 15 minutes, but this option can be configured using the `set_expiration_iat` method.

### Generating a JWT

To generate token the **application_id** claim and the **private_key** are required. Using Nexmo Account as an example, you could enter to the Applications section and select a specific application. From there you can copy the application_id and **Generate a new Public key**, And then download the private key file.

### Generating a JWT with Private Key Contents

To generate a JWT with these properties you can use:

```python
from nexmo_jwt import JWTokenGenerator
gen: JWTokenGenerator = JWTokenGenerator('your-application-id','private key contents')
token: bytes = gen.generate_token()
```

### Generating a JWT with Private Key Path

You can also provide a Path to the location of your private key:

```python
from nexmo_jwt import JWTokenGenerator
gen: JWTokenGenerator = JWTokenGenerator('your-application-id','/path/to/your/private.key')
token: bytes = gen.generate_token()
```

### Generating a JWT with Custom Claims

It is also possible to generate a JWT with custom data:

```python
from nexmo_jwt import JWTokenGenerator
gen: JWTokenGenerator = JWTokenGenerator('your-application-id','/path/to/your/private.key')
token: bytes = gen.generate_token(payload={"foo", "bar"})
```
