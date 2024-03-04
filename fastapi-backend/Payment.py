class Payment:
    def __init__(self, payment_id, person_id, payment_date):
        self.__payment_id  = payment_id
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