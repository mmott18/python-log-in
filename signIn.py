from sqlite import *
from security import *
import time


def countdown(t):
    print("Too many incorrect sign in attempts.")
    print("Please wait for " + str(t) + " seconds.")
    while t > 0:
        print(t)
        time.sleep(1)
        t -= 1


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
    attempts = 0
    success = False

    while not success:
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")

        hashed_user = hash_data(username)
        hashed_pass = hash_data(password)

        if check_user(hashed_user) == 0:
            print("Incorrect username or password")
        else:
            if check_pass(hashed_pass) == 0:
                print("Incorrect username or password.")
                attempts += 1

                if attempts >= 3:
                    diff = attempts - 2
                    countdown(3 * (2**diff))
            else:
                attempts = 0
                print("Welcome, " + username + ".")
                success = True


def menu():
    create_table()
    run = True
    while run:

        print("Would you like to sign in or register?")
        choice = input("Enter s for sign in or r for register: ")

        if choice[0].lower() == "r":
            register_user()
        elif choice[0].lower() == "s":
            sign_in_user()
            run = False
            close_db()
        else:
            print("Invalid choice.")


menu()
