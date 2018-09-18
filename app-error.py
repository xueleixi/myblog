import werkzeug.exceptions
from flask import Flask, render_template, request, jsonify
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s %(lineno)s %(message)s')

"""
flask错误处理
# http://flask.pocoo.org/docs/0.12/errorhandling/#error-handlers

"""
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


@app.route('/user/<int:id>')
def user(id=12):
    return 'hello %d' % id


# 根据异常类型设置handler
# 捕获所有的异常
# @app.errorhandler(werkzeug.exceptions.NotFound)
# def error_handle(error):
#     logging.info(error)
#     if request.is_xhr:
#         return jsonify({'code': -1, 'msg': 'not found'})
#     else:
#         return 'not found', 404


# app.register_error_handler(404)

@app.errorhandler(werkzeug.exceptions.HTTPException)
def error_handler_http(error):
    logging.info('xx')
    logging.error(error)
    return error, 404


# @app.errorhandler(404)
# def page_not_found(error):
#     logging.info(error)
#     return 'page_not_found', 404


# cookie加密
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.run(debug=True)
