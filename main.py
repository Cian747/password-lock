#!/usr/bin/env python3.9
from user import User
from cred import Credentials

def sign_up(f_name,l_name,us_name,pass_word):
    '''
    Function to create an account
    '''
    new_user = User(f_name,l_name,us_name,pass_word)
    return new_user

def save_user(user):
    '''
    save your account upon login
    '''
    User.save_user()

def delete_cred():
    '''
    Delete credentials
    '''
    Credentials.delete_cred()

def show_cred():
    '''
    View the credentials you have created
    '''
    return Credentials.display_credentials()



def main():
    print("Hello welcome to Grid lock. What's your name?")
    u_name = input()

    print(f"Hey {u_name}. How would you like to proceed?: ")
    print("\n")

    while True:
        print("use these short codes: ss - Sign up," )