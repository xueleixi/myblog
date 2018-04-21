import mimetypes

from flask import Blueprint, render_template, jsonify, send_from_directory, make_response

blueprint = Blueprint('res', __name__)


@blueprint.route('/str')
def echo_str():
    return 'hello word'


@blueprint.route('/template')
def echo_template():
    return render_template('index.html')


@blueprint.route('/json')
def echo_json():
    return jsonify(username='xueleixi',
                   email='xlx@qq.com',
                   id=62)


@blueprint.route('/download')
def echo_download():
    response = make_response("hello! this is a text file")
    # mime_type = mimetypes.guess_type(filename)[0]
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Content-Disposition'] = 'attachment; filename={}'.format('hello.txt')
    return response


@blueprint.route('/uploads/<path:filename>')
def download_file(filename):
    """
    下载静态文件
    :param filename:
    :return:
    """
    # return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    pass
