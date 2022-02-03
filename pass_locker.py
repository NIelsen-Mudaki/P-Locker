class User:
    '''
        Class to generate new instance of a user.
    '''
    users_list = []

    def __init__(self,f_name,l_name,password):
        '''
        __init__ method that helps to define properties of an object
        '''
        self.f_name = f_name
        self.l_name = l_name
        self.password = password

    pass


class Credentials:
    '''
        Class to create new objects of credentials.
    '''
    credentials_list = []

    def __init__(self,account,user_name,password):
        '''
            method to help define credentials of a user. 
        '''

        self.account = account
        self.user_name = user_name
        self.password = password

    pass