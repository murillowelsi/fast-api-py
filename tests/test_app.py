from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_api_py.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root_status_code(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def test_read_root_response_content(client):
    response = client.get('/')
    assert response.json() == {'message': 'Hello World'}


def test_read_root_message_key(client):
    response = client.get('/')
    assert 'message' in response.json()


def test_read_root_message_value(client):
    response = client.get('/')
    assert response.json().get('message') == 'Hello World'


def test_read_root_message_startswith(client):
    response = client.get('/')
    assert response.json().get('message').startswith('Hello')


def test_read_root_message_endswith(client):
    response = client.get('/')
    assert response.json().get('message').endswith('World')


def test_create_user(client):
    request_body = {
        'username': 'Test',
        'email': 'user@example.com',
        'password': '123',
    }

    response = client.post('/users', json=request_body)

    assert response.status_code == HTTPStatus.CREATED
    assert 'id' in response.json()
    assert response.json().get('username') == request_body.get('username')
    assert response.json().get('email') == request_body.get('email')
    assert 'password' not in response.json()


def test_create_user_with_invalid_email(client):
    request_body = {
        'username': 'Test',
        'email': 'test',
        'password': '123',
    }

    response = client.post('/users', json=request_body)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_read_users(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.json()['users'], list)
    assert len(response.json()['users']) == 1
    assert 'id' in response.json()['users'][0]
    assert 'username' in response.json()['users'][0]
    assert 'email' in response.json()['users'][0]
    assert 'password' not in response.json()['users'][0]


def test_read_user_by_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert 'id' in response.json()
    assert 'username' in response.json()
    assert 'email' in response.json()
    assert 'password' not in response.json()


def test_read_user_by_id_not_found(client):
    response = client.get('/users/999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    request_body = {
        'username': 'Fodase',
        'email': 'user@example.com',
        'password': '123',
    }

    response = client.put('/users/1', json=request_body)

    assert response.status_code == HTTPStatus.OK
    assert response.json().get('username') == request_body.get('username')
    assert response.json().get('email') == request_body.get('email')
    assert 'password' not in response.json()


def test_update_user_not_found(client):
    request_body = {
        'username': 'Fodase',
        'email': 'user@example.com',
        'password': '123',
    }

    response = client.put('/users/999', json=request_body)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user_with_invalid_email(client):
    request_body = {
        'username': 'Test',
        'email': 'test',
        'password': '123',
    }

    response = client.put('/users/1', json=request_body)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NO_CONTENT
