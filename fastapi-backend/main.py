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
from Schedule import Schedule
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
    source_station_set = set()
    province_lst = bus_controller.search_route_by_province(source_province)
    for province in province_lst:
        for route in province.get_route_lst:
            if province.get_province_name == source_province:
                source_station_set.add(route.get_source_station)
    source_station_lst = list(source_station_set)
    return source_station_lst

@app.get('/api/destination_province')
def get_destination_province(source_province, source_station):
    destination_province_set = set()
    province_lst = bus_controller.search_route_by_province(source_province)
    for province in province_lst:
        for route in  province.get_route_lst:
            if province.get_province_name == source_province and route.get_source_station == source_station:
                destination_province_set.add(route.get_destination_province)
    destination_provinces_lst = list(destination_province_set)
    return destination_provinces_lst

@app.get('/api/destination_station')
def get_destination_station(source_province, source_station, destination_province):
    destination_station_set = set()
    province_lst = bus_controller.search_route_by_province(source_province)
    for province in province_lst:
        for route in province.get_route_lst:
            if province.get_province_name == source_province and route.get_source_station == source_station and route.get_destination_province == destination_province:
                destination_station_set.add(route.get_destination_station)
    destination_stations_lst = list(destination_station_set)
    return destination_stations_lst

@app.get('/api/date_trip')
def get_date_trip():
    pass

@app.get('/api/trip')
def get_trip():
    pass

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