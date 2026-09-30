# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Teachers can sign students up for activities and unregister them
- Students can browse activities and view participant lists without logging in

## Teacher Access

Teacher accounts are assigned by the school and stored in the local, git-ignored `src/teachers.json` file as salted PBKDF2 password hashes. The expected structure is shown in `src/teachers.example.json`. No teacher passwords are stored in plaintext and there is no public account registration page.

Run `python src/set_teacher_password.py <username>` from the repository root to add or update a teacher account. The script creates `src/teachers.json` if needed and prompts for the password without echoing it. Teacher sessions use an HTTP-only cookie and expire after eight hours. Set `COOKIE_SECURE=true` when serving the app over HTTPS.

## Getting Started

1. Install the dependencies:

   ```
   pip install fastapi uvicorn
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.
