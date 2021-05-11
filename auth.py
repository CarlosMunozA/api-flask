from flask import request
from functools import wraps
import json


def api_key_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        API_KEY = 'hfy92kadHgkk29fahjsu3j922v9sjwaucahf'
        user_key = request.headers.get('x-api-key')
        if user_key is  None:
            return json.dumps({ 'message':'no key' })
        if user_key != API_KEY:
            return json.dumps({ 'message':'invalid key' })
        return f(*args, **kwargs)
    return wrap