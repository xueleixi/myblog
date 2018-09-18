from app_test import app
from flask import request

"""
    使用ide运行报错，建议直接python执行
"""

app.testing = True
with app.test_client() as c:
    rv = c.get('/?name=lisi')
    print(request.args)
    print(rv)
    assert b'index' in rv.data
    assert request.args['name'] == 'lisi'

with app.test_request_context('/?name=Peter'):
    assert request.path == '/'
    assert request.args['name'] == 'Peter'

# app.config['TESTING']=True
# c = app.test_client()
# rv = c.get('/')
#
# assert b'index' in rv.data


import unittest


class T(unittest.TestCase):

    def test_get(self):
        app.config['TESTING'] = True
        c = app.test_client()
        rv = c.get('/')
        assert b'index' in rv.data


unittest.main()
