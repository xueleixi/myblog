import unittest
from app_test import app
from pprint import pprint
from flask import request


class AppTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def testRoute(self):
        pass

    def test_empty_db(self):
        rv = self.app.get('/')
        pprint(rv.__dict__)
        pprint(rv.data)
        assert b'index' in rv.data

    def test_login(self):
        rv = self.app.post('/login', data=dict(username='john', password='123'), follow_redirects=True)
        self.assertIn(b'success', rv.data)

if __name__ == '__main__':
    unittest.main()
