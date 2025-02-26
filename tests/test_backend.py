import sys
import os

# Add the backend/src folder to the sys.path so that server.py can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend/src')))

from fastapi.testclient import TestClient
from server import app  # Now this import should work

client = TestClient(app)

# Test GET /api/lists (to get all lists)
def test_get_all_lists():
    response = client.get("/api/lists")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Check if the response is a list

# Test POST /api/lists (to create a new list)
def test_create_todo_list():
    new_list = {"name": "Test List"}
    response = client.post("/api/lists", json=new_list)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "Test List"

# Test GET /api/lists/{list_id} (get a single list)
def test_get_list():
    # First create a list to test fetching
    new_list = {"name": "Test List"}
    create_response = client.post("/api/lists", json=new_list)
    list_id = create_response.json()["id"]

    # Now fetch the created list
    response = client.get(f"/api/lists/{list_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test List"

# Test DELETE /api/lists/{list_id} (delete a list)
def test_delete_list():
    # First create a list to test deletion
    new_list = {"name": "Test List"}
    create_response = client.post("/api/lists", json=new_list)
    list_id = create_response.json()["id"]

    # Delete the created list
    response = client.delete(f"/api/lists/{list_id}")
    assert response.status_code == 200
    assert response.json() is True  # Assuming your delete endpoint returns `True` on success

# Test POST /api/lists/{list_id}/items (create an item)
def test_create_item():
    # Create a list first
    new_list = {"name": "Test List"}
    create_list_response = client.post("/api/lists", json=new_list)
    list_id = create_list_response.json()["id"]

    # Now create an item in the list
    new_item = {"label": "Test Item"}
    response = client.post(f"/api/lists/{list_id}/items/", json=new_item)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["label"] == "Test Item"

# Test DELETE /api/lists/{list_id}/items/{item_id} (delete an item)
def test_delete_item():
    # Create a list first
    new_list = {"name": "Test List"}
    create_list_response = client.post("/api/lists", json=new_list)
    list_id = create_list_response.json()["id"]

    # Create an item
    new_item = {"label": "Test Item"}
    create_item_response = client.post(f"/api/lists/{list_id}/items/", json=new_item)
    item_id = create_item_response.json()["id"]

    # Delete the item
    response = client.delete(f"/api/lists/{list_id}/items/{item_id}")
    assert response.status_code == 200

# Test GET /api/dummy (get a dummy response)
def test_get_dummy():
    response = client.get("/api/dummy")
    assert response.status_code == 200
    assert "id" in response.json()
    assert "when" in response.json()
