# Task Management App with FastAPI

This is a simple Task Management application built with FastAPI, allowing you to manage your tasks efficiently. You can create, view, update, and filter tasks based on various criteria.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Running the App](#running-the-app)
  - [API Endpoints](#api-endpoints)
    - [Get All Tasks](#get-all-tasks)
    - [Get Task by ID](#get-task-by-id)
    - [Mark Task as Finished](#mark-task-as-finished)
    - [Create a New Task](#create-a-new-task)
    - [Update Task](#update-task)
    - [Delete Task](#delete-task)
    - [Create User](#create-user)
    - [User Login](#user-login)

## Getting Started

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/task-management-app.git
    cd task-management-app

2. **Create and activate a virtual environment:**
    ```bash
    virtualenv venv
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt

## Project Structure
The project is structured as follows:
    ```bash
    Task-Management/
    ├── repository/
    │   ├── __init__.py
    │   ├── task.py
    │   └── user.py
    ├── routers/  
    │   ├── __init__.py
    │   ├── authentication.py
    │   ├── task.py
    │   └── user.py
    ├── __init__.py
    ├── .env
    ├── database.py
    ├── hashing.py
    ├── main.py
    ├── models.py
    ├── oauth2.py
    ├── requirements.txt
    ├── schemas.py
    └── token_manager.py

- ***`repository/`***: This directory contains modules for database interactions and data models. task.py and user.py define the database models for tasks and users.

- ***`routers/`***: This directory contains modules that define API endpoints and request handling logic. `authentication.py`, `task.py`, and `user.py` handle various API endpoints and their functionality.

- ***`.env/`***: This file can be used to store environment variables and configuration settings.

- ***`database.py/`***: This module is responsible for configuring the database connection.

- ***`hashing.py/`***: This module provides functions for hashing and verifying passwords.

- ***`main.py/`***: This is the entry point of the FastAPI application where the FastAPI `FastAPI` instance is created and configured.

- ***`models.py/`***: This module defines the data models used in the application.

- ***`oauth2.py/`***: This module contains OAuth2-related functions for user authentication.

- ***`requirements.txt/`***: This file lists the required Python packages and their versions.

- ***`schemas.py/`***: This module defines Pydantic schemas used for data validation and serialization.

- ***`token_manager.py/`***: This module manages JWT (JSON Web Token) creation and validation for authentication.

## Usage
### Running the App
1. **Ensure you are in the project directory and the virtual environment is activated.**
2. **Run the FastAPI development server:**
    ```bash
    uvicorn main:app --reload
This will start the FastAPI application on http://localhost:8000.

### API Endpoints
#### Get All Tasks
- **Endpoint:** /tasks
- **Method:** GET
- **Parameters:**
- ***`page`***: Page number (default is 1)
- ***`per_page`***: Items per page (default is 10)
- ***`finished`***: Filter by finished tasks (True/False/None for all)
- ***`created_at_start`***: Filter tasks created after this date (YYYY-MM-DD)
- ***`created_at_end`***: Filter tasks created before this date (YYYY-MM-DD)
- ***`finished_at_start`***: Filter tasks finished after this date (YYYY-MM-DD)
- ***`finished_at_end`***: finished_at_end
- **Response:** List of tasks matching the criteria.

#### Get Task by ID
- **Endpoint:** /tasks/{id}
- **Method:** GET
- **Parameters:** id - Task ID
- **Response:** Details of the task with the specified ID.

#### Mark Task as Finished
- **Endpoint:** /tasks/{id}/finished
- **Method:** PUT
- **Parameters:** id - Task ID
- **Response:** Updated task status.

#### Create a New Task
- **Endpoint:** /tasks
- **Method:** POST
- **Request Body:** Task details (title and description)
- **Response:** Created task details.

#### Update Task
- **Endpoint:** /tasks/{id}
- **Method:** PUT
- **Parameters:** id - Task ID
- **Request Body:** Updated task details (title, description, and finished status)
- **Response:** Updated task details.

#### Delete Task
- **Endpoint:** /tasks/{id}
- **Method:** DELETE
- **Parameters:** id - Task ID
- **Response:** No content (204) upon successful deletion.

#### Create User
- **Endpoint:** /user
- **Method:** POST
- **Request Body:** User details (user_name, email, and password)
- **Response:** Created user details.

#### User Login
- **Endpoint:** /login
- **Method:** POST
- **Request Body:** User login details (username and password)
- **Response:** Access token for authentication.

    Note: Authentication is required for all endpoints except User Login.