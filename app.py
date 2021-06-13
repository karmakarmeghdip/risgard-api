from flask import Flask, request
import pyrebase
import firebase_admin
from middleware import check_auth
import os

app = Flask(__name__)

cred = firebase_admin.credentials.Certificate({
    "type":
    "service_account",
    "project_id":
    os.environ.get('PROJECT_ID'),
    "private_key_id":
    os.environ.get('PRIVATE_KEY_ID'),
    "private_key":
    os.environ.get('PRIVATE_KEY'),
    "client_email":
    os.environ.get('CLIENT_EMAIL'),
    "client_id":
    os.environ.get('CLIENT_ID'),
    "auth_uri":
    "https://accounts.google.com/o/oauth2/auth",
    "token_uri":
    "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url":
    "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url":
    os.environ.get('CLIENT_CERT_URL')
})
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app({
    "type":
    "service_account",
    "project_id":
    os.environ.get('PROJECT_ID'),
    "private_key_id":
    os.environ.get('PRIVATE_KEY_ID'),
    "private_key":
    os.environ.get('PRIVATE_KEY'),
    "client_email":
    os.environ.get('CLIENT_EMAIL'),
    "client_id":
    os.environ.get('CLIENT_ID'),
    "auth_uri":
    "https://accounts.google.com/o/oauth2/auth",
    "token_uri":
    "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url":
    "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url":
    os.environ.get('CLIENT_CERT_URL')
})


@app.route('/api/v1/health-check')
def health_check():
    return 'Ok'


@app.route('/api/v1/users')
@check_auth
def profile():
    users = []
    page = firebase_admin.auth.list_users()
    while page:
        for user in page.users:
            users.append(user.uid)
        # Get next batch of users.
        page = page.get_next_page()
    return {'data': users}, 200


@app.route('/api/v1/register')
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email is None or password is None:
            return {'error': 'Missing email or password'}, 400
        try:
            user = firebase_admin.auth.create_user(email=email,
                                                   password=password)
            return {'message': f'Successfully created user {user.uid}'}, 200
        except:
            return {'error': 'User creation failed'}, 400


@app.route('/api/v1/signin')
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email is None or password is None:
            return {'error': 'Missing email or password'}, 400
        try:
            user = pb.auth().sign_in_with_email_and_password(email, password)
            jwt = user['idToken']
            return {'token': jwt}, 200
        except:
            return {'error': 'User signin failed'}, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
