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
from Instance import create_instance,get_controller
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
def get_source_station():
    route_list = bus_controller.search_route_by_province('กรุงเทพมหานคร')
    for province_name, source_station, destination_province, destination_station in route_list:
        return source_station

@app.get('/api/destination_province')
def get_destination_province():
    destination_province_set = set()
    route_list = bus_controller.search_route_by_province('กรุงเทพมหานคร')
    for route in route_list:
        province_name, source_station, destination_province, destination_station = route
        if source_station == 'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)':
            destination_province_set.add(destination_province)
    destination_provinces_lst = list(destination_province_set)
    return destination_provinces_lst

@app.get('/api/destination_station')
def get_destination_station():
    destination_station_set = set()
    route_list = bus_controller.search_route_by_province('กรุงเทพมหานคร')
    for route in route_list:
        province_name, source_station, destination_province, destination_station = route
        if source_station == 'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)':
            if destination_province == 'กาญจนบุรี':
                destination_station_set.add(destination_station)
    destination_stations_lst = list(destination_station_set)
    return destination_stations_lst

@app.get('/api/date_trip')
def get_date_trip():
    pass

@app.get('/api/trip')
def get_trip():
    pass

@app.get('/api/seat')
def get_seat():
    bus_list = bus_controller.search_bus_by_bus_license('1นค5463')
    seat_lst = []
    for bus_license, location, seat_list in bus_list:
        for seat_number, status_seat in seat_list:
            seat_lst.append((seat_number, status_seat))
    return seat_lst

@app.post('/api/seat')
def post_seat():
    pass

@app.post('/api/info')
def post_info():
    pass

@app.get('/api/ticket')
def get_ticket():
    ticket_list = bus_controller.search_ticket_by_ticket_id('01')
    for ticket_id, schedule, seat_number in ticket_list:
        return ticket_id, schedule, seat_number

@app.put('/api/cancel')
def put_cancel():
    pass