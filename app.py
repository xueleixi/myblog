import os
from flask import Flask, request, make_response
from werkzeug.utils import secure_filename

import json
import logging

logging.basicConfig(level=logging.INFO)

UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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


@app.route('/get')
def getParams():
    try:
        size = int(request.args['size'])
        page = int(request.args['page'])
    except ValueError as e:
        return str(e) + '<br>'
    return "size=%d,page=%d" % (size, page)


@app.route('/post', methods=['POST'])
def getFormData():
    name = request.form['name']
    password = request.form['password']
    return "name=%s,password=%s" % (name, password)


@app.route('/json', methods=['POST'])
def getJsonData():
    if request.is_json:
        r = request.get_json()
        print(r)
        response = make_response(json.dumps(r))
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        return json.dumps({'code': 0, 'msg': 'not json form data'})


@app.route('/j')
def response_json():
    r = make_response("hello")
    r.headers['Content-type'] = 'application/json'
    return r


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)

        # check if the post request has the file part
        if 'file' not in request.files:
            # flash('No file part')
            # return redirect(request.url)
            return 'No file part'
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            # flash('No selected file')
            # return redirect(request.url)
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            logging.info("filename1:%s,filename2:%s" % (file.filename, filename))
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            # return redirect(url_for('uploaded_file', filename=filename))
            return "file upload successfully to:" + save_path
    return '''
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
