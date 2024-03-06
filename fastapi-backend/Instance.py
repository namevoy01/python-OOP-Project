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

bus_controller = BusService_Controller([], [], [], [], [], [], [], [])

def get_controller():
    return bus_controller

def create_instance():

# province ####################################################

    bangkok = Province('1','กรุงเทพมหานคร', [])
    bus_controller.add_province(bangkok)

    krabi = Province('2', 'กระบี่', [])
    bus_controller.add_province(krabi)

    kanchanaburi = Province('3','กาญจนบุรี', [])
    bus_controller.add_province(kanchanaburi)

    kalasin = Province('4', 'กาฬสินธุ์', [])
    bus_controller.add_province(kalasin)

    kamphaeng = Province('5','กำแพงเพชร', [])
    bus_controller.add_province(kamphaeng)

    khonkaen = Province('6', 'ขอนแก่น', [])
    bus_controller.add_province(khonkaen)

    chanthaburi = Province('7','จันทบุรี', [])
    bus_controller.add_province(chanthaburi)

    chachoengsao = Province('8', 'ฉะเชิงเทรา', [])
    bus_controller.add_province(chachoengsao)

    chonburi = Province('9','ชลบุรี', [])
    bus_controller.add_province(chonburi)

    chainat = Province('10', 'ชัยนาท', [])
    bus_controller.add_province(chainat)

    chaiyaphum = Province('11','ชัยภูมิ', [])
    bus_controller.add_province(chaiyaphum)

    chumphon = Province('12', 'ชุมพร', [])
    bus_controller.add_province(chumphon)

    chiangrai = Province('13','เชียงราย', [])
    bus_controller.add_province(chiangrai)

    chiangmai = Province('14', 'เชียงใหม่', [])
    bus_controller.add_province(chiangmai)

    trang = Province('15','ตรัง', [])
    bus_controller.add_province(trang)

    trat = Province('16', 'ตราด', [])
    bus_controller.add_province(trat)

    tak = Province('17','ตาก', [])
    bus_controller.add_province(tak)

    nakhonnayok = Province('18', 'นครนายก', [])
    bus_controller.add_province(nakhonnayok)

    nakhonpathom = Province('19','นครปฐม', [])
    bus_controller.add_province(nakhonpathom)

    nakhonphanom = Province('20', 'นครพนม', [])
    bus_controller.add_province(nakhonphanom)

    nakhonratchasima = Province('21','นครราชสีมา', [])
    bus_controller.add_province(nakhonratchasima)

    nakhonsithammarat = Province('22', 'นครศรีธรรมราช', [])
    bus_controller.add_province(nakhonsithammarat)

    nakhonsawan = Province('23','นครสวรรค์', [])
    bus_controller.add_province(nakhonsawan)

    nonthaburi = Province('24', 'นนทบุรี', [])
    bus_controller.add_province(nonthaburi)

    narathiwat = Province('25','นราธิวาส', [])
    bus_controller.add_province(narathiwat)

    nan = Province('26', 'น่าน', [])
    bus_controller.add_province(nan)

    buengkan = Province('27', 'บึงกาฬ', [])
    bus_controller.add_province(buengkan)

    buriram = Province('28','บุรีรัมย์', [])
    bus_controller.add_province(buriram)

    pathumthani = Province('29', 'ปทุมธานี', [])
    bus_controller.add_province(pathumthani)

    prachuapkkhirikhan = Province('30','ประจวบคีรีขันธ์', [])
    bus_controller.add_province(prachuapkkhirikhan)

    prachinburi = Province('31', 'ปราจีนบุรี', [])
    bus_controller.add_province(prachinburi)

    pattani = Province('32','ปัตตานี', [])
    bus_controller.add_province(pattani)

    phayao = Province('33', 'พะเยา', [])
    bus_controller.add_province(phayao)

    phangnga = Province('34','พังงา', [])
    bus_controller.add_province(phangnga)

    phatthalung = Province('35', 'พัทลุง', [])
    bus_controller.add_province(phatthalung)

    phichit = Province('36','พิจิตร', [])
    bus_controller.add_province(phichit)

    phitsanulok = Province('37', 'พิษณุโลก', [])
    bus_controller.add_province(phitsanulok)

    phetchaburi = Province('38','เพชรบุรี', [])
    bus_controller.add_province(phetchaburi)

    phetchabun = Province('39', 'เพชรบูรณ์', [])
    bus_controller.add_province(phetchabun)

    phrae = Province('40','แพร่', [])
    bus_controller.add_province(phrae)

    phuket = Province('41', 'ภูเก็ต', [])
    bus_controller.add_province(phuket)

    mahasarakham = Province('42','มหาสารคาม', [])
    bus_controller.add_province(mahasarakham)

    mukdahan = Province('43', 'มุกดาหาร', [])
    bus_controller.add_province(mukdahan)

    maehongson = Province('44','แม่ฮ่องสอน', [])
    bus_controller.add_province(maehongson)

    yasothon = Province('45', 'ยโสธร', [])
    bus_controller.add_province(yasothon)

    yala = Province('46','ยะลา', [])
    bus_controller.add_province(yala)

    roiet = Province('47', 'ร้อยเอ็ด', [])
    bus_controller.add_province(roiet)

    ranong = Province('48','ระนอง', [])
    bus_controller.add_province(ranong)

    rayong = Province('49', 'ระยอง', [])
    bus_controller.add_province(rayong)

    lopburi = Province('50','ลพบุรี', [])
    bus_controller.add_province(lopburi)

    lampang = Province('51', 'ลำปาง', [])
    bus_controller.add_province(lampang)

    lamphun = Province('52','ลำพูน', [])
    bus_controller.add_province(lamphun)

    loei = Province('53', 'เลย', [])
    bus_controller.add_province(loei)

    sisaket = Province('54','ศรีสะเกษ', [])
    bus_controller.add_province(sisaket)

    sakonnakhon = Province('55', 'สกลนคร', [])
    bus_controller.add_province(sakonnakhon)

    songkhla = Province('56','สงขลา', [])
    bus_controller.add_province(songkhla)

    satun = Province('57', 'สตูล', [])
    bus_controller.add_province(satun)

    samutprakan = Province('58','สมุทรปราการ', [])
    bus_controller.add_province(samutprakan)

    samutsongkhram = Province('59', 'สมุทรสงคราม', [])
    bus_controller.add_province(samutsongkhram)

    samutsakhon = Province('60','สมุทรสาคร', [])
    bus_controller.add_province(samutsakhon)

    sakaeo = Province('61', 'สระแก้ว', [])
    bus_controller.add_province(sakaeo)

    saraburi = Province('62','สระบุรี', [])
    bus_controller.add_province(saraburi)

    singburi = Province('63', 'สิงห์บุรี', [])
    bus_controller.add_province(singburi)

    sukhothai = Province('64','สุโขทัย', [])
    bus_controller.add_province(sukhothai)

    suphanburi = Province('65', 'สุพรรณบุรี', [])
    bus_controller.add_province(suphanburi)

    suratthani = Province('66','สุราษฎร์ธานี', [])
    bus_controller.add_province(suratthani)

    surin = Province('67', 'สุรินทร์', [])
    bus_controller.add_province(surin)

    nongkhai = Province('68','หนองคาย', [])
    bus_controller.add_province(nongkhai)

    nongbualamphu = Province('69', 'หนองบัวลำภู', [])
    bus_controller.add_province(nongbualamphu)

    ayutthaya = Province('70','อยุธยา', [])
    bus_controller.add_province(ayutthaya)

    angthong = Province('71', 'อ่างทอง', [])
    bus_controller.add_province(angthong)

    amnatcharoen = Province('72','อำนาจเจริญ', [])
    bus_controller.add_province(amnatcharoen)

    udonthani = Province('73', 'อุดรธานี', [])
    bus_controller.add_province(udonthani)

    uttaradit = Province('74','อุตรดิตถ์', [])
    bus_controller.add_province(uttaradit)

    uthaithani = Province('75', 'อุทัยธานี', [])
    bus_controller.add_province(uthaithani)

    ubonratchathani = Province('76','อุบลราชธานี', [])
    bus_controller.add_province(ubonratchathani)

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

    ### ... ###

    route_8 = Route('8',
                    'จุดจอด อ.คลองท่อม',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    500,
                    [])
    krabi.add_route(route_8)

    route_9 = Route('10',
                    'จุดจอด อ.คลองท่อม',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (ถนนบรมราชชนนี)',
                    500,
                    [])
    krabi.add_route(route_10)

    route_11 = Route('11',
                    'จุดจอด อ.คลองท่อม',
                    'กระบี่',
                    'สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    500,
                    [])
    krabi.add_route(route_11)

    route_12 = Route('12',
                    'จุดจอด อ.คลองท่อม',
                    'กระบี่',
                    'จุดจอด อ.ลำทับ',
                    500,
                    [])
    krabi.add_route(route_12)

    route_13 = Route('13',
                    'จุดจอด อ.คลองท่อม',
                    'ชุมพร',
                    'จุดจอดสี่แยกปฐมพร',
                    500,
                    [])
    krabi.add_route(route_13)

    route_14 = Route('14',
                    'จุดจอด อ.คลองท่อม',
                    'ชุมพร',
                    'จุดจอดบขส.ท่าแซะ',
                    500,
                    [])
    krabi.add_route(route_14)

    route_15 = Route('15',
                    'จุดจอด อ.คลองท่อม',
                    'ชุมพร',
                    'จุดจอด อ.หลังสวน',
                    500,
                    [])
    krabi.add_route(route_15)

    # bus ####################################################

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

    # seat ####################################################

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

    seat_A04 = Seat('4',
                'A04',
                False)
    bus_1.add_seat(seat_A04)

    seat_A05 = Seat('5',
                'A05',
                False)
    bus_1.add_seat(seat_A05)

    seat_A06 = Seat('6',
                'A06',
                False)
    bus_1.add_seat(seat_A06)

    seat_A07 = Seat('7',
                'A07',
                False)
    bus_1.add_seat(seat_A07)

    seat_A08 = Seat('8',
                'A08',
                False)
    bus_1.add_seat(seat_A08)

    seat_A09 = Seat('9',
                'A09',
                False)
    bus_1.add_seat(seat_A09)

    seat_A10 = Seat('10',
                'A10',
                False)
    bus_1.add_seat(seat_A10)

    seat_A11 = Seat('11',
                'A11',
                False)
    bus_1.add_seat(seat_A11)

    seat_A12 = Seat('12',
                'A12',
                False)
    bus_1.add_seat(seat_A12)

    seat_A13 = Seat('13',
                'A13',
                False)
    bus_1.add_seat(seat_A13)

    seat_A14 = Seat('14',
                'A14',
                False)
    bus_1.add_seat(seat_A14)

    seat_A15 = Seat('15',
                'A15',
                False)
    bus_1.add_seat(seat_A15)

    seat_A16 = Seat('16',
                'A16',
                False)
    bus_1.add_seat(seat_A16)

    seat_A17 = Seat('17',
                'A17',
                False)
    bus_1.add_seat(seat_A17)

    seat_A18 = Seat('18',
                'A18',
                False)
    bus_1.add_seat(seat_A18)

    seat_A19 = Seat('19',
                'A19',
                False)
    bus_1.add_seat(seat_A19)

    seat_A20 = Seat('20',
                'A20',
                False)
    bus_1.add_seat(seat_A20)

    seat_A21 = Seat('21',
                'A21',
                False)
    bus_1.add_seat(seat_A21)

    seat_A22 = Seat('22',
                'A22',
                False)
    bus_1.add_seat(seat_A22)

    seat_A23 = Seat('23',
                'A23',
                False)
    bus_1.add_seat(seat_A23)

    seat_A24 = Seat('24',
                'A24',
                False)
    bus_1.add_seat(seat_A24)

    seat_A25 = Seat('25',
                'A25',
                False)
    bus_1.add_seat(seat_A25)

    seat_A26 = Seat('26',
                'A26',
                False)
    bus_1.add_seat(seat_A26)

    seat_A27 = Seat('27',
                'A27',
                False)
    bus_1.add_seat(seat_A27)

    seat_A28 = Seat('28',
                'A28',
                False)
    bus_1.add_seat(seat_A28)

    seat_A29 = Seat('29',
                'A29',
                False)
    bus_1.add_seat(seat_A29)

    seat_A30 = Seat('30',
                'A30',
                False)
    bus_1.add_seat(seat_A30)

    seat_A31 = Seat('31',
                'A31',
                False)
    bus_1.add_seat(seat_A31)

    seat_A32 = Seat('32',
                'A32',
                False)
    bus_1.add_seat(seat_A32)

    seat_A33 = Seat('33',
                'A33',
                False)
    bus_1.add_seat(seat_A33)

    seat_A34 = Seat('34',
                'A34',
                False)
    bus_1.add_seat(seat_A34)

    seat_A35 = Seat('35',
                'A35',
                False)
    bus_1.add_seat(seat_A35)

    seat_A36 = Seat('36',
                'A36',
                False)
    bus_1.add_seat(seat_A36)

