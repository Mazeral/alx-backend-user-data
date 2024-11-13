#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    from api.v1.auth.basic_auth import BasicAuth
    from api.v1.auth.auth import Auth

    ba = BasicAuth()
    if not isinstance(ba, Auth):
        print("BasicAuth is not an instance of Auth")
        exit(1)
    
    print("OK", end="")
    
