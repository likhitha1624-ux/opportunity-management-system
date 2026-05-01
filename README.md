# Opportunity Management System

## Project Overview

This project is a full stack admin dashboard where admins can manage opportunities in a simple and structured way. I built the backend using Flask and connected it with the frontend to make the application fully functional.

Admins can sign up, log in, and manage their own opportunities. The system supports creating, viewing, editing, and deleting opportunities. All data is handled through backend APIs, and each admin can access only their own data.

The project also includes a secure forgot password feature using time-based reset tokens.

---

## Features

### Authentication

* Admin signup with validation
* Admin login with error handling
* Forgot password with secure reset link (1-hour expiry)

---

### Opportunity Management

* View all opportunities created by the logged-in admin
* Add new opportunities with validation
* Edit opportunities
* Delete opportunities with confirmation
* View full opportunity details

---

## Tech Stack

* Backend: Python, Flask
* Frontend: HTML, CSS, JavaScript
* API Communication: Fetch API
* Data Storage: In-memory

---

## Requirements

Make sure you have the following installed:

* Python (3.8 or above)
* pip (Python package manager)
* Web browser (Chrome recommended)

---

## Installation

Install required Python packages:

```bash id="kz3y7w"
pip install flask flask-cors
```

---

## How to Run the Project

### Step 1: Clone the Repository

```bash id="6y5r1k"
git clone https://github.com/liki/opportunity-management-system.git
cd opportunity-management-system
```

---

### Step 2: Start Backend

```bash id="9w2z1m"
cd backend
python app.py
```

You should see:

```id="v1z8xt"
Running on http://127.0.0.1:5000
```

---

### Step 3: Start Frontend

```bash id="3d0s8p"
cd sky
python -m http.server 5500
```

---

### Step 4: Open in Browser

http://127.0.0.1:5500/admin.html

---

## How It Works

* User signs up and logs in
* Dashboard loads user-specific data
* Opportunities are fetched from backend
* All operations (add, edit, delete) happen via API
* UI updates instantly without page refresh

---

## Notes

* Data resets when the backend server restarts
* Each admin can access only their own data

---

## Author

Likhitha

