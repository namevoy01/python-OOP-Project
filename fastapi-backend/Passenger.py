from User import User
from Booking import Booking
# from BusService_Controller import BusService_Controller

class Passenger(User) :
    def __init__(self, user_id, name, gender, tel, account_number, email, status_payment=False):
        super().__init__(user_id, name, gender, tel)
        self.__account_number= account_number
        self.__email = email
        self.__status_payment = status_payment
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
    
    def set_status_payment(self, status):
        self.__status_payment = status
        
    # def add_booking(self, name_passenger, payment_option, amount, date, bus_license, source_province, source_station, destination_province, destination_station, bus_trip):
    #     bus_trip = BusService_Controller.add_bus_trip(bus_license, source_province, source_station, destination_province, destination_station)
    #     booking = Booking(name_passenger, payment_option, amount, date, bus_trip)
    #     self.__booking_lst.append(booking)
    #     return booking