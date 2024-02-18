class User:
    def __init__(self, user_id, name, gender, tel):
        self.__user_id = user_id
        self.__name = name 
        self.__gender  =  gender
        self.__tel = tel 
 
    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def gender (self):
        return self.__gender 
    
    @property
    def tel  (self):
        return self.__tel 