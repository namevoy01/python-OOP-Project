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
    def __init__(self, province_lst, ticket_lst, bus_lst, payment_lst, schedule_lst, booking_lst, passenger_lst, admin_lst):
        self.__province_lst = []
        self.__ticket_lst = []
        self.__bus_lst = []
        self.__payment_lst = []
        self.__schedule_lst = []
        self.__booking_lst = []
        self.__passenger_lst = []
        self.__admin_lst = []

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
    
    @property
    def get_passenger_lst(self):
        return self.__passenger_lst
    
    @property
    def get_admin_lst(self):
        return self.__admin_lst
    
    def get_next_station(self, bus_license) :
        pass

    def add_passenger(self, user_id, name, gender, tel, email, status_payment):
        new_passenger = Passenger(user_id, name, gender, tel, email, status_payment)
        self.__passenger_lst.append(new_passenger)
        return new_passenger
        
    def add_admin(self, user_id, username, password, name, gender, tel, email, status_payment) :
        new_admin = Admin(user_id, username, password, name, gender, tel, email, status_payment)
        self.__admin_lst.append(new_admin)
        return new_admin
    
    def add_schedule(self, schedule_id, route, departure_date) :
        route_id = Route.get_route_id
        source_province = self.get_provine_lst
        source_station = Route.get_route_id
        destination_province = Route.get_destination_province
        destination_station = Route.get_destination_station
        route = Route(route_id, source_province, source_station, destination_province,destination_station)
        new_schedule = Schedule(schedule_id, route, departure_date)
        self.__province_lst.append(new_schedule)

    def add_province(self, province) :
        self.__province_lst.append(province)

    def add_bus_trip(self, bustrip_id, bus, schedule) :
        new_booking = Booking(bustrip_id, bus, schedule)
        self.__booking_lst.append(new_booking)

    def add_booking(self, booking_id, name_passenger, payment_option, amount, date, payment, bus_trip_lst) :
        new_booking = Booking(booking_id, name_passenger, payment_option, amount, date, payment, bus_trip_lst)
        self.__booking_lst.append(new_booking)

    def add_bus(self, bus) :
        self.__bus_lst.append(bus)
    
    def add_ticket(self, ticket_id , booking, seat_number):
        new_ticket = Ticket(ticket_id , booking, seat_number)
        self.__ticket_lst.append(new_ticket)

    def search_route_by_province(self, province_name):
        return {(province_name, route.get_source_station, route.get_destination_province, route.get_destination_station) 
                for province in self.__province_lst 
                if province.get_province_name == province_name 
                for route in province.get_route_lst}

    def search_ticket_by_ticket_id(self, ticket_id) :
        return [(ticket.get_ticket_id, ticket.get_schedule, ticket.get_seat_number)
                for ticket in self.__ticket_lst
                if ticket.get_ticket_id == ticket_id]

    def search_bus_by_bus_license(self, bus_license) :
        return [(bus.get_bus_license, bus.get_location,
                [(seat.get_seat_number, seat.get_status_seat) for seat in bus.get_seat_lst])
                for bus in self.__bus_lst
                if bus.get_bus_license == bus_license]

    def comfirm_booking(self, user_id) :
        return

    def cancel_ticket(self, ticket_id, phone_number)  :
        pass

    def check_refund(self, ticket_id, phone_number) :
        pass

    def send_refund_comfirm_email(self, ticket_id, email) :
        pass
