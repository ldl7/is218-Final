def test_calculator_e2e():
    # Simulate user sending API request
   import pytest
from fastapi.testclient import TestClient
from main import app  # Import the FastAPI app instance

# Create a TestClient instance to simulate API requests
client = TestClient(app)

# ==============================
# E2E Test Cases for Calculator API
# ==============================

def test_e2e_addition():
    """
    End-to-end test for the addition endpoint.
    """
    response = client.get("/add/?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_e2e_subtraction():
    """
    End-to-end test for the subtraction endpoint.
    """
    response = client.get("/sub/?a=10&b=4")
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_e2e_multiplication():
    """
    End-to-end test for the multiplication endpoint.
    """
    response = client.get("/mul/?a=6&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 42}

def test_e2e_division():
    """
    End-to-end test for the division endpoint.
    """
    response = client.get("/div/?a=12&b=4")
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_e2e_divide_by_zero():
    """
    End-to-end test for division by zero, expecting an error.
    """
    response = client.get("/div/?a=5&b=0")
    assert response.status_code == 400
    assert "error" in response.json()
    assert response.json()["error"] == "Cannot divide by zero"

def test_e2e_frontend_served():
    """
    Test if the frontend HTML file is served properly.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "Calculator" in response.text  # Ensure the HTML page has 'Calculator' as part of its content
