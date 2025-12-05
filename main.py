from flask import Flask, render_template, request, session
from Database import get_db_connection
import string

app = Flask(__name__)

conn = get_db_connection()

@app.route("/")
def hello():
    return render_template("loginPage.html")


@app.route('/loginsubmit', methods=['POST'])
def submit():
    try:
        login_type = request.form.get('login_type')
        email = request.form.get('email').lower()  # Normalize email
        password = request.form.get('password')
        
        print(f"Login Type: {login_type}, Email: {email}, Password: {password}")
        
        if not all([login_type, email, password]):
            return "All fields are required", 400
        
        conn = get_db_connection()  # Use your custom connection function
        cursor = conn.cursor(dictionary=True)  # Use dictionary cursor for easier access
        
        # Query to fetch user data
        query = "SELECT user_id, email, password_hash, role_id, student_id FROM Users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        

        if user and user['password_hash'] == '000000':  # Direct password check (no encryption)
            # Password matches
            session['user_id'] = user['user_id']
            session['email'] = user['email']
            session['role_id'] = user['role_id']
            session['student_id'] = user['student_id']
            
            if login_type == "student" and user['role_id'] == 1:  # Assuming role_id 1 is student
                query = "SELECT s.name FROM Student s join Users u ON u.sudent_id = s.student_id WHERE id = %s"

                cursor.execute(query, user['user_id'])
                name = cursor.fetchone()
                return "Login successful as Student, Welcome {name[0]}"  # Or redirect as needed
            elif login_type == "admin" and user['role_id'] == 2:  # Assuming role_id 2 is admin
                return "Login successful as Admin"  # Or redirect as needed
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
            conn.close()  # Assuming get_db_connection() returns a connection that needs closing

        


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
        Name = request.form.get('name').upper()
        DOB = request.form.get('DOB')
        email = request.form.get('email').lower()
        Gender = request.form.get('Gender')
        Phone = request.form.get('Phone')
        Aadhar = request.form.get('Aadhar')
        Street = request.form.get('Street').capitalize()
        City = request.form.get('City').capitalize()
        District = request.form.get('District').capitalize()
        State = request.form.get('State').capitalize()

        cursor = conn.cursor()
        query = """
                       INSERT INTO Student(Name,Aadhar,Date_of_Birth,gender,street,city,district,state) values
(%s, %s, %s,"Male", %s, %s, %s, %s);
                       """
        value = (Name, Aadhar,DOB,Street, City,District, State)
        cursor.execute(query, value)
        conn.commit()

        student_id = cursor.lastrowid

        query = """ INSERT INTO Users(email,phone,password_hash,role_id,student_id) values
        (%s, %s, '000000', %s, %s)"""
        value = (email, Phone, 1, student_id)
        cursor.execute(query, value)
        cursor.commit()

        return render_template("loginPage.html")
    except Exception as e:
        print(f"Error: {e}")
        return "An error occured", 500

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)