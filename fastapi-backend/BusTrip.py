class BusTrip :
<<<<<<< Updated upstream
    def __init__(self, bustrip_id , bus, schedule):
        self.__bustrip_id = bustrip_id
=======
<<<<<<< Updated upstream
    bus_trip_id = 0
    def __init__(self, bus, schedule):
        BusTrip.bus_trip_id += 1
        self.__bustrip_id = BusTrip.bustrip_id
=======
<<<<<<< Updated upstream
    def __init__(self, bustrip_id , bus, schedule):
        self.__bustrip_id = bustrip_id
=======
    bus_trip_id = 0
    def __init__(self, bus, province):
        BusTrip.bus_trip_id += 1
        self.__bus_trip_id = BusTrip.bus_trip_id
>>>>>>> Stashed changes
>>>>>>> Stashed changes
>>>>>>> Stashed changes
        self.__bus = bus
        self.__province = province

    @property
    def get_bus_trip_id(self):
        return self.__bus_trip_id
    
    @property
    def get_bus(self):
        return self.__bus
    
    @property
    def get_province(self):
        return self.__province 