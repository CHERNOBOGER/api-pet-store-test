import requests
import pytest

BASE_URL= 'https://petstore.swagger.io/v2'
HEADERS = {"Content-Type": "application/json"}
@pytest.fixture
def store_data():
    return {
  
  "id": 13,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2024-12-03T16:17:02.049Z",
  "status": "placed",
  "complete": 1

}

def test_post_create_store(store_data):
    response = requests.post(f"{BASE_URL}/store/order", json=store_data, headers=HEADERS)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert int(response_data.get("id")) == store_data["id"], "store ID does not match."

def test_get_store_by_name():
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"   

def test_put_update_store(store_data):
    store_id = store_data["id"]
    response = requests.get(f"{BASE_URL}/store/order/{store_id}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("id") == store_data["id"], "user name does not match in GET request."

def test_delete_store(store_data):
    store_id = store_data["id"]
    response = requests.delete(f"{BASE_URL}/store/order/{store_id}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code} for DELETE request"

    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"   