from flask import current_app as app, request
import firebase_admin
from .firebase import pb
from .middleware import check_auth
from . import db

@app.route('/api/v1/health-check')
def health_check():
	return 'Ok'


@app.route('/api/v1/users')
@check_auth
def list_users():
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
		username = request.form.get('username')
		password = request.form.get('password')
		if email is None or username is None or password is None:
			return {'error': 'Missing email, username or password'}, 400
		try:
			user = firebase_admin.auth.create_user(email=email,
			                                       password=password)

			# in case of a successful login we want to create save
			# the username to our database
			# db.session.
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
