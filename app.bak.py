from flask import Flask, url_for, request, render_template, session, make_response, abort
import json

from werkzeug.utils import secure_filename, redirect

app = Flask(__name__)


@app.route('/')
def index():
    name=session.get('username')
    if  name:
        return render_template('home.html',username=name)
    else:
        return redirect('login')

# 路由参数
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


# 尾随斜线的区别
@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


# 根据路由生成url
@app.route("/url")
def url():
    url1 = url_for("show_user_profile", username="lisi")
    url2 = url_for("about", p1="p1", p2="p2")
    # 静态文件
    url_for('static', filename='style.css')
    return json.dumps({'url1': url1, 'url2': url2})



# 模板引擎
# 用 Python 生成 HTML 十分无趣，而且相当繁琐，因为你必须手动对 HTML 做转义来保证应用的安全。为此，Flask 配备了 Jinja2 模板引擎。

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # return "Hello {}".format(name)
    return render_template('hello.html', name=name)


# 请求
# 环境局部变量
# request .form[],.args[]
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


def valid_login(name, password):
    return name == password


def log_the_user_in(username):
    if not isinstance(username,str):
        raise TypeError('only support str')
    session.username=username


# 文件上传
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))


# 一个更好的方式是使用延迟请求回调方式 http://docs.jinkan.org/docs/flask/patterns/deferredcallbacks.html#deferred-callbacks
@app.route('/cookie')
def cookie():
    username = request.cookies.get('username')
    # resp = make_response(render_template(...))
    resp = make_response('cookie username=%s' % username)
    resp.set_cookie('username', 'xlx')
    return resp


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
# 响应
# 视图函数的返回值会被自动转换为一个响应对象。如果返回值是一个字符串， 它被转换为该字符串为主体的、状态码为 200 OK``的 、 MIME 类型是 ``text/html 的响应对象。Flask 把返回值转换为响应对象的逻辑是这样：
# 如果返回的是一个合法的响应对象，它会从视图直接返回。
# 如果返回的是一个字符串，响应对象会用字符串数据和默认参数创建。
# 如果返回的是一个元组，且元组中的元素可以提供额外的信息。这样的元组必须是 (response, status, headers) 的形式，且至少包含一个元素。 status 值会覆盖状态代码， headers 可以是一个列表或字典，作为额外的消息标头值。
# 如果上述条件均不满足， Flask 会假设返回值是一个合法的 WSGI 应用程序，并转换为一个请求对象。



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
