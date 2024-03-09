class Payment:
    payment_id = 0
    def __init__(self, person_id, payment_date):
        Payment.payment_id += 1
        self.__payment_id  = Payment.apayment_id
        self.__person_id = person_id
        self.__payment_date = payment_date
        
    @property
    def get_payment_id (self):
        return self.__payment_id
    @property
    def get_person_id(self):
        return self.__person_id
    @property
    def get_payment_date(self):
        return self.__payment_date