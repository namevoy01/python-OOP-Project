class User :
    def __init__(self, user_id, name, gender, tel):
        self.__user_id = user_id
        self.__name = name 
        self.__gender  =  gender
        self.__tel = tel 
 
    @property
    def get_user_id(self):
        return self.__user_id
    
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_gender (self):
        return self.__gender 
    
    @property
    def get_tel(self):
        return self.__tel 