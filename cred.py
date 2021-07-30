import random
import string

class Credentials:
    """
    Created user class that will store all the data upon login
    """

    pass


    cred_list = []

    def __init__(self,user_name,password,system_username,account_name):
        """
        Initialized an object with self and the parameters it will use.
        
        Args:
        first_name: New user first name.
        last_name: New user last name.
        user_name: New user first name.
        password: New user password.
        """    

        self.user_name = user_name
        self.password = password
        self.system_username = system_username
        self.account_name = account_name
 
    def add_credentials(self):
        '''
        Add credentials
        '''
        Credentials.cred_list.append(self)


    def delete_cred(self):
        '''
        Able to delete credentials
        '''

        Credentials.cred_list.remove(self)

    @classmethod
    def credentials_exist(cls,text):
        '''
        Check if user_name exists
        Args:
            system_username: username to be searched for.
        Return:
            Boolean True or false
        '''
        for cred in cls.cred_list:
            if cred.system_username == text:
                return True
            else:
                return False 

    @classmethod
    def search_credentials(cls,text):
        '''
        search for username
        Args:
            user_name:name of account to be registered
        '''
        for cred in cls.cred_list:
            if cred.user_name == text:
                return cred

    @classmethod
    def display_credentials(cls):
        """
        display your credentials list
        """
        return cls.cred_list

    def generate_password():
        '''
        generates random password
        '''
        alphabet = string.ascii_letters + string.digits
        password = ''.join(random.choice(alphabet) for _ in range(8))

        return password