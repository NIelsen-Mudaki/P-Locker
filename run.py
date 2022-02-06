#!/usr/bin/env python3.6

from click import password_option
from passlocker import User, Credentials

def new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def create_new_credential(account,user_name,email,password):
    """
    Function that creates new credentials for a user
    """
    new_credential = Credentials(account,user_name,email,password)
    return new_credential

def save_credentials(credentials):
    """
    Function to save credentials to the credentials list
    """
    credentials.save_credentials()


def main():
    print("Welcome to the P-Locker password manager*** \n Use the following short codes to proceed*** \n ca - Create Account \n si - Already Have an Account")

    short_code = input("").lower()

    if short_code == "ca":
        print('Create your New Account here ...')
        print('-' * 20)
        username = input('username: ')

        while True:
            print("Select: \n tp - to type your password... \n gp - To generate a unique random password...")
            passwordOption = input("").lower()
            if passwordOption == 'tp':
                print('Enter Password: ')
                password = input("")
                break
            elif passwordOption == 'gp':
                password = random_password()
                break
            else:
                print('To use your account you will need to add a password')

    save_user(new_user(username,password))

    print(f'Congratulations {username} you have successfully created your account! Your password is {password}.')