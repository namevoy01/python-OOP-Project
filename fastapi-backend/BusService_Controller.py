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
    def __init__(self, province_lst, ticket_lst, bus_lst, payment_lst, schedule_lst, booking_lst):
        self.__province_lst = []
        self.__ticket_lst = []
        self.__bus_lst = []
        self.__payment_lst = []
        self.__schedule_lst = []
        self.__booking_lst = []

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
    
    @property
    def get_booking_lst(self):
        return self.__booking_lst
    
    def get_booked_seat(self, bus_license, seat_number):
        for bus in self.bus_lst:
            if bus.get_license == bus_license:
                for trip in bus.get_trip_lst:
                    for schedule in trip.get_schedule_lst:
                        for seat in schedule.get_seat_lst:
                            if seat.get_seat_number == seat_number:
                                seat.set_status(False)
                                return

    def get_next_station(self, bus_license) :
        pass

    def add_province(self, province) :
        self.__province_lst.append(province)

    def add_booking(self, booking_id, name_passenger, payment_option, amount, date, payment) :
        new_booking = Booking(booking_id, name_passenger, payment_option, amount, date, payment)
        self.__booking_lst.append(new_booking)

    def add_bus(self, bus) :
        self.__bus_lst.append(bus)

    def add_passenger_to_bus(self, booking_id, schedule, seat_number) :
        pass

    def search_route_by_province(self, province_name):
        return {(route.get_destination_province, route.get_destination_station) 
                for province in self.__province_lst 
                if province.get_province_name == province_name 
                for route in province.get_route_lst}

    def search_ticket_by_ticket_id(self, ticket_id) :
        return {(ticket.get_ticket_id, ticket.get_schedule, ticket.get_seat_number)
                for ticket in self.__ticket_lst
                if ticket.get_ticket_id == ticket_id
                for ticket in ticket.get_ticket_lst}

    def add_ticket(self, ticket_id , booking, seat_number):
        new_ticket = Ticket(ticket_id , booking, seat_number)
        self.__ticket_lst.append(new_ticket)

    def search_bus_by_bus_license(self, bus_license) :
        pass

    def search_station_by_province(self, province_id) :
        pass

    def comfirm_booking(self, ticket_id) :
        pass

    def cancel_ticket(self, ticket_id, phone_number)  :
        pass

    def check_refund(self, ticket_id, phone_number) :
        pass

    def send_refund_comfirm_email(self, ticket_id, email) :
        pass

    def  calculate_ticekt_price(self, distance) :
        pass
