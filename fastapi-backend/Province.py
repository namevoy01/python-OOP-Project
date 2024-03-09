class Province :
    province_id = 0
    def __init__(self, province_name):
        Province.province_id += 1
        self.__province_id = Province.province_id
        self.__province_name = province_name

    @property
    def get_province_id(self):
        return self.__province_id
    
    @property
    def get_province_name(self):
        return self.__province_name
    
    @property
    def get_route_lst(self):
        return self.__route_lst
    
    def add_route(self, route):
        self.__route_lst.append(route)