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
    source_stations = set()
    province_name = 'กรุงเทพมหานคร'
    
    for province in bus_controller.get_province_lst:
        if province.get_province_name == province_name:
            for route in province.get_route_lst:
                source_stations.add(route.get_source_station)
    
    return(list(source_stations))

@app.get('/api/destination_province')
def get_destination_province():
    destination_province = set()
    target_source_province = 'กรุงเทพมหานคร'
    target_source_station = 'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)'
    
    for province in bus_controller.get_province_lst:
        if province.get_province_name == target_source_province:
            for route in province.get_route_lst:
                if route.get_source_station == target_source_station:
                    destination_province.add(route.get_destination_province)
    
    return list(destination_province)

@app.get('/api/destination_station')
def get_destination_station():
    pass

@app.get('/api/date_trip')
def get_date_trip():
    pass

@app.get('/api/trip')
def get_trip():
    pass

@app.get('/api/seat')
def get_seat():
    pass

@app.post('/api/seat')
def post_seat():
    pass

@app.post('/api/info')
def post_info():
    pass

@app.get('/api/ticket')
def get_ticket():
    pass

@app.put('/api/cancel')
def put_cancel():
    pass