create_instance()

bus_controller.add_booking('001', 'chamaiporn', 'credit card', 540, '10-02-2024', 'payment')
bus_controller.add_ticket('01', 'booking', 'A01')

# check search route by province
route_list = bus_controller.search_route_by_province('กรุงเทพมหานคร')
for province_name, source_station, destination_province, destination_station in route_list:
    print(f"ต้นทาง {province_name} - {source_station}")
    print(f"ปลายทาง {destination_province} - {destination_station}")
    print("-----------------------------------------------------------------")
    

# check search ticket by ticket id
ticket_list = bus_controller.search_ticket_by_ticket_id('01')
for ticket_id, schedule, seat_number in ticket_list:
    print(f"{ticket_id} รอบรถคือ {schedule} หมายเลขที่นั่ง {seat_number}")
    print("-----------------------------------------------------------------")
    break

# check search bus by bus license
bus_list = bus_controller.search_bus_by_bus_license('1นค5463')
for bus_license, location, seat_lst  in bus_list:
    print(f"เลขทะเบียนนรถ {bus_license} สถานที่รถอยู่ปัจจุบัน {location}")
    for seat_number, status_seat in seat_lst:
        print(f"เลขที่นั่ง {seat_number} สถานะ {status_seat}")
        print("-----------------------------------------------------------------")
        break

# check search source_station by bus province
# bus_list = bus_controller.search_source_station_by_province('กรุงเทพมหานคร')
# for bus_license, location, seat_lst  in bus_list:
#     print(f"เลขทะเบียนนรถ {bus_license} สถานที่รถอยู่ปัจจุบัน {location}")
#     for seat_number, status_seat in seat_lst:
#         print(f"เลขที่นั่ง {seat_number} สถานะ {status_seat}")
#         print("-----------------------------------------------------------------")
#         break