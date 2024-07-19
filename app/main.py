from flask import (
    Flask,
    render_template,
    redirect
)
from flask import request

from price_module import PricingModule

# Data structure
emails_pws = {
    "123@g.com": {"pw": "1234", "admin": 1, "match_result": None},#admin
    "321@g.com": {"pw": "1234", "admin": 0, "match_result": None},#volunteer
}
events = []
users = []

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route(rule='/')
@app.route(rule='/login.html')
def home():
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if email in emails_pws:
        if password == emails_pws[email]["pw"] and emails_pws[email]['admin'] == 1:
            return redirect('index_admin.html')
        if password == emails_pws[email]["pw"] and emails_pws[email]['admin'] == 0:
            return redirect('index_volunteers.html')
    return "No user account has been found."

# Create a URL route in our application for "/"
@app.route('/registration.html', methods = ['GET', 'POST', 'DELETE'])
def registration():
    return render_template('registration.html')

@app.route('/register', methods = ['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    emails_pws[email] = {"pw": password, "admin": 0}
    print(email)
    print(password)
    return redirect('login.html')

@app.route('/index_admin.html')
def index_admin():
    return render_template('index_admin.html')

@app.route('/index_volunteers.html')
def index_volunteers():
    email = request.args.get('email')
    volunteer = emails_pws.get(email, None)
    match_result = volunteer.get("match_result") if volunteer else None
    return render_template('index_volunteers.html', match_result=match_result)
    #return render_template('index_volunteers.html')

@app.route('/event_management.html')
def event_management():
    return render_template('event_management.html')


@app.route('/event_management', methods=['POST'])
def create_event():
    event_name = request.form.get('event-name')
    event_description = request.form.get('event-description')
    location = request.form.get('location')
    required_skills = request.form.getlist('required-skills')
    urgency = request.form.get('urgency')
    event_date = request.form.get('event-date')

    new_event = {
        "id": len(events) + 1,
        "name": event_name,
        "description": event_description,
        "location": location,
        "skills": required_skills,
        "urgency": urgency,
        "date": event_date
    }
    print(new_event)

    events.append(new_event)
    return redirect('/event_information.html')

@app.route('/event_information.html')
def event_information():
    return render_template('event_information.html', events=events)

@app.route('/notifications.html')
def notifications():
    return render_template('notifications.html')

@app.route('/profile.html')
def profile():
    return render_template('profile.html')

@app.route('/profile', methods = ['POST'])
def update_profile():
    fullname = request.form.get('full-name')
    address1 = request.form.get('address1')
    address2 = request.form.get('address2')
    city = request.form.get('city')
    state = request.form.get('state')
    zipcode = request.form.get('zip')
    skills = request.form.getlist('skills')
    preferences = request.form.getlist('preferences')
    availability = request.form.get('availability')

    new_user = {

        "fullname": fullname,
        "address1": address1,
        "address2": address2,
        "city": city,
        "state": state,
        "zipcode": zipcode,
        "skills": skills,
        "preferences": preferences,
        "availability": availability
    }
    print(new_user)

    users.append(new_user)
    return "updated successfully"

@app.route('/volunteer_history.html')
def volunteer_history():
    return render_template('volunteer_history.html')

@app.route('/volunteer_matching.html', methods = ['GET'])
def volunteer_matching():
    match_result = None

    for event in events:
        for user in users:
            print(user)
            print(event)
            if (set(event["skills"]).issubset(set(user["skills"])) and
                    event["location"] == user["city"] and
                    event["date"] == user["availability"]):
                match_result = f"Volunteer {user['fullname']} matches the event '{event['name']}' requirements successfully!"
            else:
                match_result = "Volunteer does not match the event requirements."
        #else:
           #match_result = "Volunteer or event not found."
            #emails_pws[volunteer_email]["match_result"] = match_result
    return render_template('volunteer_matching.html', match_result=match_result)


# Instance of PricingModule for future use
pricing_module = PricingModule()



app.run(port=6213)
