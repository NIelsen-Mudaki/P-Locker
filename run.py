#!/usr/bin/env python3.6

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