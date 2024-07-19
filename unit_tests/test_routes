import unittest
from flask_testing import TestCase
from app import create_app
from app.modules import users, events

class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

class TestUserManagement(BaseTestCase):
    def test_user_registration(self):
        response = self.client.post('/register', json={
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully', response.json['message'])

    def test_user_login(self):
        response = self.client.post('/login', json={
            'username': 'user1',
            'password': 'pass1'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login successful', response.json['message'])

class TestEventManagement(BaseTestCase):
    def test_create_event(self):
        response = self.client.post('/events', json={
            'name': 'New Event',
            'description': 'A new event',
            'location': 'New Location',
            'required_skills': 'New skills',
            'urgency': 'Medium'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Event created successfully', response.json['message'])

if __name__ == '__main__':
    unittest.main()
