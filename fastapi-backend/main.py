from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from Admin import Admin
from Booking import Booking
from Bus import Bus
from BusTrip import BusTrip
from Passenger import Passenger
from Payment import Payment
from Province import Province
from Route import Route
from Seat import Seat
from Station import Station
from Ticket import Ticket
from User import User
from Instance import create_instance, get_controller
from BusService_Controller import BusService_Controller

app = FastAPI()
bus_controller = get_controller()

# Setup CORS middleware
origins = ["http://localhost:3000"]  # ระบุ domain ของ React Front-end ที่อนุญาตให้เข้าถึง
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

# API endpoint
@app.get('/api/data')
def get_data():
    return data

@app.get('/api/source_province')
def get_source_province():
    source_province = [province.get_province_name for province in bus_controller.get_province_lst]
    return source_province
  
@app.get('/api/source_station')  
def get_source_station(source_province):
    source_station = bus_controller.search_source_station(source_province)
    return source_station

@app.get('/api/destination_province')
def get_destination_province(source_province, source_station):
    destination_province = bus_controller.search_destination_province(source_province, source_station)
    return destination_province

@app.get('/api/destination_station')
def get_destination_station(source_province, source_station, destination_province):
    destination_station = bus_controller.search_destination_station(source_province, source_station,destination_province)
    return destination_station

@app.get('/api/info_trip')
def get_booking(source_province, source_station, destination_province, destination_station, departure_date, departure_time, bus_license, seat_number):
    for trip in bus_controller.get_province_lst:
        if trip.get_province_name == source_province:
            source = source_province
            for route in trip.get_route_lst:
                if route.get_source_station == source_station and route.get_destination_province == destination_province and route.get_destination_station == destination_station:
                    destination = destination_province
                    bus = route.get_bus
                    seat_number = bus_controller.search_seat_by_bus_license_and_seat_number(bus_license, seat_number)
                    departure_time = route.get_departure_time
                    return source, destination, source_station, destination_station, departure_date, departure_time, bus, seat_number

@app.get('/api/trip')
def get_trip(source_province, source_station, destination_province, destination_station, date_time):
    for trip in bus_controller.get_province_lst:
        if trip.get_province_name == source_province:
            source = source_province
            for route in trip.get_route_lst:
                if route.get_source_station == source_station and route.get_destination_province == destination_province and route.get_destination_station == destination_station:
                    destination = destination_province
                    price = route.get_price
                    bus = route.get_bus
                    seat_lst = bus_controller.search_all_seat_by_bus_license(bus)
                    seat = len(seat_lst)
                    departure_time = route.get_departure_time
                    return date_time, bus, source, destination, seat, price, departure_time
                
@app.get('/api/seat')
def get_seat(bus_license):
    bus_lst = bus_controller.search_bus_by_bus_license(bus_license)
    seat_show = []
    for bus in bus_lst:
        for seat in bus.get_seat_lst:
            seat_show.append([seat.get_seat_number, seat.get_status_seat])
    return seat_show

@app.post('/api/seat')
def post_seat():
    pass

@app.post('/api/info')
def post_info():
    pass

@app.get('/api/ticket')
def get_ticket(ticket_id):
    ticket_lst = bus_controller.search_ticket_by_ticket_id(ticket_id)
    ticket_show = []
    for ticket in ticket_lst:
        if ticket.get_ticket_id == ticket_id:
            ticket_show.append([ticket_id, ticket.get_booking, ticket.get_seat_number])
    return ticket_show

@app.put('/api/cancel')
def put_cancel():
    pass