#!/usr/bin/env python3.6

from passlocker import User, Credentials

def new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user