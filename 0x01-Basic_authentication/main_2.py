#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    from api.v1.auth.basic_auth import BasicAuth

    ba = BasicAuth()
    res = ba.decode_base64_authorization_header("NopBase64")
    if res is not None:
        print("decode_base64_authorization_header must return None if 'base64_authorization_header' is not a base64 string")
        exit(1)
    
    print("OK", end="")
