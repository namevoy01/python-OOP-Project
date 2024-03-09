class Schedule:
    schedule_id = 0
    def __init__(self, route, departure_date):
        Schedule.schedule_id += 1
        self.__schedule_id = Schedule.schedule_id
        self.__route = route
        self.__departure_date = departure_date 
 
    @property
    def get_schedule_id(self):
        return self.__schedule_id
    
    @property
    def get_route(self):
        return self.__route
    
    @property
    def get_departure_date (self):
        return self.__departure_date 
    