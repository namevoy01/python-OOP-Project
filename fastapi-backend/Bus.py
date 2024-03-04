class Bus:
    def __init__(self, bus_number, location, seat_list):
        self.__bus_number = bus_number
        self.__location = location
        self.__seat_list = []

    @property
    def get_bus_number(self):
        return self.__bus_number
    
    @property
    def get_location(self):
        return self.__location
    
    @property
    def get_seat_list(self):
        return self.__seat_list