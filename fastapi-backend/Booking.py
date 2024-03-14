from datetime import datetime

class Booking:
    booking_id = 1552010
    def __init__(self, name_passenger, payment_option, amount, departure_date, time_reserve, bus_trip, seat):
        Booking.booking_id += 1
        self.__booking_id  = Booking.booking_id 
        self.__name_passenger = name_passenger
        self.__payment_option = payment_option
        self.__amount = amount
        self.__departure_date = departure_date
        self.__time_reserve = datetime.now().strftime("%H:%M")
        self.__bus_trip = bus_trip
        self.__seat = seat
    
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
    def get_departure_date(self):
        return self.__departure_date
    
    @property
    def get_time_reserve(self):
        return self.__time_reserve
    
    @property
    def get_bus_trip(self):
        return self.__bus_trip
    
    @property
    def get_seat(self):
        return self.__seat
