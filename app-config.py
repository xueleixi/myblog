from flask import Flask
from pprint import pprint
import config

app = Flask(__name__)

app.config['DEBUG'] = True
app.debug = True

app.config.update(
    DEBUG=True,
    # SECRET_KEY='secret',
    # TESTING=True,
    # SERVER_NAME='host:port',
)

app.config.from_object(config.TestingConfig)

# app.run(debug=True)
pprint(app.config)

