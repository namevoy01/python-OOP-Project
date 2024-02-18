class Bus:
    def __init__(self, bus_number, location, seat_list):
        self.__bus_number = bus_number
        self.__location = location
        self.__seat_list = []

    @property
    def bus_number(self):
        return self.__bus_number
    
    @property
    def location(self):
        return self.__location
    
    @property
    def seat_list(self):
        return self.__seat_list
    
    def update_location():
        pass
