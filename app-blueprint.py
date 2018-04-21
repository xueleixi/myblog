from flask import Flask, url_for
from blueprints.admin import admin_page
from blueprints import req,res

app = Flask(__name__)
# app.register_blueprint(simple_page)
app.register_blueprint(req.req_page)
app.register_blueprint(admin_page, url_prefix='/admin')
app.register_blueprint(res.blueprint, url_prefix='/res')

"""
    1. 对请求进行测试
        1.1 获取get参数 => 参数校验
        1.2 获取post参数 
        1.3 json交互
        1.4 文件上传

    2. 对响应进行测试
        2.1 字符串
        2.2 视图渲染
        2.3 json
        2.4 cookie,header
        2.5 下载文件

    3. 数据库访问        

"""


@app.route('/')
def index():
    # url_for('admin.index') # blueprint_name.endpoint
    return ('url:' + url_for('admin.home'))


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
