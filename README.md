# Tours & Travels - Django Web Application

A full-stack travel booking platform built with Django, featuring tour packages, user bookings, and Stripe integration.

## Features
- **Tour Packages**: Browse various destinations with detailed information.
- **Booking System**: Securely book tours and manage your trips.
- **Stripe Integration**: Simulated payment processing for tour bookings.
- **Admin Dashboard**: Manage tours, users, and bookings easily.

## Tech Stack
- **Backend**: Python / Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite (Production-ready for small scale)
- **Payments**: Stripe API

## Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Tours-And-Travels.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```

## Deployment
This project is optimized for deployment on **PythonAnywhere**. See `env_setup.txt` for required environment variables.
