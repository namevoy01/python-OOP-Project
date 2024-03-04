class Ticket :
    def __init__(self, ticket_id , schedule, seat_number):
        self.__ticket_id = ticket_id
        self.__schedule = schedule
        self.__seat_number = seat_number

    @property
    def get_ticket_id(self):
        return self.__ticket_id
    
    @property
    def get_schedule(self):
        return self.__schedule
    
    @property
    def get_seat_number(self):
        return self.__seat_number