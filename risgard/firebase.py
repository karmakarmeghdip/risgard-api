import firebase_admin
import pyrebase
import os

# Firebase admin account secrets
cred = firebase_admin.credentials.Certificate({
    "type":                         os.environ.get('type'),
    "project_id":                   os.environ.get('project_id'),
    "private_key_id":               os.environ.get('private_key_id'),
    "private_key":                  os.environ.get('private_key').replace('\\n', '\n'),
    "client_email":                 os.environ.get('client_email'),
    "client_id":                    os.environ.get('client_id'),
    "auth_uri":                     os.environ.get('auth_uri'),
    "token_uri":                    os.environ.get('token_uri'),
    "auth_provider_x509_cert_url":  os.environ.get('auth_provider_x509_cert_url'),
    "client_x509_cert_url":         os.environ.get('client_x509_cert_url')
})
firebase = firebase_admin.initialize_app(cred)

# Firebase general account secrets
pb = pyrebase.initialize_app({
    "apiKey":           os.environ.get('apiKey'),
    "authDomain":       os.environ.get('authDomain'),
    "databaseURL":    os.environ.get('databaseURL'),
    "storageBucket":    os.environ.get('storageBucket'),
})