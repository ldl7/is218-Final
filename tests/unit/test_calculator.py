import pytest
from app.operations.add import add
from app.operations.sub import sub
from app.operations.mul import mul
from app.operations.div import div


# ==============================
# Test Cases for Addition
# ==============================
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),          # Base case: Positive numbers
    (-1, -2, -3),       # Edge case: Negative numbers
    (0, 0, 0),          # Edge case: Adding zeros
    (1e6, 1e6, 2e6),    # Edge case: Large numbers
    (-1, 1, 0)          # Edge case: Canceling each other out
])
def test_add(a, b, expected):
    assert add(a, b) == expected


# ==============================
# Test Cases for Subtraction
# ==============================
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),          # Base case: Positive numbers
    (-5, -3, -2),       # Edge case: Negative numbers
    (0, 0, 0),          # Edge case: Subtracting zeros
    (1e6, 1e5, 9e5),    # Edge case: Large numbers
    (1, 5, -4)          # Edge case: Result is negative
])
def test_sub(a, b, expected):
    assert sub(a, b) == expected


# ==============================
# Test Cases for Multiplication
# ==============================
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),          # Base case: Positive numbers
    (-2, -3, 6),        # Edge case: Multiplying negatives
    (0, 100, 0),        # Edge case: Multiplying by zero
    (1e3, 1e3, 1e6),    # Edge case: Large numbers
    (-2, 5, -10)        # Edge case: Negative * Positive
])
def test_mul(a, b, expected):
    assert mul(a, b) == expected


# ==============================
# Test Cases for Division
# ==============================
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2.0),         # Base case: Positive numbers
    (6, -3, -2.0),       # Edge case: Dividing negatives
    (1e6, 1e3, 1000.0), # Edge case: Large numbers
    (-10, 5, -2.0)       # Edge case: Negative divided by positive
])
def test_div(a, b, expected):
    assert div(a, b) == expected


# ==============================
# Test Division by Zero
# ==============================
def test_divide_by_zero():
    with pytest.raises(ValueError, match="cant divide by zero."):
        div(100, 0)
