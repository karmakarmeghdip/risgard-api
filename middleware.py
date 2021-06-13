from flask import request
from functools import wraps
import firebase_admin

def check_auth(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if not request.headers.get('authorization'):
            return { 'error': 'Missing authorization headers' }, 400
        try:
            user = firebase_admin.auth.verify_id_token(
                request.headers.get('authorization')
            )
            request.user = user
        except:
            return { 'error': 'Invalid token provided' },400
        return f(*args, **kwargs)
    return wrap