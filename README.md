# SplitWise

## Local Virtual Environment Setup

1. **Install Python version 3.11.4**:
   To ensure compatibility, install Python version 3.11.4 using pyenv:
   ```bash
   pyenv install 3.11.4
   ```

2. **Create and activate a virtual environment**:
   Create a new virtual environment and activate it:
   ```bash
   pyenv virtualenv 3.11.4 splitwise-3.11.4
   pyenv activate splitwise-3.11.4
   ```

---

## Install Requirements

To install all the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

---

## Database Settings

Make sure to update or add your database details directly in `settings.py`.  
**Note**: This will be moved to a `.env` file in a future version for better security.

---

## Run Migrations

Apply all necessary database migrations by running:
```bash
python manage.py migrate
```

---

## Run the Application

Start the development server using:
```bash
python manage.py runserver
```

---

## Features

- **JWT Token Authentication**: For secure API access.
- **Custom User Model**: User authentication and management.
- **Currency Model**: Manages multiple currencies for user transactions.
- **Expenses Model**: Allows users to track and manage their expenses.

---
