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

# province ####################################################

bangkok = Province('1','กรุงเทพมหานคร', [])
bus_controller.add_province(bangkok)
krabi = Province('2', 'กระบี่', [])
bus_controller.add_province(krabi)

# route ####################################################

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
                50,
                [])
bangkok.add_route(route_6)

route_7 = Route('7',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กระบี่',
                'จุดจอด อ.เขาพนม',
                520,
                [])
bangkok.add_route(route_7)

route_8 = Route('8',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กาญจนบุรี',
                'จุดจอด น้ำตกเกริงกะเวีย',
                230,
                [])
bangkok.add_route(route_8)

route_9 = Route('9',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กาญจนบุรี',
                'จุดจอด อ.สังขละบุรี',
                250,
                [])
bangkok.add_route(route_9)

route_10 = Route('10',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กาญจนบุรี',
                'จุดจอด อ.ทองผาภูมิ',
                250,
                [])
bangkok.add_route(route_10)

route_11 = Route('11',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กาญจนบุรี',
                'จุดจอด บ้านท่าเสา',
                280,
                [])
bangkok.add_route(route_11)

route_12 = Route('12',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กาญจนบุรี',
                'จุดจอด อ.ไทรโยค',
                280,
                [])
bangkok.add_route(route_12)

route_13 = Route('13',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กาญจนบุรี',
                'สถานีขนส่งผู้โดยสาร จ.กาญจนบุรี',
                280,
                [])
bangkok.add_route(route_13)

route_7 = Route('7',
                'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                'กาญจนบุรี',
                'จุดจอด อ.เขาพนม',
                500,
                [])
bangkok.add_route(route_7)

# seat ####################################################

bus_1 = Bus('1','1นค5463', 'on station', [])
bus_controller.add_bus(bus_1)
bus_2 = Bus('2','3นถ4263', 'on station', [])
bus_controller.add_bus(bus_2)
bus_3= Bus('3','1ตก9954', 'on station', [])
bus_controller.add_bus(bus_3)
bus_4 = Bus('4','2บห4110', 'on station', [])
bus_controller.add_bus(bus_4)
bus_5 = Bus('5','1วส7845', 'on station', [])
bus_controller.add_bus(bus_5)

seat_A01 = Seat('1',
            'A01',
            False)
bus_1.add_seat(seat_A01)

seat_A02 = Seat('2',
            'A02',
            False)
bus_1.add_seat(seat_A02)

seat_A03 = Seat('3',
            'A03',
            False)
bus_1.add_seat(seat_A03)

print("รายการจังหวัดและเส้นทาง:")
print([province.get_province_name for province in bus_controller.get_province_lst])
print([bus.get_bus_number for bus in bus_controller.get_bus_lst])