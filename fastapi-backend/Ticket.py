class Ticket :
    ticket_id = 15001010
    def __init__(self, booking, seat_number):
        Ticket.ticket_id += 1
        self.__ticket_id = Ticket.ticket_id
        self.__booking = booking
        self.__seat_number = seat_number

    @property
    def get_ticket_id(self):
        return self.__ticket_id
    
    @property
    def get_booking(self):
        return self.__booking
    
    @property
    def get_seat_number(self):
        return self.__seat_number