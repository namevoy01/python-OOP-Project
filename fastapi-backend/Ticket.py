class Ticket :
    def __init__(self, ticket_id , schedule, seat_number):
        self.__ticket_id = ticket_id
        self.__schedule = schedule
        self.__seat_number = seat_number

    @property
    def ticket_id(self):
        return self.__ticket_id
    
    @property
    def schedule(self):
        return self.__schedule
    
    @property
    def seat_number(self):
        return self.__seat_number