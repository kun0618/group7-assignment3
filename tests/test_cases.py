import unittest
from flask import Flask
from flask.testing import FlaskClient

# Import the application instance
from flask import app, emails_pws, events, users


class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test client and initialize data."""
        cls.client = app.test_client()
        cls.client.testing = True

        # Reset data before each test
        emails_pws.clear()
        events.clear()
        users.clear()

    def test_home_page(self):
        """Test the home and login page."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_login_successful_admin(self):
        """Test login with valid admin credentials."""
        emails_pws['admin@example.com'] = {"pw": "admin123", "admin": 1}
        response = self.client.post('/login', data={'email': 'admin@example.com', 'password': 'admin123'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/index_admin.html')

    def test_login_successful_volunteer(self):
        """Test login with valid volunteer credentials."""
        emails_pws['volunteer@example.com'] = {"pw": "volunteer123", "admin": 0}
        response = self.client.post('/login', data={'email': 'volunteer@example.com', 'password': 'volunteer123'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/index_volunteers.html')

    def test_login_unsuccessful(self):
        """Test login with invalid credentials."""
        response = self.client.post('/login', data={'email': 'unknown@example.com', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No user account has been found.', response.data)

    def test_registration(self):
        """Test user registration."""
        response = self.client.post('/register', data={'email': 'newuser@example.com', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/login.html')
        self.assertIn('newuser@example.com', emails_pws)

    def test_create_event(self):
        """Test event creation."""
        response = self.client.post('/event_management', data={
            'event-name': 'Community Cleanup',
            'event-description': 'A day of cleaning the local park.',
            'location': 'Downtown',
            'required-skills': ['Cleaning', 'Organizing'],
            'urgency': 'High',
            'event-date': '2024-08-01'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/event_information.html')
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]['name'], 'Community Cleanup')

    def test_update_profile(self):
        """Test profile update."""
        response = self.client.post('/profile', data={
            'full-name': 'John Doe',
            'address1': '123 Main St',
            'address2': '',
            'city': 'Somewhere',
            'state': 'CA',
            'zip': '90001',
            'skills': ['First Aid'],
            'preferences': ['Outdoor'],
            'availability': '2024-08-01'
        })
        self.assertEqual(response.data, b'Profile updated successfully')
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['fullname'], 'John Doe')

    def test_volunteer_matching(self):
        """Test volunteer matching logic."""
        emails_pws['volunteer@example.com'] = {"pw": "volunteer123", "admin": 0}
        users.append({
            'fullname': 'Jane Smith',
            'city': 'Downtown',
            'skills': ['Cleaning'],
            'availability': '2024-08-01'
        })
        events.append({
            'name': 'Community Cleanup',
            'skills': ['Cleaning'],
            'location': 'Downtown',
            'date': '2024-08-01'
        })

        response = self.client.get('/volunteer_matching.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Volunteer Jane Smith matches the event', response.data)


if __name__ == '__main__':
    unittest.main()
