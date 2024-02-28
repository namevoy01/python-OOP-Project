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
from BusService_Controller import BusService_Controller

bus_controller = BusService_Controller()

def get_bus_controller():
    return bus_controller

def create_instance():

    # Create province
    province1 = Province("province_id_1", "Bangkok", [])
    province2 = Province("province_id_2", "Chonburi", [])
    province3 = Province("province_id_3", "Rayong", [])
    bus_controller.add_province(province1)
    bus_controller.add_province(province2)
    bus_controller.add_province(province3)

    # Create station
    station1 = Station("station_id_1", "หมอชิต")
    station2 = Station("station_id_2", "เอกมัย")
    station3 = Station("station_id_3", "สวนสนุก")
    station4 = Station("station_id_4", "บางแสน")
    station5 = Station("station_id_5", "สุราษฎร์ธานี")
    station6 = Station("station_id_6", "บ้านฉาง")

    # Create route
    route1 = Route(station1, station2, [])
    route2 = Route(station1, station3, [])
    route3 = Route(station1, station4, [])
    route4 = Route(station1, station5, [])
    route5 = Route(station1, station6, [])
    bus_controller.add_route(route1)
    bus_controller.add_route(route2)
    bus_controller.add_route(route3)
    bus_controller.add_route(route4)
    bus_controller.add_route(route5)

    # Create buse
    bus1 = Bus("license_bus_1", ["seat1", "seat2", "seat3"], "location")
    bus2 = Bus("license_bus_2", ["seat4", "seat5", "seat6"], "location")
    bus_controller.add_bus(bus1)
    bus_controller.add_bus(bus2)

    # Create schedule
    schedule1 = Schedule("schedule_id_1", route1, "2024-03-01")
    schedule2 = Schedule("schedule_id_2", route1, "2024-03-02")
    bus_controller.add_schedule(schedule1)
    bus_controller.add_schedule(schedule2)

    # Create booking
    booking1 = Booking("booking_id_1", "passenger_name_1", "payment_option_1", 100, "2024-03-01", Payment("payment_id_1", "2024-03-01", "person_id_1"))
    booking2 = Booking("booking_id_2", "passenger_name_2", "payment_option_2", 150, "2024-03-02", Payment("payment_id_2", "2024-03-02", "person_id_2"))
    bus_controller.add_booking(booking1)
    bus_controller.add_booking(booking2)

    # Create ticket
    ticket1 = Ticket("ticket_id_1", schedule1, "seat1")
    ticket2 = Ticket("ticket_id_2", schedule2, "seat2")

    # Create bus trip
    bus_trip1 = BusTrip("bustrip_id_1", bus1, schedule1)
    bus_trip2 = BusTrip("bustrip_id_2", bus2, schedule2)

    # Create seat
    seat1 = Seat("seat_number_1", "status_seat_1")
    seat2 = Seat("seat_number_2", "status_seat_2")

    return bus_controller

bus_controller = create_instance()