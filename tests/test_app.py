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
