from fastapi.testclient import TestClient 
from fastapi import Depends
from oauth2 import get_current_user
from main import app 
import datetime
import pytz
from dateutil import parser

client = TestClient(app)

data = {
  "title": "string",
  "description": "string"
}

def test_create_task():
    auth_data = {"username": "xxx", "password": "xxx"}
    auth_response = client.post("/login", data=auth_data)
    auth_token = auth_response.json().get("access_token")

    data = {"title": "New Task", "description": "This is a new task."}

    response = client.post(
        "/tasks",
        json=data,
        headers={"Authorization": f"Bearer {auth_token}"},  # Add authorization header
    )
    assert response.json()["title"] == "New Task"
    assert response.json()["description"] == "This is a new task."
    created_at_str = response.json()["created_at"]
    created_at_datetime = parser.parse(created_at_str).astimezone(pytz.timezone('Africa/Tunis'))
    current_datetime = datetime.datetime.now(pytz.timezone('Africa/Tunis'))  # Make it offset-aware
    assert created_at_datetime <= current_datetime
    assert response.status_code == 201