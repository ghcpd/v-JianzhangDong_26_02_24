import pytest
from app.validator import User


def test_valid_user():
    user = User(name="Alice", age=30)
    assert user.name == "Alice"
    assert user.age == 30


def test_invalid_age():
    with pytest.raises(ValueError):
        User(name="Bob", age=-1)