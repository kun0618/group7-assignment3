from flask import (
    Flask,
    render_template,
    redirect
)
from flask import request

emails_pws = {
    "123@g.com": {"pw": "1234", "admin": 1},
    "321@g.com": {"pw": "1234", "admin": 0},
}

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
    return render_template('index_volunteers.html')

@app.route('/event_management.html')
def event_management():
    return render_template('event_management.html')

@app.route('/notifications.html')
def notifications():
    return render_template('notifications.html')

@app.route('/profile.html')
def profile():
    return render_template('profile.html')

@app.route('/profile', methods = ['POST'])
def update_profile():
    address1 = request.form.get('address1')
    print(address1)
    return "updated successfully"

@app.route('/volunteer_history.html')
def volunteer_history():
    return render_template('volunteer_history.html')

@app.route('/volunteer_matching.html')
def volunteer_matching():
    return render_template('volunteer_matching.html')

app.run(port=6213)