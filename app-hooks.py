from flask import Flask, g, after_this_request, render_template
import time

app = Flask(__name__)


@app.route('/')
def index():
    @after_this_request
    def add_header(response):
        print("after request over")
        response.headers['X-Foo'] = 'Parachute'
        return response

    print("request")
    return 'Hello World!'


@app.before_request
def detect_user_language():
    print("before request:%s" % time.time())


@app.after_request
def after_req(response):
    print(response)
    print('req over:%s' % time.time())
    return response



if __name__ == '__main__':
    app.run(debug=True)
