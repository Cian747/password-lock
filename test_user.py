import unittest
from user import User
from cred import Credentials

class TestUser(unittest.TestCase):
    
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setup(self):
        '''
        Set up the user class to run before each test cases
        '''
        self.new_user = User("Cian","Kaiser","Cian254","23456")
        # self.new_cred = Credentials("cyan_kaiser","ab!@254","Cian254","github")


    def test_init(self):
        '''
        first test to test both objects.
        '''

        # User class test
        self.assertEqual(self.new_user.first_name,"Cian")
        self.assertEqual(self.new_user.first_name,"Kaiser")
        self.assertEqual(self.new_user.first_name,"Cian254")
        self.assertEqual(self.new_user.first_name,"23456")

        # Credentials class test
        # self.assertEqual(self.new_cred.user_name,"cyan_kaiser")
        # self.assertEqual(self.new_user.first_name,"ab!@254")
        # self.assertEqual(self.new_user.first_name,"Cian254")
        # self.assertEqual(self.new_user.first_name,"github")

if __name__ == '__main__':
    unittest.main()









# Sign up - user
# Login -- system_username - user
# Add credentials - cred
# Create credentials - cred
# Create password
# Generate password
# Delete credentials
