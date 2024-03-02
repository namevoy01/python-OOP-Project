class Station:
    def __init__(self, station_id, name_station):
        self.__station_id = station_id
        self.__name_station = name_station

    @property
    def station_id(self):
        return self.__station_id
    
    @property
    def name_station(self):
        return self.__name_station