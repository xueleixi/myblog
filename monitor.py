import os
from flask import Flask, request, render_template

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'


@app.route('/')
def index():
    return render_template('/monitor/index.html')


@app.route('/monitor')
def monitor():
    return render_template('/monitor/monitor.html')


@app.route('/upload', methods=['POST'])
def get():
    files = request.files
    file = files['imagefile']
    filename = '1.jpg'
    # os.remove(os.path.join('static', filename))
    # import time
    # time.sleep(30)
    ret = file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print(ret)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
