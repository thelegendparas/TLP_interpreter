import os
import getpass
from repl import start

def main():
    try:
        # Get the current user's username
        username = getpass.getuser()

        # Print the greeting message
        print(f"Hello {username}! Welcome to TPL programming language")
        print("Feel free to type n commands")

        # Start the REPL
        start()

    except Exception as e:
        print(f"An error has occured: {e}")

if __name__ == "__main__":
    main()