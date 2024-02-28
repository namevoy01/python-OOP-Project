from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from BusService_Controller import BusService_Controller

app = FastAPI()
bus_controller = BusService_Controller([], [], [], [], [], [])

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
def get_province():
    return bus_controller.get_province_lst

@app.get('/api/source_station')
def get_source_station():
    return bus_controller.get_source_station()

@app.get('/api/destination_province')
def get_destination_province():
    pass

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
