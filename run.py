from cli.main import run
import sys
import os

if __name__ == "__main__":
    username = sys.argv[1]
    token = os.getenv("GITHUB_TOKEN")
    run(username, token)