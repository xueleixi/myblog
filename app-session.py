from flask import Flask, session, request, make_response
from pprint import pprint

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a'



@app.route('/')
def index():
    if session.get('username'):
        return 'hello %s' % session['username']
    return 'hello stranger'


@app.route('/login/<username>')
def login(username):
    session['username'] = username
    return '%s logged in' % username


@app.route('/cookie')
def cookie():
    r = make_response('set cookie')

@app.before_request
def print_session():
    pprint(session)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
