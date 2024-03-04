from Admin import Admin
from Booking import Booking
from Bus import Bus
from BusTrip import BusTrip
from Passenger import Passenger
from Payment import Payment
from Province import Province
from Route import Route
from Schedule import Schedule
from Seat import Seat
from Station import Station
from Ticket import Ticket
from User import User
from BusService_Controller import BusService_Controller

bus_controller = BusService_Controller([], [], [], [], [])

# province and route ####################################################

bangkok = Province('1','กรุงเทพมหานคร')
bus_controller.add_province(bangkok)

route_1 = Route('1',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กรุงเทพมหานคร',
                'ท่าอากาศยานสุวรรณภูมิ',
                100,
                [])
bangkok.add_route(route_1)

route_2 = Route('2',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กรุงเทพมหานคร',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (รังสิต)',
                100,
                [])
bangkok.add_route(route_2)

route_3 = Route('3',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กระบี่',
                'จุดจอด อ.เหนือคลอง',
                500,
                [])
bangkok.add_route(route_3)

route_4 = Route('4',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กระบี่',
                'สถานีขนส่งผู้โดยสาร จ.กระบี่',
                500,
                [])
bangkok.add_route(route_4)

route_5 = Route('5',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กระบี่',
                'จุดจอด อ.คลองท่อม',
                500,
                [])
bangkok.add_route(route_5)

route_6 = Route('6',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กระบี่',
                'ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                500,
                [])
bangkok.add_route(route_6)

route_7 = Route('7',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กระบี่',
                'จุดจอด อ.เขาพนม',
                500,
                [])
bangkok.add_route(route_7)

krabi = Province('2', 'krabi')
bus_controller.add_province(bangkok)

# seat ####################################################

bus_1 = Bus('1','1นค5463', 'on station', [])
bus_controller.add_bus(bus_1)

route_1 = Route('1',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กรุงเทพมหานคร',
                'ท่าอากาศยานสุวรรณภูมิ',
                100,
                [])
bangkok.add_route(route_1)

# print("รายการจังหวัดและเส้นทาง:")
# for province in bus_controller.get_province_lst:
#     print(f"จังหวัด : {province.get_province_name}")
#     print("เส้นทาง :")
#     for route in province.get_route_lst:
#         print(f"- จุดเริ่มต้น : {route.get_source_station}")
#         print(f"  จุดหมายปลายทาง : {route.get_destination_station}")
#         print(f"  ราคา : {route.get_price} บาท")
#         break
