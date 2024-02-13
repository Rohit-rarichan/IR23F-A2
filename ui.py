# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Rohit George Rarichan
# rraricha@uci.edu
# 36126645
from pathlib import Path
from Profile import Profile

def create_journal(filepath):   #creating the journal and adding the inputs
    username = input('Enter the Username: ')
    password = input("Enter the password: ")
    bio = input("Enter bio: ")
    if Path(filepath).exists():
        print("File exists and will now be opened")
        open_journal(filepath)
    file_name = Path(filepath).open('w')
    profile = Profile(username,password,bio)
    profile.save_profile(filepath)
    file_name.close()


def read_file(myPath):        #reading the contents of a file 
    try:
        with myPath.open('r') as my_file:
            data = my_file.read()
            if not data:
                print("EMPTY")
            else:
                print(data)
    except FileNotFoundError:
        print(f"File not found: {myPath}")
    except Exception as e:
        print(f"Error reading file: {e}")

def open_journal(filepath):   #opening the journal with the option to view its contents
    profile = Profile()
    a = input("Do you want to see file content Y/N")
    if a == 'Y':
        read_file(Path(filepath))
    if filepath[-4::1] == ".dsu":
        profile.load_profile(filepath)
        return profile
    else:
        print("Invalid file format")

def edit_journal(profile, option, open_path):  #editing the contents of the journal based on the user input
    if "-usr" in option:
        username = option["-usr"]
        profile.username = username
    if "-pwd" in option:
        password = option["-pwd"]
        profile.password = password
    if "-bio" in option:
        bio = option["-bio"]
        profile.bio = bio 
    if "-addpost" in option:
        post_content = option["-addpost"]
        profile.add_post(post_content)
    if "-delpost" in option:
        post_id = option["-delpost"]
        profile.delete_post(post_id)
    profile.save_profile(open_path)

def print_journal(profile, option):  #printing the contents of the journal that the user requests
    if "-usr" in option:
        print("Username: ", profile.username)
    if "-pwd" in option:
        print("Password: ", profile.password)
    if "-bio" in option:
        print("Bio: ", profile.bio)
    if "-posts" in option:
        print("Posts: ")
        for i, post in enumerate(profile.posts):
            print(f"ID: {i+1}, Content: {post}")
    if "-post" in option:
        post_id = int(option["-post"])
        if i<= post_id <= len(profile.posts):
            print(f"Post {post_id} : {profile.posts[post_id - 1]}")
        else:
            print("Invalid post ID.")
    if "-all" in option:
        print("Username: ", profile.username)
        print("Password: ", profile.password)
        print("Bio: ", profile.bio)
        print("Posts: ")
        for i, post in enumerate(profile.posts):
            print(f"ID: {i+1}, Content: {post}")

def admin():    #admin function if the user doesn't want heavy interface
    while True:
        admin_input = input()
        admin_input = admin_input.split(" ")
        if len(admin_input) == 4 and admin_input[0] == 'C' and admin_input[2] == '-n':
            Path_init = Path(admin_input[1]) / (admin_input[3] + ".dsu")
            create_journal(Path_init)
        elif len(admin_input) == 2 and admin_input[0] =='O':
            open_path = admin_input[1]
            profile_enclosed = open_journal(open_path)
        elif admin_input[0] == 'E':
            option = {} 
            for i in range(1, len(admin_input), 2):
                    option[admin_input[i]] = admin_input[i+1]
            edit_journal(profile_enclosed, option, open_path)
        elif admin_input[0] == 'P':
            option = {} 
            for i in range(1, len(admin_input), 2):
                    option[admin_input[i]] = admin_input[i+1]
            print_journal(profile_enclosed, option)
        elif admin_input == ['Q']:
            break
        elif admin_input =='' or admin_input == ' ':
            break

def user_interface():   #interface for uses who want it 
    while True:
        try:
            command = input('''Welcome! Do you want to create or open a DSU file (type 'C' to create, 'O' to open,
                            type 'E' to edit and 'P' to print the contents of the file
                            type 'admin' for self user input with no prompt :
                            type 'Q' to quit''')

            if command == 'C':   #create command 
                create_path = input("Amazing!, What is the name of the file you want to create ")
                create_journal(create_path)
            elif command == 'O':  #open command
                open_path = input("Cool!, Which file would you like to open ")
                profile = open_journal(open_path)
            elif command == 'E':  #editing command
                keyword = input("Enter the control for what you want to edit ")
                list_keyword = keyword.split(" ")
                option = {} 
                for i in range(0, len(list_keyword), 2):
                    option[list_keyword[i]] = list_keyword[i+1]
                edit_journal(profile, option, open_path)
            elif command == 'P':    #printing command
                keyword = input("Enter the control for what you want to output ")
                list_keyword = keyword.split(" ")
                option = {} 
                for i in range(0, len(list_keyword), 2):
                    list_keyword = list_keyword.strip("/'")
                    list_keyword = list_keyword.strip('/"')
                    option[list_keyword[i]] = list_keyword[i+1]
                print_journal(profile, option)
            elif command == "Q":   #to quit the program
                print("Hope you have completed what you wanted to, Bye!")
                break 
            elif command == "admin":   #to go into admin mode
                admin()
            else:  #if command inputed was incorrect
                print("Incorrect command, Please type again")
        except TypeError:  #if the type entered was not string
            raise Exception("You have used the wrong datatype, Only string is excpeted")