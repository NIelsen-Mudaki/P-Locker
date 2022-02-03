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

if __name__ == '__main__':
    unittest.main()