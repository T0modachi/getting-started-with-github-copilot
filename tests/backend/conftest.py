import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(autouse=True)
def restore_activity_state():
    original_participants = {
        name: list(data["participants"])
        for name, data in activities.items()
    }
    yield
    for name, data in activities.items():
        data["participants"] = original_participants[name]


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
