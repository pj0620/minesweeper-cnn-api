import os
import sys
import unittest
from unittest import TextTestRunner
import subprocess


def unittests_passed():
    cmd = ["nosetests"]
    result = subprocess.run(cmd, text=True, capture_output=True)

    print('STDOUT')
    print(result.stdout)
    print('STDERR')
    print(result.stderr)

    # Store stderr in a variable
    stderr_content = result.stderr

    if 'FAILED' in stderr_content:
        print('Unit tests failed!')
        return False
    else:
        print('Unit tests passed')
        return True

def start_server():
    # Set environment variables
    print("Setting FLASK_ENV to development...")
    os.environ["FLASK_ENV"] = "development"
    os.environ["FLASK_APP"] = "app.py"

    # Define the FLASK variable
    FLASK = "./venv/bin/flask"
    print(f"Using Flask executable at: {FLASK}")

    # Run the flask app
    print("Running Flask app...")
    subprocess.run([FLASK, "run"])


def main():
    if not unittests_passed():
        print('Canceling starting of server')
        return

    print('Starting server')
    start_server()


if __name__ == '__main__':
    main()
