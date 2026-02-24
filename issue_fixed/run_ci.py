import subprocess
import sys


def run():
    print("=== Installing dependencies ===")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    print("=== Running pytest ===")
    subprocess.check_call([sys.executable, "-m", "pytest"])


if __name__ == "__main__":
    run()