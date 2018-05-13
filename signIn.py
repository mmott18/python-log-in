from sqlite import *

create_table()

run = True


def register_user():
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")

    if check_user(username) == 0:
        insert_user_info(username, password)
        close_db()
    else:
        print("User already exists.")


def sign_in_user():
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")

    if check_user(username) == 0:
        print("Incorrect username or password")
    else:
        if check_pass(password) == 0:
            print("Incorrect username or password.")
        else:
            print("Welcome, " + username + ".")


while run:

    print("Would you like to sign in or register?")
    choice = input("Enter s for sign in or r for register: ")

    if choice == ("r" or "R"):
        register_user()
        choice = ""
    if choice == ("s" or "S"):
        sign_in_user()
        choice = ""
        run = False
