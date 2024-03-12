from datetime import datetime

class Payment:
    payment_id = 0
    def __init__(self, name_passenger):
        Payment.payment_id += 1
        self.__payment_id  = Payment.payment_id
        self.__name_passenger = name_passenger
        self.__payment_date = datetime.now()
        
    @property
    def get_payment_id (self):
        return self.__payment_id
    
    @property
    def get_name_passenger(self):
        return self.__name_passenger
    
    @property
    def get_payment_date(self):
        return self.__payment_date