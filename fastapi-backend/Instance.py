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

bangkok = Province('1', 'กรุงเทพมหานคร')
bus_controller.add_province(bangkok)

route_1 = Route('1', 'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)', 'กระบี่', 'จุดจอด อ.เหนือคลอง', 300, [])
bangkok.add_route(route_1)

krabi = Province('2', 'กระบี่')
bus_controller.add_province(krabi)

print("รายการจังหวัดและเส้นทาง:")
for province in bus_controller.get_province_lst:
    print(f"จังหวัด : {province.get_province_name}")
    print("เส้นทาง :")
    for route in province.get_route_lst:
        print(f"- จุดเริ่มต้น : {route.get_source_station}")
        print(f"  จุดหมายปลายทาง : {route.get_destination_station}")
        print(f"  ราคา : {route.get_price} บาท")
        break