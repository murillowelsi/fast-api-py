from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_py.app import app


def test_read_root_should_return_ok():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World - Fodase'}
    assert response.json().get('message') == 'Hello World - Fodase'
    assert response.json().get('message').endswith('Fodase')

    def test_read_root_status_code():
        client = TestClient(app)

        response = client.get('/')

        assert response.status_code == HTTPStatus.OK

    def test_read_root_response_content():
        client = TestClient(app)

        response = client.get('/')

        assert response.json() == {'message': 'Hello World - Fodase'}

    def test_read_root_message_key():
        client = TestClient(app)

        response = client.get('/')

        assert 'message' in response.json()

    def test_read_root_message_value():
        client = TestClient(app)

        response = client.get('/')

        assert response.json().get('message') == 'Hello World - Fodase'

    def test_read_root_message_endswith():
        client = TestClient(app)

        response = client.get('/')

        assert response.json().get('message').endswith('Fodase')
