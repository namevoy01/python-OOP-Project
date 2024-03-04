class Province :
    def __init__(self, province_id , province_name, route_lst):
        self.__province_id = province_id
        self.__province_name= province_name
        self.__route_lst = []

    @property
    def get_province_id(self):
        return self.__province_id
    
    @property
    def get_province_name(self):
        return self.__province_name
    
    @property
    def get_route_lst(self):
        return self.__route_ls