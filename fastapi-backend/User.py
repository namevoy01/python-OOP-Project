class User :
    user_id = 0
    def __init__(self, name_passenger, surname_passenger, gender, tel):
        User.user_id += 1
        self.__user_id = User.user_id
        self.__name_passenger = name_passenger
        self.__surname_passenger = surname_passenger
        self.__gender  =  gender
        self.__tel = tel 
 
    @property
    def get_user_id(self):
        return self.__user_id
    
    @property
    def get_name_passenger(self):
        return self.__name_passenger
    
    @property
    def get_surname_passenger(self):
        return self.__surname_passenger
    
    @property
    def get_gender (self):
        return self.__gender 
    
    @property
    def get_tel(self):
        return self.__tel 