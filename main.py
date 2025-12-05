from flask import Flask, render_template, request
from Database import get_db_connection

app = Flask(__name__)

conn = get_db_connection()

@app.route("/")
def hello():
    return render_template("loginPage.html")

@app.route('/loginsubmit', methods=['POST'])
def submit():
    try:
        login_type = request.form.get('login_type')
        email = request.form.get('email')
        password = request.form.get('password')
        
        print(f"Login Type: {login_type}, Email: {email}, Password: {password}")
        
        # Ensure a response is always returned
        return "Submitted"
    except Exception as e:
        print(f"Error in submit: {e}")
        return "An error occurred", 500  # Return an error response

@app.route('/register')
def register():
    try:
        return render_template('Register.html')
    except Exception as e:
        print(f"Error: {e}")
        return "An error occured", 500

@app.route('/registersubmit', methods=['POST'])
def registersubmit():
    try:
        Name = request.form.get('Name')
        DOB = request.form.get('DOB')
        email = request.form.get('email')
        Phone = request.form.get('Phone')
        Aadhar = request.form.get('Aadhar')
        Street = request.form.get('Street')
        City = request.form.get('City')
        District = request.form.get('District')
        State = request.form.get('State')
        
        return f"{Name} {DOB} {email} {Phone} {Aadhar} {Street} {City} {District} {State}"
    except Exception as e:
        print(f"Error: {e}")
        return "An error occured", 500

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)