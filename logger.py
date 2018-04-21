from flask import Flask
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route('/')
def index():
    app.logger.info('abc')
    return 'index'


app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')

app.run(debug=True)
