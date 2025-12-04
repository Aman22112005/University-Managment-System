# University-Managment-System

## Project Overview
This project is a comprehensive web-based University Management System (UMS) designed to streamline administrative, academic, and operational processes within a university ecosystem. It includes features for managing universities, colleges, students, staff, courses, exams, fees, budgets, libraries, labs, and more. The system supports multiple user roles (students, college admins, university admins) with role-based access control.

The backend is built with Python Flask, using MySQL as the database (based on the provided ER diagram schema). The frontend uses Bootstrap for responsive design, ensuring compatibility across devices. This is an ongoing project aimed at providing a scalable, secure, and user-friendly platform for educational institutions.

## Features
- **User Management**: Registration and login for students, staff, and admins. Role-based permissions (e.g., students can view grades, admins can manage budgets).
- **Academic Management**: Degree programs, subjects, courses, semesters, enrollments, and grade tracking.
- **Student Portal**: View enrolled courses, exam results, fees, library borrows, and credits.
- **Staff Portal**: Manage courses, exams, salaries, and lab equipment.
- **Admin Portal**: Oversee universities, colleges, budgets, expenses, and audit logs.
- **Financials**: Fee management, payments, outstanding fees, salaries, and budgeting.
- **Resources**: Library book management, lab equipment tracking, and borrow records.
- **Auditing & Security**: Audit logs for changes, secure authentication (hashed passwords), and data versioning.
- **Responsive UI**: Mobile-friendly forms and pages using Bootstrap.

## Tech Stack
- **Backend**: Python Flask (web framework), MySQL (database).
- **Frontend**: HTML, CSS, Bootstrap 5 (responsive design).
- **Database**: MySQL with the provided ER diagram schema.
- **Security**: Password hashing (e.g., via Werkzeug), CSRF protection, input validation.
- **Version Control**: Git (hosted on GitHub).
- **Other Tools**: dotenv for environment variables, mysql-connector-python for DB connections.

## Setup Instructions
1. **Prerequisites**:
   - Python 3.8+ installed.
   - MySQL server running.
   - Git for cloning the repo.

2. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/university-management-system.git
   cd university-management-system
   ```

3. **Install Dependencies**:
   ```
   pip install flask mysql-connector-python python-dotenv
   ```

4. **Database Setup**:
   - Create a MySQL database (e.g., `ums_db`).
   - Run the SQL scripts from `db/schema.sql` to create tables based on the ER diagram.
   - Update `.env` file with DB credentials (e.g., DB_HOST, DB_USER, etc.).

5. **Run the Application**:
   ```
   python app.py  # Or flask run
   ```
   - Access at `http://127.0.0.1:5000`.

6. **Production Deployment**:
   - Use Gunicorn: `gunicorn app:app`.
   - Configure Nginx for SSL and reverse proxy.

## Project Structure
```
university-management-system/
├── app.py                 # Main Flask app
├── db/
│   ├── schema.sql         # Database schema
│   └── migrations/        # Future DB updates
├── static/                # CSS, JS, images
├── templates/             # HTML templates (login, register, etc.)
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Contributing
- Fork the repo and create a feature branch.
- Follow PEP 8 for Python code.
- Test changes locally before submitting a PR.
- Report issues via GitHub Issues.

## License
This project is licensed under the MIT License. See LICENSE file for details.

## Progress Checklist
Track development milestones here. Update as you progress.

### Phase 1: Planning & Setup
- [x] Define project scope and features
- [x] Create ER diagram and database schema
- [x] Set up GitHub repository
- [x] Initialize Flask app structure
- [x] Set up MySQL database locally

### Phase 2: Backend Development
- [ ] Implement user authentication (login/register)
- [ ] Create models for all entities (University, Student, etc.)
- [ ] Build API endpoints for CRUD operations
- [ ] Add role-based access control
- [ ] Implement audit logging
- [ ] Secure endpoints (CSRF, validation)

### Phase 3: Frontend Development
- [x] Create login page (HTML/Bootstrap)
- [x] Create registration page (HTML/Bootstrap)
- [ ] Build student dashboard
- [ ] Build admin dashboard
- [ ] Add responsive forms for all entities
- [ ] Integrate JavaScript for dynamic elements

### Phase 4: Features & Integrations
- [ ] Course enrollment and grade management
- [ ] Fee payment system
- [ ] Library and lab management
- [ ] Budget and expense tracking
- [ ] Exam and attempt logging
- [ ] Reporting and analytics

### Phase 5: Testing & Deployment
- [ ] Unit tests for backend
- [ ] UI/UX testing on mobile/desktop
- [ ] Security audit (e.g., SQL injection prevention)
- [ ] Deploy to production server
- [ ] Performance optimization

### Phase 6: Documentation & Maintenance
- [ ] Complete API documentation
- [ ] User manuals for different roles
- [ ] Bug fixes and updates
- [ ] Scale for multiple universities

**Current Status**: In early development. Login/register pages are prototyped. Next: DB setup and basic backend routes.

For questions or updates, contact pradeepgame3@gmail.com or open an issue on GitHub.

by **Aman Singh Bisht**