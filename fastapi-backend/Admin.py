from User import User

class Admin(User) :
    def __init__(self, user_id, name_passenger, surname_passenger, gender, tel, username, password):
        super().__init__(user_id, name_passenger, surname_passenger, gender, tel)
        self.__username = username
        self.__password = password
 
    @property
    def get_username(self):
        return self.__username
    
    @property
    def get_password(self):
        return self.__password
    