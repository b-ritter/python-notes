""" Sealed envelope example from Princeton course
'Intro to Crypto and Cryptocurrencies'
https://www.youtube.com/watch?v=fOMVZXLjKYo
"""

import hashlib

def commit(key, msg):
    m = hashlib.sha256()
    m.update(key)
    m.update(msg)
    return {
        "hash": m.hexdigest(),
        "key": key
    }

def verify(com, key, msg):
    v = hashlib.sha256()
    v.update(key)
    v.update(msg)
    try:
        assert v.hexdigest() == com
        return "Message has been verified"
    except:
        raise

sealed_msg = 'there'

key = hashlib.sha256().hexdigest()

msg = commit(key, sealed_msg)

public_msg = msg.get('hash')

print(verify(public_msg, msg.get('key'), sealed_msg))