class Bus:
    def __init__(self, bus_id, bus_number, location, seat_list):
        self.__bus_id = bus_id
        self.__bus_number = bus_number
        self.__location = location
        self.__seat_lst = []

    @property
    def get_bus_id(self):
        return self.__bus_id

    @property
    def get_bus_number(self):
        return self.__bus_number
    
    @property
    def get_location(self):
        return self.__location
    
    @property
    def get_seat_lst(self):
        return self.__seat_lst
    
    def add_seat(self, seat):
        self.__seat_lst.append(seat)