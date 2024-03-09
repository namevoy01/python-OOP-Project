class Bus:
    bus_id = 0
    def __init__(self, bus_license, location, seat_list):
        Bus.bus_id += 1
        self.__bus_id = Bus.bus_id
        self.__bus_license = bus_license
        self.__location = location
        self.__seat_lst = []

    @property
    def get_bus_id(self):
        return self.__bus_id

    @property
    def get_bus_license(self):
        return self.__bus_license
    
    @property
    def get_location(self):
        return self.__location
    
    @property
    def get_seat_lst(self):
        return self.__seat_lst
    
    def add_seat(self, seat):
        self.__seat_lst.append(seat)