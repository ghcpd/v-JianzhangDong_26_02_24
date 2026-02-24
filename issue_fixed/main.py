from app.processor import load_users

if __name__ == "__main__":
    users = load_users()
    for u in users:
        print(u)