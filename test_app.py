import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_chat_with_known_topic(client):
    response = client.post(
        "/chat",
        json={"message": "I have a fever"}
    )

    assert response.status_code == 200
    assert "reply" in response.json


def test_chat_with_empty_message(client):
    response = client.post(
        "/chat",
        json={"message": ""}
    )

    assert response.status_code == 400