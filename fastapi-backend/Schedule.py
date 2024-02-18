class Schedule:
    def __init__(self, schedule_id, route, departure_date):
        self.__schedule_id = schedule_id
        self.__route = route 
        self.__departure_date  =  departure_date 
 
    @property
    def schedule_id(self):
        return self.__schedule_id
    
    @property
    def route(self):
        return self.__route
    
    @property
    def departure_date (self):
        return self.__departure_date 
    