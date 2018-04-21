import json, logging

import os
from flask import Blueprint, request, make_response
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

logging.basicConfig(level=logging.INFO)
req_page = Blueprint('req', __name__,
                     template_folder='templates')




@req_page.route('/get')
def getParams():
    try:
        size = int(request.args['size'])
        page = int(request.args['page'])
    except ValueError as e:
        return str(e) + '<br>'
    return "size=%d,page=%d" % (size, page)


@req_page.route('/post', methods=['POST'])
def getFormData():
    name = request.form['name']
    password = request.form['password']
    return "name=%s,password=%s" % (name, password)


@req_page.route('/json', methods=['POST'])
def getJsonData():
    if request.is_json:
        r = request.get_json()
        print(r)
        response = make_response(json.dumps(r))
        response.headers['Content-Type'] = 'req_pagelication/json'
        return response
    else:
        return json.dumps({'code': 0, 'msg': 'not json form data'})


@req_page.route('/j')
def response_json():
    r = make_response("hello")
    r.headers['Content-type'] = 'req_pagelication/json'
    return r


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@req_page.route('/upload', methods=['GET', 'POST'])
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
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(save_path)
            # return redirect(url_for('uploaded_file', filename=filename))
            return "file upload successfully to:" + save_path
    return '''
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
