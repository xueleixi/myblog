import os
from flask import Flask, request, render_template
from PIL import Image

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
    filename = 'big.jpg'
    # os.remove(os.path.join('static', filename))
    # import time
    # time.sleep(30)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    small_file_path = os.path.join(app.config['UPLOAD_FOLDER'], "1.jpg")

    ret = file.save(file_path)
    smallImage = Image.new('RGB', (640, 640))

    img = Image.open(file_path)
    img = img.resize((640, 640), Image.ANTIALIAS)
    smallImage.paste(img, (0, 0))
    smallImage.save(small_file_path, "JPEG")
    print(ret)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
