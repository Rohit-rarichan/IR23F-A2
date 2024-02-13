# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Rohit George Rarichan
# rraricha@uci.edu
# 36126645
from pathlib import Path
from Profile import Profile

def create_journal(filepath):
    username = input('Enter the Username: ')
    password = input("Enter the password: ")
    bio = input("Enter bio: ")
    file_name = Path(filepath).open('w')
    profile = Profile(username,password,bio)
    profile.save_profile(filepath)
    file_name.close()


def user_interface():
    while True:
        try:
            command = input('''Welcome! Do you want to create or open a DSU file (type 'C' to create, 'O' to open,
                            type 'E' to edit and 'P' to print the contents of the file
                            type 'admin' for self user input with no prompt :
                            type 'Q' to quit''')

            if command == 'C':
                create_path = input("Amazing!, What is the name of the file you want to create ")
                create_journal(create_path)
            elif command == "Q":
                print("Hope you have completed what you wanted to, Bye!")
                break
            else:
                print("Incorrect command, Please type again")
        except TypeError:
            raise Exception("You have used the wrong datatype, Only string is excpeted")