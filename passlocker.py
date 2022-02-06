import pyperclip
import random

class User:
    '''
        Class to generate new instance of a user.
    '''
    users_list = []

    def __init__(self,username,password):
        '''
        __init__ method that helps to define properties of an object
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
            method to save users to users_list
        '''

        User.users_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.users_list

    def delete_user(self):
        '''
            method to delete a saved user from the users_list
        '''

        User.users_list.remove(self)

    pass


class Credentials:
    '''
        Class to create new objects of credentials.
    '''
    credentials_list = []

    def __init__(self,account,user_name,email,password):
        '''
            method to help define credentials of a user. 
        '''

        self.account = account
        self.user_name = user_name
        self.email = email
        self.password = password

    def save_credentials(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list

        """
        return cls.credentials_list

    pass