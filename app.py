from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello from python flask'


@app.route('/get')
def get():
    name = request.args.get('name')
    return 'name=%s' % name


if __name__ == '__main__':
    app.run(debug=True,port=8080)





