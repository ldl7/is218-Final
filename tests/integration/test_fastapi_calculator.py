import pytest
from fastapi.testclient import TestClient
from main import app  # Ensure 'main.py' is correctly importing the FastAPI app instance

# Create a TestClient instance to simulate API requests
client = TestClient(app)


# ==============================
# Test Cases for /add/
# ==============================
@pytest.mark.parametrize("a, b, expected_result", [
    (1, 2, 3),          # Positive numbers
    (-1, -2, -3),       # Negative numbers
    (0, 0, 0),          # Both zeros
    (1e6, 1e6, 2e6),    # Large numbers
    (-1, 1, 0)          # Canceling each other out
])
def test_add(a, b, expected_result):
    response = client.get(f"/add/?a={a}&b={b}")
    assert response.status_code == 200
    assert response.json() == {"result": expected_result}


# ==============================
# Test Cases for /sub/
# ==============================
@pytest.mark.parametrize("a, b, expected_result", [
    (5, 3, 2),          # Positive numbers
    (-5, -3, -2),       # Negative numbers
    (0, 0, 0),          # Both zeros
    (1e6, 1e5, 9e5),    # Large numbers
    (1, 5, -4)          # Result is negative
])
def test_sub(a, b, expected_result):
    response = client.get(f"/sub/?a={a}&b={b}")
    assert response.status_code == 200
    assert response.json() == {"result": expected_result}


# ==============================
# Test Cases for /mul/
# ==============================
@pytest.mark.parametrize("a, b, expected_result", [
    (2, 3, 6),          # Positive numbers
    (-2, -3, 6),        # Multiplying negatives
    (0, 100, 0),        # Multiplying by zero
    (1e3, 1e3, 1e6),    # Large numbers
    (-2, 5, -10)        # Negative times positive
])
def test_mul(a, b, expected_result):
    response = client.get(f"/mul/?a={a}&b={b}")
    assert response.status_code == 200
    assert response.json() == {"result": expected_result}


# ==============================
# Test Cases for /div/
# ==============================
@pytest.mark.parametrize("a, b, expected_result", [
    (6, 3, 2.0),          # Positive numbers
    (-6, -3, 2.0),        # Dividing negatives
    (0, 5, 0.0),          # Zero as numerator
    (1e6, 1e2, 1e4),      # Large numbers
    (-6, 3, -2.0)         # Negative divided by positive
])
def test_div(a, b, expected_result):
    response = client.get(f"/div/?a={a}&b={b}")
    assert response.status_code == 200
    assert response.json() == {"result": expected_result}


# ==============================
# Test Division by Zero
# ==============================
def test_divide_by_zero():
    response = client.get("/div/?a=5&b=0")
    assert response.status_code == 400  # Expecting a 400 Bad Request
    assert "error" in response.json()  # Check for 'detail' instead of 'error'
    assert response.json()["error"] == "Cannot divide by zero"  # Correct message
