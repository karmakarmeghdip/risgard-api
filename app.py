from flask import Flask
app=Flask(__name__)

users=[{'name': 'Meghdip'}]

@app.route('/api/profile')
def profile():
    return {'data': users}, 200
