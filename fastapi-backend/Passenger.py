from User import User

class Passenger(User):
    def __init__(self, name_passenger, surname_passenger, gender, tel, email, account_number):
        super().__init__(name_passenger, surname_passenger, gender, tel)
        self.__account_number = account_number
        self.__email = email
        self.__status_payment = True
        self.__booking_lst = []

    @property
    def get_account_number(self):
        return self.__account_number

    @property
    def get_email(self):
        return self.__email

    @property
    def get_status_payment(self):
        return self.__status_payment
    
    @property
    def get_booking_lst(self):
        return self.__booking_lst

    def set_status_payment(self, status):
        self.__status_payment = status
        