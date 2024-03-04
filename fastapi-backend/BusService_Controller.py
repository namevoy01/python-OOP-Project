from Admin import Admin
from Booking import Booking
from Bus import Bus
from BusTrip import BusTrip
from Passenger import Passenger
from Payment import Payment
from Province import Province
from Route import Route
from Schedule import Schedule
from Seat import Seat
from Station import Station
from Ticket import Ticket
from User import User

class BusService_Controller :
    def __init__(self, province_lst, ticket_lst, bus_lst, payment_lst, schedule_lst):
        self.__province_lst = []
        self.__ticket_lst = []
        self.__bus_lst = []
        self.__payment_lst = []
        self.__schedule_lst = []

    @property
    def get_province_lst(self):
        return self.__province_lst
    
    @property
    def get_ticket_lst(self):
        return self.__ticket_lst
    
    @property
    def get_bus_lst(self):
        return self.__bus_lst
    
    @property
    def get_payment_lst(self):
        return self.__payment_lst
    
    @property
    def get_schedule_lst(self):
        return self.__schedule_lst
    
    def get_booked_seat(self, bus_license, seat_number, seat_status) :
        pass

    def get_next_station(self, bus_license) :
        pass

    def add_province(self, province) :
        self.__province_lst.append(province)

    def add_booking(self, booking_id, passenger_name, payment_option, amount) :
        pass

    def add_bus(self) :
        self.__bus_lst.append()
    
    def add_route(self, route):
        self.__route_lst.append(route)

    def add_passenger_to_bus(self, booking_id, schedule, seat_number) :
        pass

    def adjust_status_seat(self) :
        pass

    def add_passenger_to_bus(self, booking_id, schedule, seat_number) :
        pass

    def comfirm_booking(self, ticket_id) :
        pass

    def cancel_ticket(self, ticket_id, phone_number)  :
        pass

    def check_refund(self, ticket_id, phone_number) :
        pass

    def send_refund_comfirm_email(self, ticket_id, email) :
        pass

    def search_route_by_province(self, province_id, route) :
        pass

    def search_ticket_by_ticket_id(self, ticket_id) :
        pass

    def search_bus_by_bus_license(self, bus_license) :
        pass

    def search_station_by_province(self, province_id) :
        pass

    def  calculate_ticekt_price(self, distance) :
        pass