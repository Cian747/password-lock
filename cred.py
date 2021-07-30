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
 
