

---

# Gas Utility Service Application
# Task by Bynry

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Admin Interface](#admin-interface)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

The **Gas Utility Service Application** is a Django-based web platform designed to streamline and manage gas utility services for consumers. The application allows customers to:

- **Submit Service Requests Online:** Easily log issues or request new installations.
- **Track the Status of Requests:** Monitor the progress of their service requests in real-time.
- **View Account Information:** Access and manage their account details securely.

For customer support representatives and administrators, the application provides robust tools to:

- **Manage Service Requests:** View, update, and resolve customer requests efficiently.
- **Provide Support:** Communicate with customers and offer timely assistance.

## Features

### For Customers

- **User Registration & Authentication:**
  - Secure sign-up and login functionalities.
  - Password reset and account management features.

- **Service Request Management:**
  - Submit new service requests with detailed descriptions.
  - View a history of all submitted requests.
  - Track the current status of each request.

- **Account Information:**
  - View account details such as account number and balance.
  - Update personal information.

### For Administrators & Support Representatives

- **Admin Dashboard:**
  - Access all customer service requests.
  - Update the status of requests (e.g., Pending, In Progress, Completed, Cancelled).
  - Search and filter requests based on various criteria.

- **User Management:**
  - Manage customer accounts.
  - Assign roles and permissions to support staff.

## Technologies Used

- **Backend:**
  - [Django](https://www.djangoproject.com/) – Python-based web framework.
  - [PostgreSQL](https://www.postgresql.org/) – Relational database system.

- **Frontend:**
  - [Bootstrap](https://getbootstrap.com/) – CSS framework for responsive design.
  - [HTML5 & CSS3](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) – Markup and styling languages.
  - [JavaScript](https://www.javascript.com/) – Enhancing interactivity.

- **Others:**
  - [Gunicorn](https://gunicorn.org/) – Python WSGI HTTP Server.
  - [Nginx](https://www.nginx.com/) – Web server for serving static files and as a reverse proxy.

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

- **Python 3.12** or later
- **pip** – Python package installer
- **PostgreSQL** – For the production database (optional if using SQLite for development)
- **Git** – Version control system

## Installation

Follow these steps to set up the Gas Utility Service Application on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gas-utility-service.git
cd gas-utility-service
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Ensure you have `pip` updated and install the required packages.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

*If `requirements.txt` is not present, you can create one by running:*

```bash
pip freeze > requirements.txt
```

*Alternatively, install Django directly:*

```bash
pip install django
```

### 4. Configure the Database

By default, Django uses SQLite for development. For production, it's recommended to use PostgreSQL.

#### **Using SQLite (Default for Development)**

No additional configuration is needed. Django will create a `db.sqlite3` file in your project directory.

#### **Using PostgreSQL**

1. **Install PostgreSQL:**

   - [Download PostgreSQL](https://www.postgresql.org/download/) and follow the installation instructions for your operating system.

2. **Create a Database and User:**

   ```bash
   # Access PostgreSQL shell
   psql -U postgres

   # Inside psql shell
   CREATE DATABASE gas_utility_db;
   CREATE USER gas_user WITH PASSWORD 'securepassword';
   ALTER ROLE gas_user SET client_encoding TO 'utf8';
   ALTER ROLE gas_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE gas_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE gas_utility_db TO gas_user;
   \q
   ```

3. **Update `settings.py`:**

   Modify the `DATABASES` section in `gas_utility_service/settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'gas_utility_db',
           'USER': 'gas_user',
           'PASSWORD': 'securepassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

*Follow the prompts to set up an admin account.*

### 7. Collect Static Files

```bash
python manage.py collectstatic
```

*This command collects all static files into the directory specified by `STATIC_ROOT` in `settings.py`.*

## Configuration

### Environment Variables

For security, sensitive information like secret keys and database credentials should be stored as environment variables.

1. **Create a `.env` File:**

   In the root directory of your project, create a `.env` file and add the following:

   ```env
   SECRET_KEY=your_production_secret_key
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

   DB_NAME=gas_utility_db
   DB_USER=gas_user
   DB_PASSWORD=securepassword
   DB_HOST=localhost
   DB_PORT=5432

   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_email_password
   DEFAULT_FROM_EMAIL=no-reply@gasutility.com
   ```

2. **Update `settings.py` to Use Environment Variables:**

   Install `python-decouple` if not already installed:

   ```bash
   pip install python-decouple
   ```

   Modify `gas_utility_service/settings.py`:

   ```python
   from decouple import config
   import os

   SECRET_KEY = config('SECRET_KEY')
   DEBUG = config('DEBUG', default=False, cast=bool)
   ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': config('DB_NAME'),
           'USER': config('DB_USER'),
           'PASSWORD': config('DB_PASSWORD'),
           'HOST': config('DB_HOST'),
           'PORT': config('DB_PORT', default='5432'),
       }
   }

   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = config('EMAIL_HOST')
   EMAIL_PORT = config('EMAIL_PORT', cast=int)
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = config('EMAIL_HOST_USER')
   EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
   DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
   ```

3. **Ensure `.env` is in `.gitignore`:**

   Add `.env` to your `.gitignore` file to prevent it from being pushed to GitHub.

   ```gitignore
   # .gitignore

   # Environment Variables
   .env
   ```

## Running the Application

### Development Server

Start the Django development server:

```bash
python manage.py runserver
```

*Access the application at `http://127.0.0.1:8000/`.*

### Production Server

For deploying to a production environment, consider using Gunicorn and Nginx. Below are high-level steps:

1. **Install Gunicorn:**

   ```bash
   pip install gunicorn
   ```

2. **Start Gunicorn:**

   ```bash
   gunicorn gas_utility_service.wsgi:application --bind 0.0.0.0:8000
   ```

3. **Configure Nginx:**

   Set up Nginx as a reverse proxy to Gunicorn and serve static files.

   ```nginx
   # /etc/nginx/sites-available/gas_utility_service

   server {
       listen 80;
       server_name yourdomain.com www.yourdomain.com;

       location = /favicon.ico { access_log off; log_not_found off; }
       location /static/ {
           root /path/to/your/project;
       }

       location /media/ {
           root /path/to/your/project;
       }

       location / {
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
           proxy_pass http://127.0.0.1:8000;
       }
   }
   ```

4. **Enable the Nginx Server Block and Restart Nginx:**

   ```bash
   sudo ln -s /etc/nginx/sites-available/gas_utility_service /etc/nginx/sites-enabled
   sudo nginx -t  # Test the configuration
   sudo systemctl restart nginx
   ```

5. **Secure with SSL/TLS:**

   Use Certbot to obtain and install SSL certificates.

   ```bash
   sudo apt-get install certbot python3-certbot-nginx
   sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
   ```

## Usage

### Customer Side

1. **Register an Account:**

   - Navigate to the registration page (`http://yourdomain.com/register/`).
   - Fill in the required details and submit the form.

2. **Login:**

   - Access the login page (`http://yourdomain.com/login/`).
   - Enter your credentials to access the dashboard.

3. **Submit a Service Request:**

   - From the dashboard, click on "Submit New Service Request".
   - Fill in the request type and description.
   - Submit the form to log your request.

4. **Track Service Requests:**

   - View all your service requests listed on the dashboard.
   - Click on a specific request to see detailed information and current status.

5. **View Account Information:**

   - Access your account details, including account number and balance, from the dashboard.

### Administrator & CSR Side

1. **Access Admin Interface:**

   - Navigate to the admin panel (`http://yourdomain.com/admin/`).
   - Log in using your superuser or staff credentials.

2. **Manage Service Requests:**

   - View all customer service requests.
   - Update the status of requests (e.g., Pending, In Progress, Completed, Cancelled).

3. **Manage Customers:**

   - Add, edit, or delete customer accounts.
   - View customer details and account information.

## Admin Interface

The Django admin interface provides a comprehensive tool for managing customers and service requests.

### Registering Models in Admin

Ensure that your `admin.py` includes the registration of all necessary models.

```python
# customer_service/admin.py

from django.contrib import admin
from .models import Customer, ServiceRequest

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_number', 'balance')
    search_fields = ('user__username', 'account_number')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'request_type', 'status', 'created_at')
    list_filter = ('status', 'request_type', 'created_at')
    search_fields = ('customer__user__username', 'customer__account_number')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
```

*Customize the `ModelAdmin` classes as needed to enhance the admin interface.*

## Contributing

Contributions are welcome! Follow these steps to contribute to the project:

1. **Fork the Repository:**

   Click the "Fork" button at the top-right corner of the repository page.

2. **Clone Your Fork:**

   ```bash
   git clone https://github.com/yourusername/gas-utility-service.git
   cd gas-utility-service
   ```

3. **Create a New Branch:**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. **Make Your Changes:**

   Implement your feature or fix.

5. **Commit Your Changes:**

   ```bash
   git commit -m "Add feature: YourFeatureName"
   ```

6. **Push to Your Fork:**

   ```bash
   git push origin feature/YourFeatureName
   ```

7. **Create a Pull Request:**

   Go to the original repository and create a pull request from your fork.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or support, please contact:

- **Name:** Your Name
- **Email:** your_email@example.com
- **LinkedIn:** [your-linkedin-profile](https://www.linkedin.com/in/your-profile/)
- **GitHub:** [yourusername](https://github.com/yourusername)

---


## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [PostgreSQL](https://www.postgresql.org/)

---

*Feel free to customize this `README.md` further to better fit the specifics of your project. Including actual paths to images and ensuring all links are correctly set up will enhance the professionalism and usability of your GitHub repository.*