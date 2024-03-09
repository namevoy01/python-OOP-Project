class BusTrip :
    bus_trip_id = 0
    def __init__(self, bus, schedule):
        BusTrip.bus_trip_id += 1
        self.__bustrip_id = BusTrip.bustrip_id
        self.__bus = bus
        self.__schedule = schedule

    @property
    def get_bustrip_id(self):
        return self.__bustrip_id
    
    @property
    def get_bus(self):
        return self.__bus
    
    @property
    def get_schedule(self):
        return self.__schedule 