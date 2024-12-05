import requests
import pytest

BASE_URL= 'https://petstore.swagger.io/v2'
HEADERS = {"Content-Type": "application/json"}

@pytest.fixture
def user_data():
    return {
  "id": 1,
  "username": "user12",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}

def test_post_create_user(user_data):
    response = requests.post(f"{BASE_URL}/user", json=user_data, headers=HEADERS)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert int(response_data.get("message")) == user_data["id"], "user ID does not match."

def test_get_user_by_name(user_data):
    user_name = user_data["username"]
    response = requests.get(f"{BASE_URL}/user/{user_name}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("username") == user_data["username"], "user name does not match in GET request."

def test_put_update_user(user_data):
    updated_data = user_data.copy()
    user_name = user_data["username"]
    updated_data["firstName"] = "Integer"
    response = requests.put(f"{BASE_URL}/user/{user_name}", json=updated_data, headers=HEADERS)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code} for PUT request"
    response = requests.get(f"{BASE_URL}/user/{user_name}")
    response_data = response.json() if response.content else {}
    assert response_data.get("firstName") == updated_data["firstName"], "user name did not update."

def test_delete_user(user_data):
    user_name = user_data["username"]
    response = requests.delete(f"{BASE_URL}/user/{user_name}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code} for DELETE request"

    response = requests.get(f"{BASE_URL}/user/{user_name}")
    assert response.status_code == 404, f"Expected 404 for deleted user, got {response.status_code}"

