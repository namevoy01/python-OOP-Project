class Ticket :
    ticket_id = 0
    def __init__(self, schedule, seat_number):
        Ticket.ticket_id += 1
        self.__ticket_id = Ticket.ticket_id
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