class BusTrip :
    bus_trip_id = 0
    def __init__(self, bus, province, route, departure_date, departure_time):
        BusTrip.bus_trip_id += 1
        self.__bus_trip_id = BusTrip.bus_trip_id
        self.__bus = bus
        self.__province = province
        self.__route = route
        self.__departure_date = departure_date
        self.__departure_time = departure_time

    @property
    def get_bus_trip_id(self):
        return self.__bus_trip_id
    
    @property
    def get_bus(self):
        return self.__bus
    
    @property
    def get_province(self):
        return self.__province 
    
    @property
    def get_route(self):
        return self.__route
    
    @property
    def get_departure_date(self):
        return self.__departure_date
    
    @property
    def get_departure_time(self):
        return self.__departure_time