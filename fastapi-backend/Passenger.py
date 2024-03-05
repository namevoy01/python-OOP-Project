from User import User

class Passenger(User) :
    def __init__(self, user_id, name, gender, tel, account_number, email, status_payment=False):
        super().__init__(user_id, name, gender, tel)
        self.__account_number= account_number
        self.__email = email
        self.__status_payment = status_payment
 
    @property
    def get_account_number(self):
        return self.__account_number
    
    @property
    def get_email(self):
        return self.__email
    
    @property
    def get_status_payment(self):
        return self.__status_payment