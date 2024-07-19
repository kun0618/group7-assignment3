import unittest
from app.main import app, emails_pws, events, users
from app.price_module import PricingModule

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

        # Reset the data to ensure test isolation
        global emails_pws, events, users
        emails_pws = {
            "123@g.com": {"pw": "1234", "admin": 1, "match_result": None},
            "321@g.com": {"pw": "1234", "admin": 0, "match_result": None},
        }
        events = []
        users = []

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_login_page(self):
        response = self.client.get('/login.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email:', response.data)
        self.assertIn(b'Password:', response.data)
        self.assertIn(b'Login', response.data)
        self.assertIn(b'Register here', response.data)

    def test_successful_login_admin(self):
        response = self.client.post('/login', data={
            'email': '123@g.com',
            'password': '1234'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/index_admin.html')

    def test_successful_login_volunteer(self):
        response = self.client.post('/login', data={
            'email': '321@g.com',
            'password': '1234'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/index_volunteers.html')

    def test_failed_login(self):
        response = self.client.post('/login', data={
            'email': 'nonexistent@g.com',
            'password': 'wrong'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No user account has been found.', response.data)

    def test_registration_page(self):
        response = self.client.get('/registration.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email:', response.data)
        self.assertIn(b'Password:', response.data)
        self.assertIn(b'Register', response.data)

    def test_registration(self):
        response = self.client.post('/register', data={
            'email': 'newuser@g.com',
            'password': 'newpass'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/login.html')

    def test_event_management_page(self):
        response = self.client.get('/event_management.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Event Name:', response.data)
        self.assertIn(b'Event Description:', response.data)
        self.assertIn(b'Location:', response.data)
        self.assertIn(b'Required Skills:', response.data)
        self.assertIn(b'Urgency:', response.data)
        self.assertIn(b'Event Date:', response.data)

    def test_create_event(self):
        response = self.client.post('/event_management', data={
            'event-name': 'Test Event',
            'event-description': 'Description of test event',
            'location': 'Test Location',
            'required-skills': ['skill1', 'skill2'],
            'urgency': 'medium',
            'event-date': '2024-12-31'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/event_information.html')

    def test_event_information_page(self):
        response = self.client.get('/event_information.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Event Information', response.data)
        self.assertIn(b'No events available.', response.data)

        self.client.post('/event_management', data={
            'event-name': 'Test Event',
            'event-description': 'Description of test event',
            'location': 'Test Location',
            'required-skills': ['skill1', 'skill2'],
            'urgency': 'medium',
            'event-date': '2024-12-31'
        })
        response = self.client.get('/event_information.html')
        self.assertIn(b'Test Event', response.data)
        self.assertIn(b'Description of test event', response.data)

    def test_profile_page(self):
        response = self.client.get('/profile.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Full Name:', response.data)
        self.assertIn(b'Address 1:', response.data)
        self.assertIn(b'Address 2:', response.data)
        self.assertIn(b'City:', response.data)
        self.assertIn(b'State:', response.data)
        self.assertIn(b'Zip Code:', response.data)
        self.assertIn(b'Skills:', response.data)
        self.assertIn(b'Preferences:', response.data)
        self.assertIn(b'Availability:', response.data)

    def test_update_profile(self):
        response = self.client.post('/profile', data={
            'full-name': 'John Doe',
            'address1': '123 Main St',
            'address2': 'Apt 4B',
            'city': 'Springfield',
            'state': 'TX',
            'zip': '12345',
            'skills': ['skill1', 'skill2'],
            'preferences': 'None',
            'availability': '2024-07-19'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'updated successfully', response.data)

    def test_volunteer_matching_page(self):
        response = self.client.get('/volunteer_matching.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Match Result', response.data)

        self.client.post('/event_management', data={
            'event-name': 'Test Event',
            'event-description': 'Description of test event',
            'location': 'Springfield',
            'required-skills': ['skill1', 'skill2'],
            'urgency': 'medium',
            'event-date': '2024-07-19'
        })

        self.client.post('/profile', data={
            'full-name': 'John Doe',
            'address1': '123 Main St',
            'address2': 'Apt 4B',
            'city': 'Springfield',
            'state': 'TX',
            'zip': '12345',
            'skills': ['skill1', 'skill2'],
            'preferences': 'None',
            'availability': '2024-07-19'
        })

        response = self.client.get('/volunteer_matching.html')
        self.assertIn(b"Volunteer John Doe matches the event 'Test Event' requirements successfully!", response.data)

if __name__ == '__main__':
    unittest.main()
