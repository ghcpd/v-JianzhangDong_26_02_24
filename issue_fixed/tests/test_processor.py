from app.processor import load_users


def test_load_users():
    users = load_users()
    assert len(users) == 2
    assert users[0].name == "Alice"