class Route:
    def __init__(self, source_station, destination_station, price, bus_trip_lst):
        self.__source_station = source_station
        self.__destination_station = destination_station
        self.__price = price
        self.__bus_trip_lst = []

    @property
    def get_source_station(self):
        return self.__source_station
    
    @property
    def get_destination_station(self):
        return self.__destination_station
    
    @property
    def get_price(self):
        return self.__price
    
    @property
    def get_bus_trip_lst(self):
        return self.__bus_trip_lst
    
    def add_bus_trip(bus_trip):
        pass
