from User import User

class Passenger(User) :
    def __init__(self, account_number, email):
        self.__account_number= account_number
        self.__email = email
 
    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def email(self):
        return self.__email
    