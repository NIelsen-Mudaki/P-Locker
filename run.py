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

def random_password():
    '''
        Method to generate a random password
    '''
    generatePassword = User.generate_password()
    return generatePassword


def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def create_new_credential(account,user_name,password):
    """
    Function that creates new credentials for a user
    """
    new_credential = Credentials(account,user_name,password)
    return new_credential

def save_credentials(credentials):
    """
    Function to save credentials to the credentials list
    """
    credentials.save_credentials()

def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
    check_user = Credentials.verify_user(username,password)
    return check_user

def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)


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

    elif short_code == "si":
        print('-' * 20)
        print('Enter your username and password to log in.')
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker Manager")  
            print('\n')
        while True:
            print("Use these short codes:\n 'cc' - Create a new credential \n 'dc' - Display Credentials \n 'fc' - Find a credential \n 'd' - Delete credential \n 'ex' - Exit the application \n")
            short_code = input().lower()
            if short_code == "cc":
                print("Create New Credential")
                print('-'*20)
                print("Account name ....")
                account = input().lower()
                print("Your Account username")
                username = input().lower()
                while True:
                    print(" 'tp' - To type your password\n ")
                    passwordOption = input().lower()
                    if passwordOption == 'tp':
                        password = input("Enter Your Own Password: \n")
                        break
                    else:
                        print("Invalid password please try again")
                save_credentials(create_new_credential(account,username,password))
                print('\n')
                print(f"Account Credential for: {account} - UserName: {username} - Password:{password} created succesfully")
                print('\n')
            
            elif short_code == "dc":
                if display_accounts_details():
                    print("Here's your list of acoounts: ")
                    
                    print('*' * 20)
                    print('_'* 20)
                    for account in display_accounts_details():
                        print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                        print('_'* 20)
                    print('*' * 20)
                else:
                    print("You don't have any credentials saved yet..........")
            elif short_code == "fc":
                print("Enter the Account Name you want to search for")
                search_name = input().lower()
                if find_credential(search_name):
                    search_credential = find_credential(search_name)
                    print(f"Account Name : {search_credential.account}")
                    print('-' * 50)
                    print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                    print('-' * 50)
                else:
                    print("That Credential does not exist")
                    print('\n')

            elif short_code == "d":
                print("Enter the account name of the Credentials you want to delete")
                search_name = input().lower()
                if find_credential(search_name):
                    search_credential = find_credential(search_name)
                    print("_"*50)
                    search_credential.delete_credentials()
                    print('\n')
                    print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                    print('\n')
                else:
                    print("The credential you want to delete does not exist in your store")
            elif short_code == 'ex':
                print("Thanks for using P-Locker password manager... Hope to see you next time!")
                break


if __name__ == '__main__':
    main()