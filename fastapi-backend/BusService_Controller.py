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
    def __init__(self, province_lst, ticket_lst, bus_lst, payment_lst, passenger_lst, admin_lst, schedule_lst, bus_trip_lst):
        self.__province_lst = []
        self.__ticket_lst = []
        self.__bus_lst = []
        self.__payment_lst = []
        self.__passenger_lst = []
        self.__admin_lst = []
        self.__schedule_lst = []
        self.__bus_trip_lst = []

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
    def get_passenger_lst(self):
        return self.__passenger_lst
    
    @property
    def get_schedule_lst(self):
        return self.__schedule_lst
    
    @property
    def get_admin_lst(self):
        return self.__admin_lst
    
    @property
    def get_bus_trip_lst(self):
        return self.__bus_trip_lst
    
    def get_next_station(self, bus_license) :
        pass

    def add_passenger(self, user_id, name, gender, tel, email, status_payment):
        new_passenger = Passenger(user_id, name, gender, tel, email, status_payment)
        self.__passenger_lst.append(new_passenger)
        return self.__passenger_lst
        
    def add_admin(self, user_id, username, password, name, gender, tel, email, status_payment) :
        new_admin = Admin(user_id, username, password, name, gender, tel, email, status_payment)
        self.__admin_lst.append(new_admin)
        return self.__admin_lst
    
    def add_schedule(self, route, departure_date):
        new_schedule = Schedule(route, departure_date)
        self.__schedule_lst.append(new_schedule)
        return new_schedule
        
    def add_province(self, province) :
        self.__province_lst.append(province)

    def add_bus(self, bus) :
        self.__bus_lst.append(bus)
        
    def add_bus_trip(self, bus_license, province_name):
        bus = self.search_bus_by_bus_license(bus_license)
        province = self.search_route_by_province(province_name)
        bus_trip = BusTrip(bus, province)
        self.__bus_trip_lst.append(bus_trip)
        return self.__bus_trip_lst
    
    def add_ticket(self, booking, seat_number):
        new_ticket = Ticket(booking, seat_number)
        self.__ticket_lst.append(new_ticket)
        return self.__ticket_lst

    def search_source_station(self, source_province):
        source_station_set = set()
        province_lst = self.search_route_by_province(source_province)
        for province in province_lst:
            for route in province.get_route_lst:
                if province.get_province_name == source_province:
                    source_station_set.add(route.get_source_station)
        source_station_lst = list(source_station_set)
        return source_station_lst
    
    def search_destination_province(self, source_province, source_station):
        destination_province_set = set()
        province_lst = self.search_route_by_province(source_province)
        for province in province_lst:
            for route in province.get_route_lst:
                if province.get_province_name == source_province and route.get_source_station == source_station:
                    destination_province_set.add(route.get_destination_province)
        destination_province_lst = list(destination_province_set)
        return destination_province_lst
    
    def search_destination_station(self, source_province, source_station, destination_province):
        destination_station_set = set()
        province_lst = self.search_route_by_province(source_province)
        for province in province_lst:
            for route in province.get_route_lst:
                if province.get_province_name == source_province and route.get_source_station == source_station and route.get_destination_province == destination_province:
                    destination_station_set.add(route.get_destination_station)
        destination_stations_lst = list(destination_station_set)
        return destination_stations_lst
    
    def search_route_by_province(self, province_name):
        for province in self.__province_lst:
            if province.get_province_name == province_name:
                return [province]
            
    def search_ticket_by_ticket_id(self, ticket_id) :
        for ticket in self.__ticket_lst:
            if ticket.get_ticket_id == ticket_id:
                return [ticket]
            
    def search_booking_by_name_passenger(self, name_passenger) :
        for passenger in self.__passenger_lst:
            if passenger.get_name_passenger == name_passenger:
                return [passenger]

    def search_bus_by_bus_license(self, bus_license) :
        for bus in self.__bus_lst:
            if bus.get_bus_license == bus_license:
                return bus
                
    def search_get_route_in_trip_by_province(self, province):
        for trip in self.__bus_trip_lst:
            province_info = trip.get_province
            for province in province_info :
                for route in province.get_route_lst :
                    return [province, route]
                
    def search_get_bus_in_trip_by_bus_license(self, bus_license):
        for trip in self.__bus_trip_lst:
            bus_info = trip.get_bus
            return [bus_info]

    def return_route(self, name_passenger, province_name):
        search_province_in_trip = self.search_get_route_in_trip_by_province(province_name)
        for route in search_province_in_trip:
            return province_name, route.get_source_station, route.get_destination_province, route.get_destination_station

    def return_bus(self, name_passenger, bus_license):
        search_bus_in_trip = self.search_get_bus_in_trip_by_bus_license(bus_license)
        for bus in search_bus_in_trip:
            for seat in bus.get_seat_lst:
                return bus.get_bus_license, seat.get_seat_number
                

    def comfirm_booking(self, user_id) :
        return

    def cancel_ticket(self, ticket_id, phone_number)  :
        pass

    def check_refund(self, ticket_id, phone_number) :
        pass

    def send_refund_comfirm_email(self, ticket_id, email) :
        pass
