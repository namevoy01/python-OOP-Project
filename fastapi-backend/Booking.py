class Booking:
    def __init__(self, booking_id, name_passenger, payment_option, date, payment):
        self.__booking_id  = booking_id 
        self.__name_passenger = name_passenger
        self.__payment_option = payment_option
        self.__date = date
        self.__payment = payment
    
    @property
    def booking_id (self):
        return self.__booking_id 
    @property
    def name_passenger(self):
        return self.__name_passenger
    @property
    def payment_option(self):
        return self.__payment_option
    @property
    def date(self):
        return self.__date
    @property
    def payment(self):
        return self.__payment
