class User:
    """
     Created user class that will store all the data upon login
    """

    pass

    user_list = [] #List that will contain the user's input details

    def __init__(self,first_name,last_name,user_name,password):
          """
          Initialized an object with self and the parameters it will use.
        
          Args:
          first_name: New User first name.
          last_name: New User last name.
          user_name: New User user name.
          password: New User password.
        
          """  

          self.first_name = first_name
          self.last_name = last_name
          self.user_name = user_name
          self.password = password


    def save_user(self):
        '''
        save the user input details
        '''

        User.user_list.append(self)

    def save_multiple_user(self):
        '''
        save multiple users
        '''
        
