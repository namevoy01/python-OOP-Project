class Ticket :
    ticket_id = 35301072
    def __init__(self, name_passenger):
        Ticket.ticket_id += 1
        self.__ticket_id = Ticket.ticket_id
        self.__name_passenger = name_passenger
        
    @property
    def get_ticket_id(self):
        return self.__ticket_id
    
    @property
    def get_name_passenger(self):
        return self.__name_passenger