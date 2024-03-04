from User import User

class Passenger(User) :
    def __init__(self, account_number, email):
        self.__account_number= account_number
        self.__email = email
 
    @property
    def get_account_number(self):
        return self.__account_number
    
    @property
    def get_email(self):
        return self.__email
    