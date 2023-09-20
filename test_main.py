from fastapi.testclient import TestClient 
from fastapi import Depends
from oauth2 import get_current_user
from main import app 
import datetime
import pytz
from dateutil import parser

client = TestClient(app)

task_data = {"title": "New Task", "description": "This is a new task."}
task_compare_data = {'title': 'New Task', 'description': 'This is a new task.', 'finished': False, 'finished_at': None, 'assigned_to': None}
auth_data = {"username": "xxx", "password": "xxx"}
auth_response = client.post("/login", data=auth_data)
auth_token = auth_response.json().get("access_token")

def test_create_task():
    response = client.post(
        "/tasks",
        json=task_data,
        headers={"Authorization": f"Bearer {auth_token}"},  
    )
    assert response.json()["title"] == "New Task"
    assert response.json()["description"] == "This is a new task."
    created_at_str = response.json()["created_at"]

    created_at_datetime = parser.parse(created_at_str).astimezone(pytz.timezone('Africa/Tunis'))
    current_datetime = datetime.datetime.now(pytz.timezone('Africa/Tunis'))  
    assert created_at_datetime <= current_datetime
    assert response.status_code == 201

def test_get_all_tasks():
    response = client.get(
        "/tasks",
        headers={"Authorization": f"Bearer {auth_token}"},  
    )
    assert response.status_code == 200
    assert task_compare_data == response.json()[-1]

def test_set_task_finished():
    response = client.put(
        "/tasks/54/finished",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 202
    assert response.json()["data"]["finished"]
    created_at_datetime = parser.parse(response.json()["data"]["finished_at"]).astimezone(pytz.timezone('Africa/Tunis'))
    current_datetime = datetime.datetime.now(pytz.timezone('Africa/Tunis'))  
    assert created_at_datetime <= current_datetime

def test_remove_task():
    response = client.delete(
        "/tasks/52",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 204
    