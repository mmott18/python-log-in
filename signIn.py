from sqlite import *
from security import *


def register_user():
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")

    if check_user(username) == 0:
        hashed_user = hash_data(username)
        hashed_pass = hash_data(password)
        insert_user_info(hashed_user, hashed_pass)
    else:
        print("User already exists.")


def sign_in_user():
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")

    hashed_user = hash_data(username)
    hashed_pass = hash_data(password)

    if check_user(hashed_user) == 0:
        print("Incorrect username or password")
    else:
        if check_pass(hashed_pass) == 0:
            print("Incorrect username or password.")
        else:
            print("Welcome, " + username + ".")


def menu():
    create_table()
    run = True
    while run:

        print("Would you like to sign in or register?")
        choice = input("Enter s for sign in or r for register: ")
        print(choice)

        if choice[0].lower() == "r":
            register_user()
            print(choice)
        elif choice[0].lower() == "s":
            sign_in_user()
            print(choice)
            run = False
            close_db()
        else:
            print("Invalid choice.")
            print(choice)


menu()
