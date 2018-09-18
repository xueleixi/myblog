from flask import Flask, request,make_response

app = Flask(__name__)

from pprint import pprint


@app.route('/')
def index():
    return 'index'


@app.route('/get')
def get():
    name = request.args.get('name')
    return 'name=%s' % name


@app.route('/login', methods=['POST'])
def login():
    # ImmutableMultiDict 如果请求中没有携带会触发一个（BadRequestKeyError: 400:）异常
    username = request.form['username']
    password = request.form['password']
    pprint(username)
    pprint(password)
    return "login success"


@app.errorhandler(400)
def error_400(e):
    print(e)
    return '400'

@app.route('/connect/')
def redirect():
    return make_response('')


if __name__ == '__main__':
    app.run(debug=True,host='www.myweb.com',port=80)
