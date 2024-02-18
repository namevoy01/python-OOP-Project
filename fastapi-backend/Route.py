class Bus:
    def __init__(self, source_station, destination_station, price, bus_trip_lst):
        self.__source_station = source_station
        self.__destination_station = destination_station
        self.__price = price
        self.__bus_trip_lst = []

    @property
    def source_station(self):
        return self.__source_station
    
    @property
    def destination_station(self):
        return self.__destination_station
    
    @property
    def price(self):
        return self.__price
    
    @property
    def bus_trip_lst(self):
        return self.__bus_trip_lst
    
    def add_bus_trip(bus_trip):
        pass
