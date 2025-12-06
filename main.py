from flask import Flask, render_template, request, session, flash, redirect, url_for
from Database import get_db_connection
import string
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32) #------Generate Secret Key, Needed for Session[]-------


@app.route("/")
def hello():
    return redirect("/login")


@app.route("/login")
def login():
    return render_template("loginPage.html")


@app.route('/loginsubmit', methods=['POST'])
def submit():
    conn = None
    cursor = None
    try:
        login_type = request.form.get('login_type')
        email = request.form.get('email').lower()  # Normalize email
        password = request.form.get('password')
        
        print(f"Login Type: {login_type}, Email: {email}, Password: {password}")
        
        if not all([login_type, email, password]):
            return "All fields are required", 400
        
        conn = get_db_connection()  # Use custom connection function from database.py
        if not conn:
            return f"Database Connection Failed", 500
        cursor = conn.cursor(dictionary=True)  # Use dictionary cursor for easier access
        
        # Query to fetch user data
        query = "SELECT user_id, email, password_hash, role_id, student_id FROM Users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        

        if user and user['password_hash'] == '000000':  # -------Default Password Need Update-------
            # Password matches
            session['user_id'] = user['user_id']
            session['email'] = user['email']
            session['role_id'] = user['role_id']
            session['student_id'] = user['student_id']
            print(f"Userid: {type(user['student_id'])} {user['student_id']}")
            
            if login_type == "student" and user['role_id'] == 1:  # role_id 1 is student
                query = "SELECT s.name FROM Student s join Users u ON u.student_id = s.student_id WHERE u.user_id = %s"

                cursor.execute(query, (user['user_id'],))
                name = cursor.fetchone()
                if name:
                    return f"Login successful as Student, Welcome {name['name']}"  # -----required update for admin dashboard in Future-----
            elif login_type == "admin" and user['role_id'] == 2:  # --------Assuming role_id 2, need update in future --------
                return "Login successful as Admin"  # -----required update for admin dashboard in Future-----
            else:
                return "Invalid login type for this user", 403
        else:
            return "Invalid email or password", 401
        
    except Exception as e:
        print(f"Error in submit: {e}")
        return "An error occurred", 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()  # Closes the connection

        


@app.route('/register')
def register():
    try:
        return render_template('Register.html')
    except Exception as e:
        print(f"Error: {e}")
        return "An error occured", 500


@app.route('/registersubmit', methods=['POST'])
def registersubmit():
    conn = None
    cursor = None
    try:
        # Get and validate form data
        Name = request.form.get('name', '').strip().upper()
        DOB = request.form.get('DOB', '').strip()
        email = request.form.get('email', '').strip().lower()
        Gender = request.form.get('Gender', '').strip()
        Phone = request.form.get('Phone', '').strip()
        Aadhar = request.form.get('Aadhar', '').strip()
        Street = request.form.get('Street', '').strip().capitalize()
        City = request.form.get('City', '').strip().capitalize()
        District = request.form.get('District', '').strip().capitalize()
        State = request.form.get('State', '').strip().capitalize()
        
        # Basic validation
        if not all([Name, DOB, email, Phone, Aadhar, Street, City, District, State]):
            return "All fields are required", 400
        
        conn = get_db_connection()  # Use your custom connection function
        if not conn:
            return f"Database Connection Failed", 500
       
        # Get connection
        cursor = conn.cursor(dictionary=True)  # Enable dict results
        
        # Check for existing email
        cursor.execute("SELECT email FROM Users WHERE email = %s", (email,))
        if cursor.fetchone():
            return "Email already exists", 409
        
        # Insert into Student
        query_student = """
            INSERT INTO Student (Name, Aadhar, Date_of_Birth, gender, street, city, district, state)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_student, (Name, Aadhar, DOB, Gender, Street, City, District, State))
        conn.commit()
        
        student_id = cursor.lastrowid
        
        # Insert into Users
        query_users = """
            INSERT INTO Users (email, phone, password_hash, role_id, student_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query_users, (email, Phone, "000000", 1, student_id))
        conn.commit()
        
        # Success response
        return render_template("registration_success.html")
    
    except Exception as e:
        print(f"Error: {str(e)}")  # Secure logging
        conn.rollback()  # Rollback on error
        return "An error occurred", 500
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


@app.route("/registration_success")
def registration_success():
    return redirect(url_for("login"))

            
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)            # Password matches
