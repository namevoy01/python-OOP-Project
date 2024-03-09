class User :
    user_id = 0
    def __init__(self, name, gender, tel):
        User.user_id += 1
        self.__user_id = User.user_id
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