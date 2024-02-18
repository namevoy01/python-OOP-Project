class Seat :
    def __init__(self, seat_number , status_seat):
        self.__seat_number = seat_number
        self.__status_seat= status_seat

    @property
    def seat_number(self):
        return self.__seat_number
    
    @property
    def status_seat(self):
        return self.__status_seat