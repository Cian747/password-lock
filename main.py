#!/usr/bin/env python3.9
from user import User
from cred import Credentials

def sign_up(f_name,l_name,us_name,pass_word):
    '''
    Function to create an account
    '''
    new_user = User(f_name,l_name,us_name,pass_word)
    return new_user

def create_credential(new_username,new_password,sys_username,account_name):
    '''
    create a credential
    '''
    new_cred = Credentials(new_username,new_password,sys_username,account_name)
    return new_cred

def save_credential(cred):
    '''
    add credentials of accounts
    '''
    Credentials.add_credentials(cred)



def validate_credential(cred):
    '''
    Search for your username
    '''
    return Credentials.credentials_exist(cred)


def find_credential(cred):
    '''
    Finds the username
    '''
    return Credentials.search_credentials(cred)


def get_password():
    '''
    Get your generated password
    '''
    return Credentials.generate_password()

def save_user(user):
    '''
    save your account upon login
    '''
    User.save_user(user)

def delete_cred(cred):
    '''
    Delete credentials
    '''
    Credentials.delete_cred(cred)

def show_cred():
    '''
    View the credentials you have created
    '''
    return Credentials.display_credentials()



def main():
    print("Hello welcome to Grid lock. What's your name?")
    u_name = input()

    print(f"Hey {u_name}. How would you like to proceed?: ")
    print("\n")

    while True:
        print("use these short codes: ss == Sign up to Grid ,cc == create credential account, dc == display credentials, rm == delete credentials, ex == Exit" )

        short_code = input().lower()
            
        if short_code == "ss":
                print("Sign up")
                print("-"*10)

                print ("First name ....")
                f_name = input()

                print("Last name ...")
                l_name = input()

                print("new user_name ...")
                us_name = input()

                print("password ...")
                pass_word = input() 
                print("\n")


                save_user(sign_up(f_name,l_name,us_name,pass_word))

                print("Account created")
                print("-"*5)
                print(f"Grid: User name: {us_name} ")
                print("-"*5)
                print(f"Grid; Password: {pass_word}")
                print("-"*20)

        elif short_code == "cc":
            print("Create credential account")
            print("-"*20)

            print("Enter Grid user-name")
            print("-"*10)
            sys_username = input()
            print("Enter the username you'll create for the host account: ")
            print("-"*10)
            new_username = input()
            print("Account password: ")
            print("-"*5)
            print("To generate password type - ga")
            gen_rate = input().lower()

            if gen_rate == "ga":
                new_password = get_password()
                print(new_password)
            else:
                print("Type in yours") 
                print("-"*10)
                new_password = input()
            print("Account being made for? i.e Instagram,Twitter,Facebook: ")
            print("-"*10)
            account_name = input() 

            save_credential(create_credential(new_username,new_password,sys_username,account_name)) #created a credential


        elif short_code == "rm":
            print("Kindly enter your Grid username")
            said_name = str(input())
            if validate_credential(said_name):
                print("Please input user name for account you would like to delete: ")
                name_input = str(input()) 
                obtained_input = find_credential(name_input)
                delete_cred(obtained_input)
                    
            print("Account has been deleted")
            print("-"*20)

        elif short_code == "dc":
            print("Kindly enter your Grid username: ")
            said_name = str(input())
            if validate_credential(said_name):
                for credential in Credentials.cred_list:
                    print(f"Account name: {credential.account_name}.....Username: {credential.user_name}....Password: {credential.password}")
                    print("\n")


        elif short_code == "ex":
            print("Hope I helped. Goodbye....")
            break
        else:

            print("Please input a proper short code.")


if __name__ == '__main__':
    main()            
