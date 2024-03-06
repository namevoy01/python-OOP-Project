class Seat :
    def __init__(self, seat_id, seat_number , status_seat=False):
        self.__seat_id = seat_id
        self.__seat_number = seat_number
        self.__status_seat = status_seat

    @property
    def get_seat_id(self):
        return self.__seat_id

    @property
    def get_seat_number(self):
        return self.__seat_number
    
    @property
    def get_status_seat(self):
        return self.__status_seat
    
    def set_status_seat(self, status):
        self.__status_seat = status