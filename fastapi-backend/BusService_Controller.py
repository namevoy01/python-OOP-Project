from Admin import Admin
from Booking import Booking
from Bus import Bus
from BusTrip import BusTrip
from Passenger import Passenger
from Payment import Payment
from Province import Province
from Route import Route
from Seat import Seat
from Ticket import Ticket
from User import User

class BusService_Controller :
    def __init__(self):
        self.__province_lst = []
        self.__ticket_lst = []
        self.__bus_lst = []
        self.__payment_lst = []
        self.__passenger_lst = []
        self.__admin_lst = []
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
    def get_admin_lst(self):
        return self.__admin_lst
    
    @property
    def get_bus_trip_lst(self):
        return self.__bus_trip_lst

    def add_passenger(self, name_passenger, surname_passenger, gender, tel, email, status_payment):
        new_passenger = Passenger(name_passenger, surname_passenger, gender, tel, email, status_payment)
        self.__passenger_lst.append(new_passenger)
        
    def add_admin(self, username, password, name_passenger, surname_passenger, gender, tel) :
        new_admin = Admin(username, password, name_passenger, surname_passenger, gender, tel)
        self.__admin_lst.append(new_admin)
        return self.__admin_lst
    
    def add_booking(self, name_passenger, surname_passenger, gender, tel, email, status_payment, payment_option, amount, time_reserve, bus_license, seat_number, source_province, source_station, destination_province, destination_station, departure_date):
        seat = self.search_seat_number_and_status_seat_by_seat(bus_license, seat_number)
        bus_trip = self.add_bus_trip(bus_license, source_province, source_station, destination_province, destination_station, departure_date)
        booking = Booking(name_passenger, payment_option, amount, departure_date, time_reserve, bus_trip, seat)
        self.add_passenger(name_passenger, surname_passenger, gender, tel, email, status_payment)
        passenger_lst = self.search_passenger_by_name_passenger(name_passenger, surname_passenger)
        passenger_lst.get_booking_lst.append(booking)
        return passenger_lst
        
    def add_province(self, province) :
        self.__province_lst.append(province)

    def add_bus(self, bus) :
        self.__bus_lst.append(bus)
        
    def add_payment(self, payment):
        self.__payment_lst.append(payment)
        
    def add_bus_trip(self, bus_license, source_province, source_station, destination_province, destination_station, departure_date):
        bus = Bus(self.search_bus_by_bus_license(bus_license))
        province = Province(source_province)
        source_station = self.search_source_station_by_route(source_province, source_station, destination_province, destination_station)
        destination_province = self.search_destination_province_by_route(source_province, source_station, destination_province, destination_station)
        destination_station = self.search_destination_station_by_route(source_province, source_station, destination_province, destination_station)
        departure_time = self.search_departure_time_by_route(source_province, source_station, destination_province, destination_station)
        price = self.search_price_by_route(source_province, source_station, destination_province, destination_station)
        route = Route(source_station, destination_province, destination_station, price, bus, departure_time)
        bus_trip = BusTrip(bus, province, route, departure_date)
        self.__bus_trip_lst.append(bus_trip)
        return bus_trip
    
    def add_ticket(self, name_passenger):
        new_ticket = Ticket(name_passenger)
        for passenger in self.__passenger_lst:
            if passenger.get_name_passenger == name_passenger:
                surname_passenger = passenger.get_surname_passenger
        self.payment(name_passenger, surname_passenger)
        self.change_status_seat_when_passenger_has_paid(name_passenger, surname_passenger)
        self.__ticket_lst.append(new_ticket)
        return self.__ticket_lst
    
    def search_bus_by_bus_license(self, bus_license):
        for bus in self.__bus_lst:
            if bus.get_bus_license == bus_license:
                return bus
    
    def search_passenger_by_name_passenger(self, name_passenger, surname_passenger):
        for passenger in self.__passenger_lst:
            if passenger.get_name_passenger == name_passenger and passenger.get_surname_passenger == surname_passenger:
                return passenger

    def search_source_station(self, source_province):
        source_station_set = set()
        province = self.search_province_by_province(source_province)
        for route in province.get_route_lst:
            if province.get_province_name == source_province:
                source_station_set.add(route.get_source_station)
        source_station_lst = list(source_station_set)
        return source_station_lst
    
    def search_destination_province(self, source_province, source_station):
        destination_province_set = set()
        province = self.search_province_by_province(source_province)
        for route in province.get_route_lst:
            if province.get_province_name == source_province and route.get_source_station == source_station:
                destination_province_set.add(route.get_destination_province)
        destination_province_lst = list(destination_province_set)
        return destination_province_lst
    
    def search_destination_station(self, source_province, source_station, destination_province):
        destination_station_set = set()
        province = self.search_province_by_province(source_province)
        for route in province.get_route_lst:
            if province.get_province_name == source_province and route.get_source_station == source_station and route.get_destination_province == destination_province:
                destination_station_set.add(route.get_destination_station)
        destination_stations_lst = list(destination_station_set)
        return destination_stations_lst
    
    def search_province_by_province(self, province_name):
        for province in self.__province_lst:
            if province.get_province_name == province_name:
                return province
    
    def search_route_by_province(self, province_name):
        province = self.search_province_by_province(province_name)
        for route in province.get_route_lst:
            return route
    
    def search_ticket_by_ticket_id(self, ticket_id) :
        for ticket in self.__ticket_lst:
            if ticket.get_ticket_id == ticket_id:
                return ticket
            
    def search_booking_by_name_passenger(self, name_passenger, surname_passenger) :
        for passenger in self.__passenger_lst:
            if passenger.get_name_passenger == name_passenger and passenger.get_surname_passenger == surname_passenger:
                for booking in passenger.get_booking_lst:
                    return booking
                
    def search_bus_trip_by_name_passenger(self, name_passenger, surname_passenger):
        booking = self.search_booking_by_name_passenger(name_passenger, surname_passenger)
        bus_trip = booking.get_bus_trip
        return bus_trip
           
    def search_all_seat_by_bus_license(self, bus_license):
        seat_lst = []
        for bus in self.__bus_lst:
            for seat in bus.get_seat_lst:
                if seat.get_status_seat == True:
                    seat_lst.append((seat.get_seat_number, seat.get_status_seat))
            return seat_lst
    
    def search_seat_lst_by_bus_license(self, bus_license):
        bus = self.search_bus_by_bus_license(bus_license)
        for seat in bus.get_seat_lst:
            return seat
                    
    def search_price_by_route(self, source_province, source_station, destination_province, destination_station):
        province = self.search_province_by_province(source_province)
        if province.get_province_name == source_province:
            for route in province.get_route_lst:
                if route.get_source_station == source_station and route.get_destination_province == destination_province and route.get_destination_station == destination_station:
                    return route.get_price
    
    def search_source_station_by_route(self, source_province, source_station, destination_province, destination_station):
        province = self.search_province_by_province(source_province)
        for route in province.get_route_lst:
            if route.get_source_station == source_station and route.get_destination_province == destination_province and route.get_destination_station == destination_station:
                return source_station
                    
    def search_destination_province_by_route(self, source_province, source_station, destination_province, destination_station):
        province = self.search_province_by_province(source_province)
        for route in province.get_route_lst:
            if route.get_source_station == source_station and route.get_destination_province == destination_province and route.get_destination_station == destination_station:
                return destination_province
        
    def search_destination_station_by_route(self, source_province, source_station, destination_province, destination_station):
        province = self.search_province_by_province(source_province)
        for route in province.get_route_lst:
            if route.get_source_station == source_station and route.get_destination_province == destination_province and route.get_destination_station == destination_station:
                return destination_station
                    
    def search_departure_time_by_route(self, source_province, source_station, destination_province, destination_station):
        province = self.search_province_by_province(source_province)
        for route in province.get_route_lst:
            if route.get_source_station == source_station and route.get_destination_province == destination_province and route.get_destination_station == destination_station:
                return route.get_departure_time 
     
    def search_seat_number_and_status_seat_by_seat(self, bus_license, seat_number):
        bus = self.search_bus_by_bus_license(bus_license)
        for seat in bus.get_seat_lst:
            if seat.get_seat_number == seat_number:
                return seat
        
    def payment(self, name_passenger, surname_passenger) :
        passenger = self.search_passenger_by_name_passenger(name_passenger, surname_passenger)
        if passenger.get_name_passenger == name_passenger:
            passenger.set_status_payment(False)
            return passenger.get_status_payment
                           
    def change_status_seat_when_passenger_has_paid(self, name_passenger, surname_passenger):
        booking = self.search_booking_by_name_passenger(name_passenger, surname_passenger)
        seat = booking.get_seat
        seat.set_status_seat(False)
        return seat.get_status_seat

    def get_seat(self, bus_license):
        id = 0
        info_seat = []
        bus = self.search_bus_by_bus_license(bus_license)
        for seat in bus.get_seat_lst:
            id += 1
            info_seat.append({
            'id': id, 
            'seat_number': seat.get_seat_number,
            'status_seat': seat.get_status_seat
            })
        return info_seat

    def get_trip(self, source_province, source_station, destination_province, destination_station, departure_date):
        id = 0
        info_trip = []
        for bus in self.__bus_lst:
            for province in self.get_province_lst:
                for route in province.get_route_lst:
                    source_province = province.get_province_name
                    seat_empty = self.search_all_seat_by_bus_license(bus.get_bus_license)
                    count_seat = len(seat_empty)
                    if route.get_source_station == source_station and route.get_destination_province == destination_province and route.get_destination_station == destination_station:
                        self.add_bus_trip(bus.get_bus_license, source_province, source_station, destination_province, destination_station, departure_date)
                        departure_time = route.get_departure_time
                        price = route.get_price
                        id += 1
                        info_trip.append({
                        'id': id, 
                        'source_province': source_province,
                        'destination_province': destination_province,
                        'source_station': source_station,
                        'destination_station': destination_station,
                        'departure_date': departure_date,
                        'departure_time': departure_time,
                        'bus_license': bus.get_bus_license,
                        'count_seat': count_seat,
                        'price' : price
                    })
                return info_trip
    
    def get_info_on_booking(self, source_province, source_station, destination_province, destination_station, departure_date, departure_time, bus_license, seat_number):
        id = 0
        info_in_booking = []
        for trip in self.get_bus_trip_lst:
            bus = trip.get_bus
            route = trip.get_route
            if route.get_source_station == source_station and route.get_destination_province == destination_province and route.get_destination_station == destination_station:
                seat = self.search_seat_lst_by_bus_license(bus_license)
                status_seat = seat.get_status_seat
                departure_time = route.get_departure_time
                self.add_bus_trip(bus.get_bus_license, source_province, source_station, destination_province, destination_station, departure_date)
                id += 1
                info_in_booking.append({
                    'id': id, 
                    'source_province': source_province,
                    'destination_province': destination_province,
                    'source_station': source_station,
                    'destination_station': destination_station,
                    'departure_date': departure_date,
                    'departure_time': departure_time,
                    'bus_license': bus_license,
                    'seat_number' : seat_number,
                    'seat_status' : status_seat,
                })
            return info_in_booking
    
    def cancel_ticket(self, ticket_id):
        for ticket in self.__ticket_lst:
            if str(ticket.get_ticket_id) == ticket_id:
                name_passenger = ticket.get_name_passenger
                for passenger in self.__passenger_lst:
                    surname_passenger = passenger.get_surname_passenger
                    bus_trip = self.search_bus_trip_by_name_passenger(name_passenger, surname_passenger)
                    booking = self.search_booking_by_name_passenger(name_passenger, surname_passenger)
                    seat = booking.get_seat
                    self.get_ticket_lst.remove(ticket)
                    passenger.get_booking_lst.remove(booking)
                    self.get_bus_trip_lst.remove(bus_trip)
                    self.get_passenger_lst.remove(passenger)
                    passenger.set_status_payment(True)
                    seat.set_status_seat(True)
                    return ticket.get_ticket_id
                
    def login_for_admin(self, username, password):
        id = 0
        info_admin = []
        for admin in self.__admin_lst:
            if admin.get_username == username and admin.get_password == password:
                info_admin.append({
                    'username' : username,
                    'password' : password
                })
            return info_admin
            
    def get_schedule_info(self):
        id = 0
        info_schedule = []
        for bus in self.__bus_lst:
            for province in self.__province_lst:
                for route in province.get_route_lst:
                    id += 1
                    info_schedule.append({
                        'id': id, 
                        'bus_license': bus.get_bus_license,
                        'source_province': province.get_province_name,
                        'destination_province': route.get_destination_province,
                        'departure_time': route.get_departure_time
                    })
                return info_schedule
            
    def get_search_ticket(self, ticket_id):
        id = 0
        info_ticket = []
        for ticket in self.get_ticket_lst:
            if str(ticket.get_ticket_id) == str(ticket_id):
                name_passenger = ticket.get_name_passenger
                for passenger in self.__passenger_lst:
                    surname_passenger = passenger.get_surname_passenger
                    bus_trip = self.search_bus_trip_by_name_passenger(name_passenger, surname_passenger)
                    province = bus_trip.get_province
                    route = bus_trip.get_route
                    bus_lst = bus_trip.get_bus
                    bus = bus_lst.get_bus_license
                    id += 1
                    info_ticket.append({
                        'id': id, 
                            'ticket_id': ticket_id,
                            'bus_license': bus.get_bus_license,
                            'source_province': province.get_province_name,
                            'destination_province': route.get_destination_province,
                            'source_station' : route.get_source_station,
                            'destination_station' : route.get_destination_station,
                            'departure_time': route.get_departure_time,
                            'name_passenger' : name_passenger,
                            'surname_passenger' : passenger.get_surname_passenger,
                            'status_payment' : passenger.get_status_payment,
                            'tel' : passenger.get_tel,
                            'email' : passenger.get_email
                    })
                return info_ticket
        
    def return_ticket(self, name_passenger, surname_passenger, time_reserve):
        for passenger in self.__passenger_lst:
            if passenger.get_name_passenger == name_passenger and passenger.get_surname_passenger == surname_passenger:
                for booking in passenger.get_booking_lst:
                    # print(booking.get_time_reserve, str(time_reserve))
                    # return type(booking.get_time_reserve), type(str(time_reserve))
                    if booking.get_time_reserve == str(time_reserve):
                        for ticket in self.__ticket_lst:
                            if ticket.get_name_passenger == name_passenger:
                                return ticket.get_ticket_id