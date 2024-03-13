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
from Ticket import Ticket
from User import User
from Instance import get_controller
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
    source_province =  [province.get_province_name for province in bus_controller.get_province_lst]
    return source_province
  
@app.get('/api/source_station')  
def get_source_station(source_province):
    source_station = bus_controller.search_source_station(source_province)
    return source_station

@app.get('/api/destination_province')
def get_destination_province(source_province, source_station):
    destination_province =  bus_controller.search_destination_province(source_province, source_station)
    return destination_province
    
@app.get('/api/destination_station')
def get_destination_station(source_province, source_station, destination_province):
    destination_station =  bus_controller.search_destination_station(source_province, source_station,destination_province)
    return destination_station
    
@app.get('/api/info_trip')
def get_info(source_province, source_station, destination_province, destination_station, departure_date, departure_time, bus_license, seat_number):
    info_on_booking = bus_controller.get_info_on_booking(source_province, source_station, destination_province, destination_station, departure_date, departure_time, bus_license, seat_number)
    return info_on_booking

@app.get('/api/trip')
def get_trip(source_province, source_station, destination_province, destination_station, departure_date):
    trip = bus_controller.get_trip(source_province, source_station, destination_province, destination_station, departure_date)
    return trip
                
@app.get('/api/seat')
def get_seat(bus_license):
    seat = bus_controller.get_seat(bus_license)
    return seat

@app.post('/api/info')
def post_info(name_passenger, surname_passenger, gender, tel, email, status_payment, payment_option, amount, date, bus_license, seat_number, source_province, source_station, destination_province, destination_station, departure_date):
    bus_controller.add_booking(name_passenger, surname_passenger, gender, tel, email, status_payment, payment_option, amount, date, bus_license, seat_number, source_province, source_station, destination_province, destination_station, departure_date)

@app.get('/api/ticket')
def get_ticket(ticket_id):
    ticket = bus_controller.get_search_ticket(ticket_id)
    return ticket
    
@app.delete('/api/cancel')
def delete_cancel(ticket_id):
    cancel_ticket = bus_controller.cancel_ticket(ticket_id)
    return cancel_ticket

@app.post('/api/login')
def login(username, password):
    user = bus_controller.login_for_admin(username, password)
    return user

@app.get('/api/schedule')
def schedule():
    schedule = bus_controller.get_schedule_info()
    return schedule

@app.get('/api/search_ticket')
def search_ticket(ticket_id):
    search = bus_controller.get_search_ticket(ticket_id)
    return search