class BusTrip :
    def __init__(self, bustrip_id , bus, schedule):
        self.__bustrip_id = bustrip_id
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