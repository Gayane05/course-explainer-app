import importlib
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')))

app = importlib.import_module('app').app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Course Explainer', response.data)

    def test_course(self):
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Course Details', response.data)

    def test_contact_status(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_contact_shows_name(self):
        response = self.app.get('/contact')
        self.assertIn(b'Course Explainer Team', response.data)

    def test_contact_shows_email(self):
        response = self.app.get('/contact')
        self.assertIn(b'contact@courseexplainer.com', response.data)

    def test_contact_shows_social_links(self):
        response = self.app.get('/contact')
        self.assertIn(b'GitHub', response.data)
        self.assertIn(b'LinkedIn', response.data)
        self.assertIn(b'Twitter', response.data)

    def test_contact_nav_link_present(self):
        response = self.app.get('/')
        self.assertIn(b'Contact', response.data)


if __name__ == '__main__':
    unittest.main()
