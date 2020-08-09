import unittest, os
from app.utils.urlparser import url_parse


class AuthorizationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_01_url_parse(self):
        self.assertEqual(url_parse('a.bc'), 'a.bc')
        self.assertEqual(url_parse('a.bc/xyz'), 'a.bc/xyz')
        self.assertEqual(url_parse('a.bc/123'), 'a.bc/{id}')
