# Task Management App with FastAPI

This is a simple Task Management application built with FastAPI, allowing you to manage your tasks efficiently. You can create, view, update, and filter tasks based on various criteria.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the App](#running-the-app)
  - [API Endpoints](#api-endpoints)
    - [Get All Tasks](#get-all-tasks)
    - [Get Task by ID](#get-task-by-id)
    - [Mark Task as Finished](#mark-task-as-finished)
    - [Create a New Task](#create-a-new-task)
- [Contributing](#contributing)
- [License](#license)

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
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt

## Usage
### Running the App
1. **Ensure you are in the project directory and the virtual environment is activated.**
2. **Run the FastAPI development server:**
    ```bash
    uvicorn main:app --reload
This will start the FastAPI application on http://localhost:8000.



