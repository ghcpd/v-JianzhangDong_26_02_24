import json
from app.validator import User


def load_users():
    with open("data/sample.json") as f:
        raw = json.load(f)

    return [User(**item) for item in raw]