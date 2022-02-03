import unittest
from passlocker import User, Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
            method to run before a test case
        '''

        self.new_user = User('Nielsen','Mudaki','pass1234') #create a user object

    def test_init(self):
        '''
            test case to see if object is initialised properly
        '''

        self.assertEqual(self.new_user.f_name, 'Nielsen')
        self.assertEqual(self.new_user.l_name, 'Mudaki')
        self.assertEqual(self.new_user.password, 'pass1234')

    def test_save_user(self):
        '''
            test case to confirm if a user is saved into the user list
        '''
        self.new_user.save_user() #saving a user
        self.assertEqual(len(User.users_list),1)


class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.

        """
        self.new_credential = Credentials('Gmail','Nielsen-Jumba','jumbanielsen@gmail.com','pass1234')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.user_name,'Nielsen-Jumba')
        self.assertEqual(self.new_credential.email, 'jumbanielsen@gmail.com')
        self.assertEqual(self.new_credential.password,'pass1234')

    def save_credential_tests(self):
        """
        test case to test if the crential object is saved into the credentials list.

        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_delete_credentials(self):
        '''
            test case to check if a user can be deleted from the users_list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('Gmail','Nielsen-Jumba','jumbanielsen@gmail.com','pass1234')
        test_credential.save_credentials()

        self.new_credential.delete_credentials() #deletes a user
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == '__main__':
    unittest.main()