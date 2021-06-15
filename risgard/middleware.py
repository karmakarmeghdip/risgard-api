from flask import request
from functools import wraps
import firebase_admin

def check_auth(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if not request.headers.get('authorization'):
            return {'error': 'Missing authorization headers'}, 400
        try:
            user = firebase_admin.auth.verify_id_token(
                request.headers.get('authorization')
            )
            request.user = user
        except:
            return {'error': 'Invalid token provided'},400
        return f(*args, **kwargs)
    return wrap


# TODO: fix check_role middleware decorator
#
# def check_role(role, uid):
# 	def wrap(f):
# 		@wrap(f)
# 		def wrapped(*args, **kwargs):
#             # Get user database role
#             user_role=1
#             if role==user_role:
#                 return f(*args, **kwargs)
#             else:
#                 return {'error': 'You do not have sufficient authority level'}
# 	    return wrapped
#     return wrap


"""
[SolverProblemError]
Because no versions of google-cloud-storage match >1.37.1,<1.38.0 || >1.38.0
 and google-cloud-storage (1.37.1) depends on requests (>=2.18.0,<3.0.0dev), google-cloud-storage (>=1.37.1,<1.38.0 || >1.38.0) requires requests (>=2.18.0,<3.0.0dev).
And because google-cloud-storage (1.38.0) depends on requests (>=2.18.0,<3.0.0dev), google-cloud-storage (>=1.37.1) requires requests (>=2.18.0,<3.0.0dev).
Because no versions of firebase-admin match >5.0.0,<6.0.0
 and firebase-admin (5.0.0) depends on google-cloud-storage (>=1.37.1), firebase-admin (>=5.0.0,<6.0.0) requires google-cloud-storage (>=1.37.1).
Thus, firebase-admin (>=5.0.0,<6.0.0) requires requests (>=2.18.0,<3.0.0dev).
And because pyrebase (3.0.27) depends on requests (2.11.1)
 and no versions of pyrebase match >3.0.27,<4.0.0, firebase-admin (>=5.0.0,<6.0.0) is incompatible with pyrebase (>=3.0.27,<4.0.0).
So, because repl-python3-beta-risgard-api depends on both pyrebase (^3.0.27) and firebase-admin (^5.0.0), version solving failed.
exit status 1


Repl.it: Package operation failed.
"""