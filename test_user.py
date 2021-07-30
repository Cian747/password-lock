import unittest
from user import User
from cred import Credentials
import pyperclip

class TestUserCred(unittest.TestCase):
    
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up the user class to run before each test cases
        '''
        self.new_user = User("Cian","Kaiser","Cian254","23456")
        self.new_cred = Credentials("cyan_kaiser","ab!@254","Cian254","github")


    def tearDown(self):
        '''
        tearDown method to refresh the user and cred list
        '''

        User.user_list = []
        Credentials.cred_list = []


    def test_init(self):
        '''
        first test to test both objects.
        '''

        # User class test
        self.assertEqual(self.new_user.first_name,"Cian")
        self.assertEqual(self.new_user.last_name,"Kaiser")
        self.assertEqual(self.new_user.user_name,"Cian254")
        self.assertEqual(self.new_user.password,"23456")

        # Credentials class test
        self.assertEqual(self.new_cred.user_name,"cyan_kaiser")
        self.assertEqual(self.new_cred.password,"ab!@254")
        self.assertEqual(self.new_cred.system_username,"Cian254")
        self.assertEqual(self.new_cred.account_name,"github")

    def test_save_user(self):
        '''
        test if user details are saved
        '''    
        self.new_user.save_user()# save user
        self.assertEqual(len(User.user_list),1)


    def save_multiple_user(self):
        '''
        create multiple users
        '''
        self.new_user.save_user()
        test_user = User("Me","You","MeU12","1234")
        test_user.save_user()

        self.assertEqual(len(User.user_list),2)


    def test_add_credentials(self):
        '''
        Credentials can be added and saved
        '''

        self.new_cred.add_credentials()
        self.assertEqual(len(Credentials.cred_list),1)

    def test_store_multiple_credentials(self):
        '''
        Checking if multiple credentials
        '''

        self.new_cred.add_credentials()
        test_cred = Credentials("Bills","1234","Me12","Twitter")
        test_cred.add_credentials()

    def test_delete_user(self):
        '''
        delete user
        '''
        self.new_user.save_user()
        test_user = User("Me","You","MeU12","1234")
        test_user.save_user()

        #test if user can be deleted
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)


    def test_delete_cred(self):
        '''
        Checking whether credentials can be deleted
        '''

        self.new_cred.add_credentials()
        test_cred = Credentials("Our12","1234","MeU12","mailchimp")
        test_cred.add_credentials()

        #test if user can be deleted
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list),1)

    def test_display_credentials(self):
        '''
        Assert that the credentials are available
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.cred_list)

    def test_search_credentials(self):
        '''
        Confirm username can be located on the list
        '''
        self.new_cred.add_credentials()
        test_cred = Credentials("Bills","1234","Me12","Twitter")
        test_cred.add_credentials() 

        #Assert that account name can be verified
        grid_username = Credentials.credentials_exist("Me12")

        self.assertTrue(grid_username)    



    

if __name__ == '__main__':
    unittest.main()









# Sign up - user
# Login -- system_username - user
# Add credentials - cred
# Create credentials - cred
# Create password
# Generate password
# Delete credentials
