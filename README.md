# Online Store - Django Project

## Overview

**Online Store** is a web-based e-commerce platform built using Django. The platform allows users to browse items, create new items, engage in conversations about items, and manage personal accounts with features such as signing up, logging in, and logging out. The project also supports role-based authentication.

## Features

- User Authentication (Signup, Login, Logout)
- Browse and add new items for sale
- Item-based conversations (buyer/seller messaging)
- User dashboard to manage items and conversations
- Responsive design using Tailwind CSS
- Admin panel for easy management

## Technologies Used

- **Backend**: Django 5.1.1 (Python)
- **Frontend**: HTML, CSS (Tailwind CSS)
- **Database**: SQLite (default Django DB)
- **Version Control**: Git
- **Other**: Django Admin

## Installation and Setup

### Prerequisites

- Python 3.10 or higher
- Git
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/Bettinalisah/OnlineStore.git
    ```

2. Navigate to the project directory:

    ```bash
    cd OnlineStore
    ```

3. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    On Windows: venv\Scripts\activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run database migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser for accessing the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your browser and go to `http://127.0.0.1:8000/` to see the application.

## Usage

- Users can register, log in, and log out.
- Logged-in users can browse, add, and message item owners.
- Admins can manage items, users, and messages through the Django admin panel.

## File Structure

![Website Screenshot](images/IMG_7550.jpg)

