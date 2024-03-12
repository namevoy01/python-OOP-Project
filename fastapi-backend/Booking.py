class Booking:
    booking_id = 155010
    def __init__(self, name_passenger, payment_option, amount, date):
        Booking.booking_id += 1
        self.__booking_id  = Booking.booking_id 
        self.__name_passenger = name_passenger
        self.__payment_option = payment_option
        self.__amount = amount
        self.__date = date
        self.__bus_trip_lst = []
    
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
    def get_bus_trip_lst(self):
        return self.__bus_trip_lst
    
    def add_bus_trip(self, bus, booking) :
        new_booking = Booking(bus, booking)
        self.__booking_lst.append(new_booking)
