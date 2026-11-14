import pytest
from fastapi.testclient import TestClient
from app import main

client = TestClient(main.app)

@pytest.fixture(autouse=True)
def reset_data():
    main.items.clear()
    main.next_id = 1

def test_list_empty():
    assert client.get('/api/items').json() == []

def test_create_and_get():
    response = client.post('/api/items', json={'name': 'Book', 'price': 10})
    assert response.status_code == 201
    assert response.json() == {'id': 1, 'name': 'Book', 'price': 10.0}
    assert client.get('/api/items/1').json()['name'] == 'Book'

def test_update():
    client.post('/api/items', json={'name': 'Book', 'price': 10})
    response = client.put('/api/items/1', json={'name': 'Pen', 'price': 2})
    assert response.status_code == 200
    assert response.json()['name'] == 'Pen'

def test_delete():
    client.post('/api/items', json={'name': 'Book', 'price': 10})
    assert client.delete('/api/items/1').status_code == 204
    assert client.get('/api/items/1').status_code == 404

def test_not_found():
    assert client.get('/api/items/999').status_code == 404
    assert client.put('/api/items/999', json={'name': 'X', 'price': 1}).status_code == 404
    assert client.delete('/api/items/999').status_code == 404

def test_validation():
    assert client.post('/api/items', json={'name': '', 'price': -1}).status_code == 422

def test_openapi():
    assert client.get('/openapi.json').status_code == 200
    assert client.get('/docs').status_code == 200

def test_basic_math():
    assert 2 + 2 == 4