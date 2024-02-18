class BusTrip :
    def __init__(self, bustrip_id , bus, schedule):
        self.__bustrip_id = bustrip_id
        self.__bus = bus
        self.__schedule = schedule

    @property
    def bustrip_id(self):
        return self.__bustrip_id
    
    @property
    def bus(self):
        return self.__bus
    
    @property
    def schedule(self):
        return self.__schedule 