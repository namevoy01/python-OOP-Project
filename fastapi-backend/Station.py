class Station:
    station_id = 0
    def __init__(self, name_station):
        Station.station_id += 1
        self.__station_id = Station.station_id
        self.__name_station = name_station

    @property
    def get_station_id(self):
        return self.__station_id
    
    @property
    def get_name_station(self):
        return self.__name_station