import secrets
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
    def credentials_exist(cls):
        '''
        Check if user_name exists
        Args:
            system_username: username to be searched for.
        Return:
            Boolean True or false
        '''
        for cred in cls.cred_list:
            if cred.system_username == cls.system_username:
                return True
            else:
                return False 

    @classmethod
    def display_credentials(cls):
        """
        display your credentials list
        """
        return cls.cred_list

    def generate_password(self):
        '''
        generates random password
        '''
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))

        return password