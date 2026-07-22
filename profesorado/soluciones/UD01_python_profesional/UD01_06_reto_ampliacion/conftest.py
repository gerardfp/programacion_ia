import pytest

@pytest.fixture
def sample_inference_payload():
    return {"prompt": "Prueba de fixture con pytest", "temperatura": 0.7}
