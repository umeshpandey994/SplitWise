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

### **Users API Endpoints Overview**:
- **POST /users/**: Create a new user.
- **GET /users/**: Retrieve a list of all users.
- **GET /users/{id}**: Retrieve a specific user by their ID.
- **PUT /users/{id}**: Fully update a specific user's details.
- **PATCH /users/{id}**: Partially update a specific user's details.
- **DELETE /users/{id}**: Delete a specific user.

This structure provides clear examples for all CRUD operations on the `Users API`.


POST endpoint

```bash
curl -X POST http://127.0.0.1:8000/api/v1/users/ \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMDc1OTc2LCJpYXQiOjE3MzE5ODk1NzYsImp0aSI6IjhmYTAwZWI5NDQ2NTQ3MTE4MTNlYTE0ZWE1YTBhNmMxIiwidXNlcl9pZCI6NH0.knFr125bYhGpg9YwipCvUy2ezZGBuj0tmVx6gAeFnlQ" \
-H "Content-Type: application/json" \
-d '{"username": "hema", "password": "admin@123", "phone_number": "1734567890"}'
```

GET endpoint
```bash
curl -X GET  http://127.0.0.1:8000/api/v1/users/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMDc1OTc2LCJpYXQiOjE3MzE5ODk1NzYsImp0aSI6IjhmYTAwZWI5NDQ2NTQ3MTE4MTNlYTE0ZWE1YTBhNmMxIiwidXNlcl9pZCI6NH0.knFr125bYhGpg9YwipCvUy2ezZGBuj0tmVx6gAeFnlQ"
```

GET /users/{id}
```bash
curl -X GET http://127.0.0.1:8000/api/v1/users/1/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <token>"
```

PUT /users/{id}
```bash
curl -X PUT http://127.0.0.1:8000/api/v1/users/1/ \
-H "Authorization: Bearer <>" \
-H "Content-Type: application/json" \
-d '{"username": "umesh2", "email": "umesh3@example.com", "phone_number": "9870543210"}'
```

PATCH /users/{id}

```bash
curl -X PATCH http://127.0.0.1:8000/api/v1/users/1/ \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{"email": "umesh.pan@ss.com"}'
```

DELETE /users/{id}

```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/users/1/ \
-H "Authorization: Bearer <token>"
```

### **Currency API Endpoints Overview**:
- **POST /currency/**: Add a new currency.
- **GET /currency/**: Retrieve a list of all currency.


```bash
curl -X POST http://localhost:8000/api/v1/currency/ \
  -H "Content-Type: application/json" \
  -d '{"name": "INR"}' \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMDc1OTc2LCJpYXQiOjE3MzE5ODk1NzYsImp0aSI6IjhmYTAwZWI5NDQ2NTQ3MTE4MTNlYTE0ZWE1YTBhNmMxIiwidXNlcl9pZCI6NH0.knFr125bYhGpg9YwipCvUy2ezZGBuj0tmVx6gAeFnlQ"
```

```bash
curl -X GET http://localhost:8000/api/v1/currency/
```


### **Expenses API Endpoints Overview**:
- **POST /expenses/**: Add a new expenses.
- **GET /expenses/**: Retrieve a list of all expenses.


    split_method_map = {
        "equal": EqualSplit,
        "fixed": FixedSplit,
        "percentage": PercentageSplit,
    }


```bash
curl -X GET http://localhost:8000/api/v1/expenses/ \
    -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMDc1OTc2LCJpYXQiOjE3MzE5ODk1NzYsImp0aSI6IjhmYTAwZWI5NDQ2NTQ3MTE4MTNlYTE0ZWE1YTBhNmMxIiwidXNlcl9pZCI6NH0.knFr125bYhGpg9YwipCvUy2ezZGBuj0tmVx6gAeFnlQ"
```

```bash
curl -X POST http://localhost:8000/api/v1/expenses/ \
  -H "Content-Type: application/json" \
  -d '{
        "paid_by": 5,
        "currency": 1,
        "total_amount": 500,
        "title": "Lunch",
        "users": [1, 4, 5],
        "split_type": "equal"
      }' \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMDc1OTc2LCJpYXQiOjE3MzE5ODk1NzYsImp0aSI6IjhmYTAwZWI5NDQ2NTQ3MTE4MTNlYTE0ZWE1YTBhNmMxIiwidXNlcl9pZCI6NH0.knFr125bYhGpg9YwipCvUy2ezZGBuj0tmVx6gAeFnlQ"
```

```bash
curl -X POST http://localhost:8000/api/v1/expenses/ \
  -H "Content-Type: application/json" \
  -d '{
        "paid_by": 1,
        "currency": 1,
        "total_amount": 500,
        "title": "Rental Car",
        "users": [1, 4, 5],
        "split_type": "fixed",
        "amounts": [200, 100, 200]
      }' \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMDc1OTc2LCJpYXQiOjE3MzE5ODk1NzYsImp0aSI6IjhmYTAwZWI5NDQ2NTQ3MTE4MTNlYTE0ZWE1YTBhNmMxIiwidXNlcl9pZCI6NH0.knFr125bYhGpg9YwipCvUy2ezZGBuj0tmVx6gAeFnlQ"
```

```bash
curl -X POST http://localhost:8000/api/v1/expenses/ \
   -H "Content-Type: application/json" \
   -d '{
   "paid_by": 4,
   "currency": 1,
   "total_amount": 100,
   "title": "Movie",
   "users": [1, 4, 5],
   "split_type": "percentage",
   "amounts": [10, 30, 60]
   }' \
   -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMDc1OTc2LCJpYXQiOjE3MzE5ODk1NzYsImp0aSI6IjhmYTAwZWI5NDQ2NTQ3MTE4MTNlYTE0ZWE1YTBhNmMxIiwidXNlcl9pZCI6NH0.knFr125bYhGpg9YwipCvUy2ezZGBuj0tmVx6gAeFnlQ"
```

Outstanding Balance for the logged in user

```bash
curl -X GET "http://localhost:8000/api/v1/expenses/user-outstanding/" \
  -H "Content-Type: application/json"
```
