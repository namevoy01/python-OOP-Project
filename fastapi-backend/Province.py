class Province :
    def __init__(self, province_id , province_name, route_lst):
        self.__province_id = province_id
        self.__province_name= province_name
        self.__route_lst = route_lst

    @property
    def province_id(self):
        return self.__province_id
    
    @property
    def province_name(self):
        return self.__province_name
    
    @property
    def route_lst(self):
        return self.__route_lst
    
    def add_route():
        pass