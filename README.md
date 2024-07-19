# group7-assignment3


Backend Technologies
We chose Python for our backend development due to its simplicity, readability, robust frameworks, extensive libraries, and rapid development speed. More details are provided below:
1. Simplicity and Readability
Ease of Learning and Use: Python's syntax is straightforward and resembles natural language, making it easy to learn and use.
Readability: Python's code readability ensures easier maintenance and debugging.
2. Rich Libraries and Frameworks
Robust Frameworks: We use Flask, which offers flexibility for lighter or microservices-based architectures.
Extensive Libraries: Python's ecosystem includes libraries for data access, manipulation, visualization, and machine learning.
3. Development Speed
Enhanced Productivity: Python's simple syntax and third-party packages provide ready-made solutions, allowing for rapid development and deployment.
Modules Implemented
1. Login Module
Functionality: Handles user authentication, registration, and login.
Details:
Registration: Endpoint to register new users.
Login: Endpoint to authenticate users.
Validation: Ensures email and password strength, along with other necessary validations.
2. User Profile Management Module
Functionality: Manages user profile data, including location, skills, preferences, and availability.
Details:
CRUD Operations: Create, Read, Update, Delete user profiles.
Validation: Ensures required fields like name, email, and location are validated.
3. Event Management Module
Functionality: Creates and manages events.
Details:
Event Creation: Endpoint to create events with details like required skills, location, urgency.
Event Management: CRUD operations for events.
Validation: Validates event details such as date, required skills, and location.
4. Volunteer Matching Module
Functionality: Matches volunteers to events based on profiles and event requirements.
Details:
Matching Logic: Algorithm to match volunteers with events based on skills, availability, and location.
5. Notification Module
Functionality: Sends notifications to volunteers for event assignments, updates, and reminders.
Details:
Notification Types: Email, SMS, or push notifications.
Trigger Points: Event assignments, updates, and reminders.
6. Volunteer History Module
Functionality: Tracks and displays volunteer participation history.
Details:
History Records: Stores and retrieves records of volunteer participation.
Display: Endpoint to fetch and display history data.
7. Pricing Module
Functionality: Creates a class (to be implemented later).
Details:
Pricing Class: Defines the structure and properties.
Usage Instructions
1. Register and Login
Use the default email and password to log in as a volunteer or administrator.
Sample accounts:
Admin account: 123@g.com, password: 1234
Volunteer account: 321@g.com, password: 1234
You can also register a new account and use it to log in.
2. Admin Account Features
1. Event Management:
Input event details on the event_management.html page.
Display event information on the event_information.html page.
2. Event Matching:
Check event matching results.
3. Volunteer Account Features
1. Profile Management:
Edit your profile and print the information in the back end.
