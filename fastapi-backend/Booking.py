class Booking:
    def __init__(self, booking_id, name_passenger, payment_option, amount, date, payment):
        self.__booking_id  = booking_id 
        self.__name_passenger = name_passenger
        self.__payment_option = payment_option
        self.__amount = amount
        self.__date = date
        self.__payment = payment
    
    @property
    def get_booking_id (self):
        return self.__booking_id 
    @property
    def get_name_passenger(self):
        return self.__name_passenger
    @property
    def get_payment_option(self):
        return self.__payment_option
    @property
    def get_amount(self):
        return self.__amount
    @property
    def get_date(self):
        return self.__date
    @property
    def get_payment(self):
        return self.__payment
