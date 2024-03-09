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

    bangkok = Province('กรุงเทพมหานคร')
    bus_controller.add_province(bangkok)

    krabi = Province('กระบี่')
    bus_controller.add_province(krabi)

    # kanchanaburi = Province('กาญจนบุรี', [])
    # bus_controller.add_province(kanchanaburi)

    # kalasin = Province('กาฬสินธุ์', [])
    # bus_controller.add_province(kalasin)

    # kamphaeng = Province('กำแพงเพชร', [])
    # bus_controller.add_province(kamphaeng)

    # khonkaen = Province('ขอนแก่น', [])
    # bus_controller.add_province(khonkaen)

    # chanthaburi = Province('จันทบุรี', [])
    # bus_controller.add_province(chanthaburi)

    # chachoengsao = Province('ฉะเชิงเทรา', [])
    # bus_controller.add_province(chachoengsao)

    # chonburi = Province('ชลบุรี', [])
    # bus_controller.add_province(chonburi)

    # chainat = Province('ชัยนาท', [])
    # bus_controller.add_province(chainat)

    # chaiyaphum = Province('ชัยภูมิ', [])
    # bus_controller.add_province(chaiyaphum)

    # chumphon = Province('ชุมพร', [])
    # bus_controller.add_province(chumphon)

    # chiangrai = Province('เชียงราย', [])
    # bus_controller.add_province(chiangrai)

    # chiangmai = Province('เชียงใหม่', [])
    # bus_controller.add_province(chiangmai)

    # trang = Province('ตรัง', [])
    # bus_controller.add_province(trang)

    # trat = Province('ตราด', [])
    # bus_controller.add_province(trat)

    # tak = Province('ตาก', [])
    # bus_controller.add_province(tak)

    # nakhonnayok = Province('นครนายก', [])
    # bus_controller.add_province(nakhonnayok)

    # nakhonpathom = Province('นครปฐม', [])
    # bus_controller.add_province(nakhonpathom)

    # nakhonphanom = Province('นครพนม', [])
    # bus_controller.add_province(nakhonphanom)

    # nakhonratchasima = Province('นครราชสีมา', [])
    # bus_controller.add_province(nakhonratchasima)

    # nakhonsithammarat = Province('นครศรีธรรมราช', [])
    # bus_controller.add_province(nakhonsithammarat)

    # nakhonsawan = Province('นครสวรรค์', [])
    # bus_controller.add_province(nakhonsawan)

    # nonthaburi = Province('นนทบุรี', [])
    # bus_controller.add_province(nonthaburi)

    # narathiwat = Province('นราธิวาส', [])
    # bus_controller.add_province(narathiwat)

    # nan = Province('น่าน', [])
    # bus_controller.add_province(nan)

    # buengkan = Province('บึงกาฬ', [])
    # bus_controller.add_province(buengkan)

    # buriram = Province('บุรีรัมย์', [])
    # bus_controller.add_province(buriram)

    # pathumthani = Province('ปทุมธานี', [])
    # bus_controller.add_province(pathumthani)

    # prachuapkkhirikhan = Province('ประจวบคีรีขันธ์', [])
    # bus_controller.add_province(prachuapkkhirikhan)

    # prachinburi = Province('ปราจีนบุรี', [])
    # bus_controller.add_province(prachinburi)

    # pattani = Province('ปัตตานี', [])
    # bus_controller.add_province(pattani)

    # phayao = Province('พะเยา', [])
    # bus_controller.add_province(phayao)

    # phangnga = Province('พังงา', [])
    # bus_controller.add_province(phangnga)

    # phatthalung = Province('พัทลุง', [])
    # bus_controller.add_province(phatthalung)

    # phichit = Province('พิจิตร', [])
    # bus_controller.add_province(phichit)

    # phitsanulok = Province('พิษณุโลก', [])
    # bus_controller.add_province(phitsanulok)

    # phetchaburi = Province('เพชรบุรี', [])
    # bus_controller.add_province(phetchaburi)

    # phetchabun = Province('เพชรบูรณ์', [])
    # bus_controller.add_province(phetchabun)

    # phrae = Province('แพร่', [])
    # bus_controller.add_province(phrae)

    # phuket = Province('ภูเก็ต', [])
    # bus_controller.add_province(phuket)

    # mahasarakham = Province('มหาสารคาม', [])
    # bus_controller.add_province(mahasarakham)

    # mukdahan = Province('มุกดาหาร', [])
    # bus_controller.add_province(mukdahan)

    # maehongson = Province('แม่ฮ่องสอน', [])
    # bus_controller.add_province(maehongson)

    # yasothon = Province('ยโสธร', [])
    # bus_controller.add_province(yasothon)

    # yala = Province('ยะลา', [])
    # bus_controller.add_province(yala)

    # roiet = Province('ร้อยเอ็ด', [])
    # bus_controller.add_province(roiet)

    # ranong = Province('ระนอง', [])
    # bus_controller.add_province(ranong)

    # rayong = Province('ระยอง', [])
    # bus_controller.add_province(rayong)

    # lopburi = Province('ลพบุรี', [])
    # bus_controller.add_province(lopburi)

    # lampang = Province('ลำปาง', [])
    # bus_controller.add_province(lampang)

    # lamphun = Province('ลำพูน', [])
    # bus_controller.add_province(lamphun)

    # loei = Province('เลย', [])
    # bus_controller.add_province(loei)

    # sisaket = Province('ศรีสะเกษ', [])
    # bus_controller.add_province(sisaket)

    # sakonnakhon = Province('สกลนคร', [])
    # bus_controller.add_province(sakonnakhon)

    # songkhla = Province('สงขลา', [])
    # bus_controller.add_province(songkhla)

    # satun = Province('สตูล', [])
    # bus_controller.add_province(satun)

    # samutprakan = Province('สมุทรปราการ', [])
    # bus_controller.add_province(samutprakan)

    # samutsongkhram = Province('สมุทรสงคราม', [])
    # bus_controller.add_province(samutsongkhram)

    # samutsakhon = Province('สมุทรสาคร', [])
    # bus_controller.add_province(samutsakhon)

    # sakaeo = Province('สระแก้ว', [])
    # bus_controller.add_province(sakaeo)

    # saraburi = Province('สระบุรี', [])
    # bus_controller.add_province(saraburi)

    # singburi = Province('สิงห์บุรี', [])
    # bus_controller.add_province(singburi)

    # sukhothai = Province('สุโขทัย', [])
    # bus_controller.add_province(sukhothai)

    # suphanburi = Province('สุพรรณบุรี', [])
    # bus_controller.add_province(suphanburi)

    # suratthani = Province('สุราษฎร์ธานี', [])
    # bus_controller.add_province(suratthani)

    # surin = Province('สุรินทร์', [])
    # bus_controller.add_province(surin)

    # nongkhai = Province('หนองคาย', [])
    # bus_controller.add_province(nongkhai)

    # nongbualamphu = Province('หนองบัวลำภู', [])
    # bus_controller.add_province(nongbualamphu)

    # ayutthaya = Province('อยุธยา', [])
    # bus_controller.add_province(ayutthaya)

    # angthong = Province('อ่างทอง', [])
    # bus_controller.add_province(angthong)

    # amnatcharoen = Province('อำนาจเจริญ', [])
    # bus_controller.add_province(amnatcharoen)

    # udonthani = Province('อุดรธานี', [])
    # bus_controller.add_province(udonthani)

    # uttaradit = Province('อุตรดิตถ์', [])
    # bus_controller.add_province(uttaradit)

    # uthaithani = Province('อุทัยธานี', [])
    # bus_controller.add_province(uthaithani)

    # ubonratchathani = Province('อุบลราชธานี', [])
    # bus_controller.add_province(ubonratchathani)

    # route ####################################################

    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กรุงเทพมหานคร',
                    'ท่าอากาศยานสุวรรณภูมิ',
                    100))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (รังสิต)',
                    100))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กระบี่',
                    'จุดจอด อ.เหนือคลอง',
                    700))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กระบี่',
                    'สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    700))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กระบี่',
                    'จุดจอด อ.คลองท่อม',
                    700))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กระบี่',
                    'ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    700))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กระบี่',
                    'จุดจอด อ.เขาพนม',
                    720))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาญจนบุรี',
                    'จุดจอด น้ำตกเกริงกะเวีย',
                    230))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาญจนบุรี',
                    'จุดจอด อ.สังขละบุรี',
                    250))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาญจนบุรี',
                    'จุดจอด อ.ทองผาภูมิ',
                    250))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาญจนบุรี',
                    'จุดจอด บ้านท่าเสา',
                    280))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาญจนบุรี',
                    'จุดจอด อ.ไทรโยค',
                    280))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาญจนบุรี',
                    'สถานีขนส่งผู้โดยสาร จ.กาญจนบุรี',
                    280))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาญจนบุรี',
                    'จุดจอด อ.เขาพนม',
                    280))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาฬสินธุ์',
                    'จุดจอด บ้านใหม่ชัยมงคล',
                    400))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาฬสินธุ์',
                    'จุดจอดบ้านบัวขาว',
                    400))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาฬสินธุ์',
                    'จุดจอด อ.เขาวง',
                    400))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาฬสินธุ์',
                    'จุดจอดวังสามหมอ',
                    420))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาฬสินธุ์',
                    'จุดจอด กิ่ง อ.นาคู',
                    430))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาฬสินธุ์',
                    'สถานีขนส่งผู้โดยสาร จ.กาฬสินธุ์',
                    450))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาฬสินธุ์',
                    'จุดจอด อ.กุฉินารายณ์',
                    450))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาฬสินธุ์',
                    'จุดจอด อ.สมเด็จ',
                    480))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาฬสินธุ์',
                    'จุดจอด อ.ห้วยผึ้ง',
                    480))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กาฬสินธุ์',
                    'จุดจอด อ.คำม่วง',
                    480))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กำแพงเพชร',
                    'จุดจอด บ้านนครชุม',
                    200))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กำแพงเพชร',
                    'จุดจอด แม่วงก์',
                    200))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กำแพงเพชร',
                    'สถานีคลองลาน แม่วงก์',
                    220))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กำแพงเพชร',
                    'จุดจอดวังปลาอ้าว',
                    220))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กำแพงเพชร',
                    'จุดจอด จุดพักรถสลกบาตร',
                    230))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กำแพงเพชร',
                    'สถานีคลองลาน',
                    230))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กำแพงเพชร',
                    'จุดจอดพรานกระต่าย',
                    240))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กำแพงเพชร',
                    'สถานีขนส่งผู้โดยสาร จ.กำแพงเพชร',
                    240))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'กำแพงเพชร',
                    'จุดจอด ต.สลกบาตร',
                    250))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ขอนแก่น',
                    'จุดจอดเขาสวนกวาง',
                    310))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ขอนแก่น',
                    'จุดจอด ทางแยกเข้าเขื่อนอุบลรัตน์',
                    310))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ขอนแก่น',
                    'จุดจอดน้ำพอง',
                    310))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ขอนแก่น',
                    'สถานีขนส่งผู้โดยสาร อ.ชุมแพ',
                    320))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ขอนแก่น',
                    'จุดจอด อ.กระนวน',
                    320))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ขอนแก่น',
                    'สถานีขนส่งผู้โดยสาร จ.ขอนแก่น (บขส.3)',
                    340))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ขอนแก่น',
                    'จุดจอดหนองสองห้อง',
                    340))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ขอนแก่น',
                    'จุดจอด อ.บ้านไผ่',
                    350))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ขอนแก่น',
                    'สถานีขนส่งผู้โดยสาร อ.พล',
                    350))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ขอนแก่น',
                    'จุดจอดศรีบุญเรือง',
                    350))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ขอนแก่น',
                    'ภูเวียง',
                    370))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'จันทบุรี',
                    'สถานีขนส่งผู้โดยสาร จ.จันทบุรี',
                    140))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'จันทบุรี',
                    'จุดจอด อ.นายายอาม',
                    140))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'จันทบุรี',
                    'จุดจอด ตลาดพลับพลา',
                    145))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'จันทบุรี',
                    'จุดจอด อ.ขลุง',
                    145))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'จันทบุรี',
                    'จุดจอด กุลพัฒน์',
                    145))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'จุดจอด บ้านบางวัว',
                    120))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'บางปะกง',
                    125))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'ชลบุรี',
                    130))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'จุดจอด ทางแยกหนองใหญ่',
                    130))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'สถานีขนส่งผู้โดยสาร จ.ชลบุรี',
                    135))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'ท่าสัตหีบ',
                    140))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'จุดจอด ร้านอาหารครัวไท',
                    140))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'บางแสน',
                    145))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'ท่าศรีราชา',
                    145))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'ท่าแหลมฉบัง',
                    155))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'ท่าพัทยา',
                    155))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ฉะเชิงเทรา',
                    'จุดจอด ต.หนองปรือ',
                    155))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชัยนาท',
                    'สถานีขนส่งผู้โดยสาร จ.ชัยนาท',
                    200))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชัยนาท',
                    'จุดจอด ทางแยกเข้า จ.ชัยนาท',
                    200))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชัยภูมิ',
                    'จุดจอดภูเขียว',
                    350))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชัยภูมิ',
                    'จุดจอด อ.จตุรัส',
                    350))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชัยภูมิ',
                    'ท่าจุดจอด ต.หนองบัวโคก',
                    355))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชัยภูมิ',
                    'จุดจอด อ.หนองเรือ',
                    355))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชัยภูมิ',
                    'จุดจอดแก้งคร้อ',
                    360))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชัยภูมิ',
                    'สถานีขนส่งผู้โดยสาร จ.ชัยภูมิ',
                    365))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชัยภูมิ',
                    'จุดจอด อ.บ้านแท่น',
                    365))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชุมพร',
                    'จุดจอด อ.ละแม',
                    460))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชุมพร',
                    'ทุ่งตะโก',
                    460))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชุมพร',
                    'จุดจอดทางแยกเข้า อ.สวี',
                    465))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชุมพร',
                    'จุดจอดบขส.ท่าแซะ',
                    465))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชุมพร',
                    'สถานีขนส่งผู้โดยสารเมืองใหม่',
                    475))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชุมพร',
                    'จุดจอด อ.หลังสวน',
                    475))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ชุมพร',
                    'จุดจอดสี่แยกปฐมพร',
                    480))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอดแม่คำหลวง',
                    750))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอด กรมขนส่ง(แม่สาย)',
                    755))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอดแม่ฟ้าหลวง',
                    755))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'สถานีขนส่งผู้โดยสาร อ.เทิง',
                    760))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอดแม่ต๋ำ',
                    765))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอด บ้านต้า',
                    765))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอด กรมขนส่ง(เทิง)',
                    770))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอด บ้านปล้อง',
                    770))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'สถานีขนส่งผู้โดยสาร อ.แม่สาย',
                    770))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอดท่าบ้านต้า',
                    775))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอด อ.พญาเม็งราย (บ้านปล้อง)',
                    775))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอดโชคชัย - แม่บง',
                    775))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอด อ.แม่สรวย',
                    780))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอดบ้านเหล่า',
                    780))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'เขื่อนภูมิพล',
                    780))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'ดอยหลวง',
                    780))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอด อ.เวียงเชียงรุ้ง',
                    780))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอดเชียงแสน',
                    785))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอดป่าแดด',
                    785))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอด อ.แม่จัน',
                    785))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'สถานีขนส่งผู้โดยสารระหว่างประเทศ อ.เชียงของ',
                    785))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอด ด่านสะพานมิตรภาพ ไทย(เชียงของ)',
                    790))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    '- สถานีขนส่งผู้โดยสาร อ.เชียงของ',
                    790))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงราย',
                    'จุดจอดบ้านศรีดอนเรือง',
                    790))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'จุดจอด อ.จอมทอง',
                    650))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'จุดจอด อ.ฝาง',
                    650))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'จุดจอด บ้านท่าตอน',
                    650))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'สถานีขนส่งผู้โดยสาร จ.เชียงใหม่ (กรมขนส่ง)',
                    655))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'จุดจอด อ.เชียงดาว',
                    655))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'จุดจอดไชยปราการ',
                    655))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'สถานีขนส่งผู้โดยสาร จ.เชียงใหม่ (อาเขต)',
                    660))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'จุดจอด อ.ฮอด',
                    660))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'จุดจอด แขวงหลวงน้ำทา(เชียงใหม่)',
                    665))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'จุดจอด แขวงอุดมชัย(เชียงใหม่)',
                    665))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'จุดจอด แขวงหลวงพระบาง(เชียงใหม่)',
                    670))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'เชียงใหม่',
                    'จุดจอดดอยเต่า',
                    670))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ตรัง',
                    'จุดจอดย่านตาขาว',
                    830))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ตรัง',
                    'สถานีขนส่งผู้โดยสาร จ.ตรัง',
                    830))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ตรัง',
                    'จุดจอดห้วยยอด',
                    840))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ตรัง',
                    'จุดจอด อันดามัน',
                    840))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ตราด',
                    'จุดจอด ต.แสนตุ้ง',
                    310))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ตราด',
                    'สถานีขนส่งผู้โดยสาร จ.ตราด',
                    310))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ตราด',
                    'จุดจอด บ้านบางกระดาน',
                    320))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ตราด',
                    'จุดจอดท่าเรืออ่าวธรรมชาติ',
                    320))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ตราด',
                    'ท่าเรือเซ็นเตอร์พอยท์',
                    330))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    'ตราด',
                    'จุดจอด อ.แหลมงอบ',
                    330))
    
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กรุงเทพมหานคร',
                    'กรมการขนส่งทางบก',
                    100))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    100))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กาฬสินธุ์',
                    'จุดจอด บ้านใหม่ชัยมงคล',
                    400))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กาฬสินธุ์',
                    'จุดจอดบ้านบัวขาว',
                    400))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กาฬสินธุ์',
                    'จุดจอด อ.เขาวง',
                    400))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กาฬสินธุ์',
                    'จุดจอดวังสามหมอ',
                    420))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กาฬสินธุ์',
                    'จุดจอด กิ่ง อ.นาคู',
                    430))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กาฬสินธุ์',
                    'สถานีขนส่งผู้โดยสาร จ.กาฬสินธุ์',
                    450))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กาฬสินธุ์',
                    'จุดจอด อ.กุฉินารายณ์',
                    450))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กาฬสินธุ์',
                    'จุดจอด อ.สมเด็จ',
                    480))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กาฬสินธุ์',
                    'จุดจอด อ.ห้วยผึ้ง',
                    480))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กาฬสินธุ์',
                    'จุดจอด อ.คำม่วง',
                    480))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กำแพงเพชร',
                    'จุดจอด บ้านนครชุม',
                    200))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กำแพงเพชร',
                    'จุดจอด แม่วงก์',
                    200))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กำแพงเพชร',
                    'สถานีคลองลาน แม่วงก์',
                    220))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กำแพงเพชร',
                    'จุดจอดวังปลาอ้าว',
                    220))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กำแพงเพชร',
                    'จุดจอด จุดพักรถสลกบาตร',
                    230))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กำแพงเพชร',
                    'สถานีคลองลาน',
                    230))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กำแพงเพชร',
                    'จุดจอดพรานกระต่าย',
                    240))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กำแพงเพชร',
                    'สถานีขนส่งผู้โดยสาร จ.กำแพงเพชร',
                    240))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'กำแพงเพชร',
                    'จุดจอด ต.สลกบาตร',
                    250))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ขอนแก่น',
                    'จุดจอดเขาสวนกวาง',
                    310))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ขอนแก่น',
                    'จุดจอด ทางแยกเข้าเขื่อนอุบลรัตน์',
                    310))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ขอนแก่น',
                    'จุดจอดน้ำพอง',
                    310))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ขอนแก่น',
                    'สถานีขนส่งผู้โดยสาร อ.ชุมแพ',
                    320))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ขอนแก่น',
                    'จุดจอด อ.กระนวน',
                    320))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ขอนแก่น',
                    'สถานีขนส่งผู้โดยสาร จ.ขอนแก่น (บขส.3)',
                    340))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ขอนแก่น',
                    'จุดจอดหนองสองห้อง',
                    340))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ขอนแก่น',
                    'จุดจอด อ.บ้านไผ่',
                    350))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ขอนแก่น',
                    'สถานีขนส่งผู้โดยสาร อ.พล',
                    350))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ขอนแก่น',
                    'จุดจอดศรีบุญเรือง',
                    350))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ขอนแก่น',
                    'ภูเวียง',
                    370))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'จันทบุรี',
                    'สถานีขนส่งผู้โดยสาร จ.จันทบุรี',
                    140))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'จันทบุรี',
                    'จุดจอด อ.นายายอาม',
                    140))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'จันทบุรี',
                    'จุดจอด ตลาดพลับพลา',
                    145))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'จันทบุรี',
                    'จุดจอด อ.ขลุง',
                    145))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'จันทบุรี',
                    'จุดจอด กุลพัฒน์',
                    145))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'จุดจอด บ้านบางวัว',
                    120))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'บางปะกง',
                    125))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'ชลบุรี',
                    130))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'จุดจอด ทางแยกหนองใหญ่',
                    130))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'สถานีขนส่งผู้โดยสาร จ.ชลบุรี',
                    135))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'ท่าสัตหีบ',
                    140))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'จุดจอด ร้านอาหารครัวไท',
                    140))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'บางแสน',
                    145))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'ท่าศรีราชา',
                    145))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'ท่าแหลมฉบัง',
                    155))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'ท่าพัทยา',
                    155))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ฉะเชิงเทรา',
                    'จุดจอด ต.หนองปรือ',
                    155))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชัยนาท',
                    'สถานีขนส่งผู้โดยสาร จ.ชัยนาท',
                    200))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชัยนาท',
                    'จุดจอด ทางแยกเข้า จ.ชัยนาท',
                    200))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชัยภูมิ',
                    'จุดจอดภูเขียว',
                    350))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชัยภูมิ',
                    'จุดจอด อ.จตุรัส',
                    350))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชัยภูมิ',
                    'ท่าจุดจอด ต.หนองบัวโคก',
                    355))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชัยภูมิ',
                    'จุดจอด อ.หนองเรือ',
                    355))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชัยภูมิ',
                    'จุดจอดแก้งคร้อ',
                    360))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชัยภูมิ',
                    'สถานีขนส่งผู้โดยสาร จ.ชัยภูมิ',
                    365))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชัยภูมิ',
                    'จุดจอด อ.บ้านแท่น',
                    365))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชุมพร',
                    'จุดจอด อ.ละแม',
                    460))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชุมพร',
                    'ทุ่งตะโก',
                    460))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชุมพร',
                    'จุดจอดทางแยกเข้า อ.สวี',
                    465))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชุมพร',
                    'จุดจอดบขส.ท่าแซะ',
                    465))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชุมพร',
                    'สถานีขนส่งผู้โดยสารเมืองใหม่',
                    475))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชุมพร',
                    'จุดจอด อ.หลังสวน',
                    475))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ชุมพร',
                    'จุดจอดสี่แยกปฐมพร',
                    480))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอดแม่คำหลวง',
                    750))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอด กรมขนส่ง(แม่สาย)',
                    755))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอดแม่ฟ้าหลวง',
                    755))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'สถานีขนส่งผู้โดยสาร อ.เทิง',
                    760))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอดแม่ต๋ำ',
                    765))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอด บ้านต้า',
                    765))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอด กรมขนส่ง(เทิง)',
                    770))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอด บ้านปล้อง',
                    770))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'สถานีขนส่งผู้โดยสาร อ.แม่สาย',
                    770))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอดท่าบ้านต้า',
                    775))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอด อ.พญาเม็งราย (บ้านปล้อง)',
                    775))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอดโชคชัย - แม่บง',
                    775))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอด อ.แม่สรวย',
                    780))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอดบ้านเหล่า',
                    780))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'เขื่อนภูมิพล',
                    780))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'ดอยหลวง',
                    780))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอด อ.เวียงเชียงรุ้ง',
                    780))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอดเชียงแสน',
                    785))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอดป่าแดด',
                    785))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอด อ.แม่จัน',
                    785))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'สถานีขนส่งผู้โดยสารระหว่างประเทศ อ.เชียงของ',
                    785))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอด ด่านสะพานมิตรภาพ ไทย(เชียงของ)',
                    790))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    '- สถานีขนส่งผู้โดยสาร อ.เชียงของ',
                    790))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงราย',
                    'จุดจอดบ้านศรีดอนเรือง',
                    790))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'จุดจอด อ.จอมทอง',
                    650))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'จุดจอด อ.ฝาง',
                    650))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'จุดจอด บ้านท่าตอน',
                    650))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'สถานีขนส่งผู้โดยสาร จ.เชียงใหม่ (กรมขนส่ง)',
                    655))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'จุดจอด อ.เชียงดาว',
                    655))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'จุดจอดไชยปราการ',
                    655))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'สถานีขนส่งผู้โดยสาร จ.เชียงใหม่ (อาเขต)',
                    660))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'จุดจอด อ.ฮอด',
                    660))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'จุดจอด แขวงหลวงน้ำทา(เชียงใหม่)',
                    665))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'จุดจอด แขวงอุดมชัย(เชียงใหม่)',
                    665))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'จุดจอด แขวงหลวงพระบาง(เชียงใหม่)',
                    670))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'เชียงใหม่',
                    'จุดจอดดอยเต่า',
                    670))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ตรัง',
                    'จุดจอดย่านตาขาว',
                    830))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ตรัง',
                    'สถานีขนส่งผู้โดยสาร จ.ตรัง',
                    830))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ตรัง',
                    'จุดจอดห้วยยอด',
                    840))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ตรัง',
                    'จุดจอด อันดามัน',
                    840))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ตราด',
                    'จุดจอด ต.แสนตุ้ง',
                    310))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ตราด',
                    'สถานีขนส่งผู้โดยสาร จ.ตราด',
                    310))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ตราด',
                    'จุดจอด บ้านบางกระดาน',
                    320))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ตราด',
                    'จุดจอดท่าเรืออ่าวธรรมชาติ',
                    320))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ตราด',
                    'ท่าเรือเซ็นเตอร์พอยท์',
                    330))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
                    'ตราด',
                    'จุดจอด อ.แหลมงอบ',
                    330))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    100))
    
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'กระบี่',
                    'จุดจอด อ.เขาพนม',
                    770))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'กระบี่',
                    'จุดจอด อ.เหนือคลอง',
                    770))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'กระบี่',
                    'สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    775))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'กระบี่',
                    'จุดจอด อ.ลำทับ',
                    780))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'กระบี่',
                    'จุดจอด อ.คลองท่อม',
                    785))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'กาฬสินธุ์',
                    'สถานีขนส่งผู้โดยสาร จ.กาฬสินธุ์',
                    545))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'กาฬสินธุ์',
                    'จุดจอด อ.สมเด็จ',
                    545))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ชุมพร',
                    'จุดจอด บ้านเขาปีบ',
                    440))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ชุมพร',
                    'จุดจอด อ.สวี',
                    440))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ชุมพร',
                    'ทุ่งตะโก',
                    445))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ชุมพร',
                    'จุดจอด อ.ละแม',
                    445))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ชุมพร',
                    'จุดจอดในเมืองชุมพร',
                    450))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ชุมพร',
                    'จุดจอดบขส.ท่าแซะ',
                    450))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ชุมพร',
                    'จุดจอดทางแยกเข้า อ.สวี',
                    450))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ชุมพร',
                    'จุดจอด อ.หลังสวน',
                    455))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ชุมพร',
                    'สถานีขนส่งผู้โดยสารเมืองใหม่',
                    455))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ชุมพร',
                    'จุดจอดสี่แยกปฐมพร',
                    460))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'เชียงใหม่',
                    'จุดจอด ต.แสนตุ้ง',
                    690))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'เชียงใหม่',
                    'สถานีขนส่งผู้โดยสาร จ.เชียงใหม่ (อาเขต)',
                    690))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ตรัง',
                    'จุดจอดย่านตาขาว',
                    830))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ตรัง',
                    'จุดจอดท่าเรืออ่าวธรรมชาติ',
                    830))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ตรัง',
                    'สถานีขนส่งผู้โดยสาร จ.ตรัง',
                    840))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ตรัง',
                    'จุดจอดห้วยยอด',
                    840))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'ตาก',
                    'สถานีขนส่งผู้โดยสาร อ .แม่สอด',
                    440))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'นครปฐม',
                    'จุดจอด อ.พุทธมณฑล',
                    740))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'นครพนม',
                    'สถานีขนส่งผู้โดยสาร จ.นครพนม',
                    740))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'นครพนม',
                    'จุดจอดค่ายพระยอด',
                    745))
    bangkok.add_route(Route('สถานีขนส่งผู้โดยสารกรุงเทพฯ(ถนนบรมราชชนนี)',
                    'นครพนม',
                    'จุดจอด ต.หนองญาติ',
                    750))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (เอกมัย)',
                    100))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'กรุงเทพมหานคร',
                    'กรมการขนส่งทางบก',
                    100))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ขอนแก่น',
                    'สถานีขนส่งผู้โดยสาร อ.พล',
                    310))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ขอนแก่น',
                    'สถานีขนส่งผู้โดยสาร จ.ขอนแก่น (บขส.3)',
                    310))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'จันทบุรี',
                    'สถานีขนส่งผู้โดยสาร จ.จันทบุรี',
                    250))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'จันทบุรี',
                    'จุดจอด ตลาดพลับพลา',
                    25))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'จันทบุรี',
                    'จุดจอด อ.ขลุง',
                    260))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'จันทบุรี',
                    'จุดจอด กุลพัฒน์',
                    260))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'จันทบุรี',
                    'จุดจอด อ.นายายอาม',
                    260))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ฉะเชิงเทรา',
                    'สถานีขนส่งผู้โดยสาร  จ.ฉะเชิงเทรา',
                    110))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ชลบุรี',
                    'จุดจอด ร้านอาหารครัวไท',
                    120))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ชลบุรี',
                    'จุดจอด กม10',
                    120))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ตราด',
                    'จุดจอด ต.แสนตุ้ง',
                    330))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ตราด',
                    'สถานีขนส่งผู้โดยสาร จ.ตราด',
                    330))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ตราด',
                    'จุดจอด บ้านบางกระดาน',
                    340))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ตราด',
                    'จุดจอดท่าเรืออ่าวธรรมชาติ',
                    340))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ตราด',
                    'ท่าเรือเซ็นเตอร์พอยท์',
                    345))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ตราด',
                    'จุดจอด อ.แหลมงอบ',
                    345))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'นครปฐม',
                    'จุดจอดบ้านเพ',
                    100))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'นครราชสีมา',
                    'สถานีขนส่งผู้โดยสาร จ.นครราชสีมา',
                    245))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ระยอง',
                    'จุดจอด อ.วังจันทร์',
                    190))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ระยอง',
                    'ท่า อ.แกลง',
                    195))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ระยอง',
                    'สถานีขนส่งผู้โดยสาร จ.ระยอง (ใหม่)',
                    195))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ระยอง',
                    'ท่ามาบตาพุด',
                    200))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'ระยอง',
                    'จุดจอด อ.บ้านฉาง',
                    200))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'สระแก้ว',
                    'สถานีขนส่งผู้โดยสาร อ.อรัญประเทศ',
                    230))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'สระแก้ว',
                    'จุดจอดตลาดโรงเกลือ',
                    230))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'หนองคาย',
                    'สถานีขนส่งผู้โดยสาร จ.หนองคาย',
                    580))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'อยุธยา',
                    'ท่าวังน้อย',
                    110))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'อุดรธานี',
                    'สถานีขนส่งผู้โดยสาร อ.กุมภวาปี',
                    54))
    bangkok.add_route(Route('ท่าอากาศยานสุวรรณภูมิ',
                    'อุดรธานี',
                    'สถานีขนส่งผู้โดยสาร จ.อุดรธานี',
                    540))
    
    ## province krabi ##

    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    780))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'กระบี่',
                    'สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    100))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'กระบี่',
                    'จุดจอด อ.ลำทับ',
                    100))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ชุมพร',
                    'จุดจอดสี่แยกปฐมพร',
                    320))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ชุมพร',
                    'จุดจอดบขส.ท่าแซะ',
                    320))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ชุมพร',
                    'จุดจอด อ.หลังสวน',
                    325))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ตรัง',
                    'จุดจอดห้วยยอด',
                    120))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ตรัง',
                    'สถานีขนส่งผู้โดยสาร จ.ตรัง',
                    120))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'นครศรีธรรมราช',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    120))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'นครศรีธรรมราช',
                    'สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    125))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'นครศรีธรรมราช',
                    'จุดจอด อ.ลำทับ',
                    130))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'นครศรีธรรมราช',
                    'จุดจอดสี่แยกปฐมพร',
                    130))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'นครศรีธรรมราช',
                    'จุดจอดบขส.ท่าแซะ',
                    130))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'นครศรีธรรมราช',
                    'จุดจอด อ.หลังสวน',
                    130))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'นครศรีธรรมราช',
                    'จุดจอดห้วยยอด',
                    135))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'นครศรีธรรมราช',
                    'สถานีขนส่งผู้โดยสาร จ.ตรัง',
                    135))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'นครศรีธรรมราช',
                    'จุดจอดห้วยยอด',
                    140))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'นครศรีธรรมราช',
                    'สถานีขนส่งผู้โดยสาร จ.ตรัง',
                    140))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'พังงา',
                    'สถานีขนส่งผู้โดยสาร จ.พังงา',
                    140))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'พังงา',
                    'จุดจอด อ.ตะกั่วทุ่ง',
                    140))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'พัทลุง',
                    'จุดจอด แยกท่ามิหรำ',
                    150))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'เพชรบุรี',
                    'จุดจอดเพชรบุรี',
                    640))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'เพชรบุรี',
                    'จุดจอด ร้านแม่แวว',
                    640))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'เพชรบุรี',
                    'จุดจอดชะอำ',
                    650))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ภูเก็ต',
                    'สถานีขนส่งผู้โดยสาร จ.ภูเก็ต',
                    170))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ภูเก็ต',
                    'สงขลา',
                    170))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ภูเก็ต',
                    'สถานีขนส่งผู้โดยสาร อ.หาดใหญ่',
                    175))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ภูเก็ต',
                    'สมุทรสงคราม',
                    175))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ภูเก็ต',
                    'จุดจอด ต.บางเค็ม',
                    180))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ภูเก็ต',
                    'จุดจอดแยกแม่กลอง',
                    180))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'สมุทรสาคร',
                    'จุดจอดมหาชัย',
                    170))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'สุราษฎร์ธานี',
                    'จุดจอด อ.พระแสง',
                    170))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'สุราษฎร์ธานี',
                    'จุดจอดแยกบ้านส้อง',
                    175))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'สุราษฎร์ธานี',
                    'จุดจอดร้านวังกุ้ง(สุราษฎร์)',
                    175))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'สุราษฎร์ธานี',
                    'สหกรณ์สุราษฎร์',
                    180))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'สุราษฎร์ธานี',
                    'จุดจอด อ.ไชยา',
                    180))
    krabi.add_route(Route('จุดขึ้น อ.คลองท่อม',
                    'ภูเก็ต',
                    'จุดจอดแยกแม่กลอง',
                    180))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (ถนนบรมราชชนนี)',
                    780))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    780))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'กระบี่',
                    'จุดจอด อ.เหนือคลอง',
                    110))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'กระบี่',
                    'จุดจอด อ.คลองท่อม',
                    115))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'กระบี่',
                    'จุดจอด อ.ลำทับ',
                    110))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ชุมพร',
                    'จุดจอดบขส.ท่าแซะ',
                    320))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ชุมพร',
                    'จุดจอดทางแยกเข้า อ.สวี',
                    320))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ชุมพร',
                    'สถานีขนส่งผู้โดยสารเมืองใหม่',
                    335))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ชุมพร',
                    'จุดจอด อ.หลังสวน',
                    340))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ชุมพร',
                    'จุดจอดสี่แยกปฐมพร',
                    340))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ตรัง',
                    'จุดจอดห้วยยอด',
                    105))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ตรัง',
                    'สถานีขนส่งผู้โดยสาร จ.ตรัง',
                    110))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'นครศรีธรรมราช',
                    'จุดจอด อ.ทุ่งใหญ่',
                    100))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดกุยบุรี',
                    525))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ประจวบคีรีขันธ์',
                    'จุดจอด สน.ทับสะแก',
                    530))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ประจวบคีรีขันธ์',
                    'จุดจอด อ.ปราณบุรี',
                    530))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ประจวบคีรีขันธ์',
                    'จุดจอด อ.หัวหิน',
                    535))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดทับสะแก(ร้านมาลี)',
                    550))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดประจวบคีรีขันธ์',
                    550))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดศูนย์บริการทางหลวงเขาโพธิ์',
                    550))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'พังงา',
                    'สถานีขนส่งผู้โดยสาร จ.พังงา',
                    130))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'พังงา',
                    'บขส. โคกกลอย',
                    135))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'พังงา',
                    'จุดจอด อ.ทับปุด',
                    140))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'พังงา',
                    'จุดจอด อ.ตะกั่วทุ่ง',
                    140))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'พังงา',
                    'สถานีขนส่งผู้โดยสาร อ.ตะกั่วป่า',
                    150))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'พังงา',
                    'สถานีขนส่งผู้โดยสาร อ.คุระบุรี',
                    150))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'พัทลุง',
                    'จุดจอด แยกท่ามิหรำ',
                    155))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'เพชรบุรี',
                    'จุดจอดเพชรบุรี',
                    630))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'เพชรบุรี',
                    'จุดจอด ร้านแม่แวว',
                    630))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'เพชรบุรี',
                    'จุดจอดชะอำ',
                    640))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ภูเก็ต',
                    'สถานีขนส่งผู้โดยสาร จ.ภูเก็ต',
                    170))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ระนอง',
                    'จุดจอด อ.กะเปอร์',
                    350))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ระนอง',
                    'สถานีขนส่งผู้โดยสาร จ.ระนอง',
                    350))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'สงขลา',
                    'สถานีขนส่งผู้โดยสาร อ.หาดใหญ่',
                    290))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'สงขลา',
                    'จุดจอด อ.ด่านนอก',
                    290))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    780))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'กระบี่',
                    'จุดจอด อ.คลองท่อม',
                    110))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'กระบี่',
                    'สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    110))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'ชุมพร',
                    'จุดจอดสี่แยกปฐมพร',
                    290))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดกุยบุรี',
                    540))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ประจวบคีรีขันธ์',
                    'จุดจอด สน.ทับสะแก',
                    540))
    krabi.add_route(Route('สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    'ประจวบคีรีขันธ์',
                    'จุดจอด อ.ปราณบุรี',
                    540))
    krabi.add_route(Route('จุดจอด อ.ปลายพระยา',
                    'ประจวบคีรีขันธ์',
                    'จุดจอด อ.หัวหิน',
                    550))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดศูนย์บริการทางหลวงเขาโพธิ์',
                    550))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดทับสะแก(ร้านมาลี)',
                    550))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดประจวบคีรีขันธ์',
                    555))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'เพชรบุรี',
                    'จุดจอดเพชรบุรี',
                    640))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'เพชรบุรี',
                    'จุดจอด ร้านแม่แวว',
                    650))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'เพชรบุรี',
                    'สมุทรสงคราม',
                    650))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'เพชรบุรี',
                    'จุดจอดแยกแม่กลอง',
                    650))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'เพชรบุรี',
                    'จุดจอด ต.บางเค็ม',
                    655))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'สมุทรสาคร',
                    'จุดจอดมหาชัย',
                    730))
    krabi.add_route(Route('จุดขึ้น อ.ปลายพระยา',
                    'สุราษฎร์ธานี',
                    'จุดจอดร้านวังกุ้ง(สุราษฎร์)',
                    120))
    krabi.add_route(Route('จุดขึ้น อ.อ่าวลึก',
                    'สมุทรสาคร',
                    'จุดจอดมหาชัย',
                    740))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    790))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (ถนนบรมราชชนนี)',
                    790))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'กระบี่',
                    'สถานีขนส่งผู้โดยสาร จ.กระบี่',
                    115))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'ชุมพร',
                    'จุดจอด อ.หลังสวน',
                    320))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'ชุมพร',
                    'จุดจอดสี่แยกปฐมพร',
                    320))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'ชุมพร',
                    'จุดจอดบขส.ท่าแซะ',
                    325))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'นครศรีธรรมราช',
                    'จุดจอด อ.ทุ่งใหญ่',
                    100))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดกุยบุรี',
                    540))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'ประจวบคีรีขันธ์',
                    'จุดจอด สน.ทับสะแก',
                    540))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'ประจวบคีรีขันธ์',
                    'จุดจอด อ.ปราณบุรี',
                    540))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'ประจวบคีรีขันธ์',
                    'จุดจอด อ.หัวหิน',
                    550))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดศูนย์บริการทางหลวงเขาโพธิ์',
                    550))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดทับสะแก(ร้านมาลี)',
                    550))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดประจวบคีรีขันธ์',
                    555))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'พังงา',
                    'จุดจอด อ.ทับปุด',
                    140))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'พังงา',
                    'สถานีขนส่งผู้โดยสาร จ.พังงา',
                    140))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'พังงา',
                    'บขส. โคกกลอย',
                    145))
    krabi.add_route(Route('จุดขึ้น อ.เหนือคลอง',
                    'เพชรบุรี',
                    'จุดจอดเพชรบุรี',
                    645))
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    785))
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    785))
    
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดทับสะแก(ร้านมาลี)',
                    545))
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดกุยบุรี',
                    545))
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'ประจวบคีรีขันธ์',
                    'จุดจอด อ.หัวหิน',
                    550))
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดศูนย์บริการทางหลวงเขาโพธิ์',
                    555))
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดประจวบคีรีขันธ์',
                    555))
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'ประจวบคีรีขันธ์',
                    'จุดจอดเกาะยายฉิม',
                    555))
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'เพชรบุรี',
                    'จุดจอดเพชรบุรี',
                    640))
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'สมุทรสงคราม',
                    'จุดจอด ต.บางเค็ม',
                    700))
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'สมุทรสาคร',
                    'จุดจอดมหาชัย',
                    740))
    krabi.add_route(Route('ท่าเรือเกาะลันตา(บ้านหัวหิน)',
                    'สุราษฎร์ธานี',
                    'จุดจอดร้านวังกุ้ง(สุราษฎร์)',
                    115))
    krabi.add_route(Route('จุดขึ้น อ.เขาพนม',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (ถนนบรมราชชนนี)',
                    780))
    krabi.add_route(Route('จุดขึ้น อ.เขาพนม',
                    'กรุงเทพมหานคร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    785))
    krabi.add_route(Route('จุดขึ้น อ.เขาพนม',
                    'ชุมพร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (ถนนบรมราชชนนี)',
                    780))
    krabi.add_route(Route('จุดขึ้น อ.เขาพนม',
                    'ชุมพร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)',
                    785))
    krabi.add_route(Route('จุดขึ้น อ.เขาพนม',
                    'ชุมพร',
                    'สถานีขนส่งผู้โดยสารกรุงเทพฯ (ถนนบรมราชชนนี)',
                    780))
    
    

    # bus ####################################################

    bus_1 = Bus('1นค5463', 'on station', [])
    bus_controller.add_bus(bus_1)
    bus_2 = Bus('3นถ4263', 'on station', [])
    bus_controller.add_bus(bus_2)
    bus_3= Bus('1ตก9954', 'on station', [])
    bus_controller.add_bus(bus_3)

    # seat ####################################################

    bus_1.add_seat(Seat('A01', False))
    bus_1.add_seat(Seat('A02', False))
    bus_1.add_seat(Seat('A03', False))
    bus_1.add_seat(Seat('A04', False))
    bus_1.add_seat(Seat('A05', False))
    bus_1.add_seat(Seat('A06', False))
    bus_1.add_seat(Seat('A07', False))
    bus_1.add_seat(Seat('A08', False))
    bus_1.add_seat(Seat('A09', False))
    bus_1.add_seat(Seat('A10', False))
    bus_1.add_seat(Seat('A11', False))
    bus_1.add_seat(Seat('A12', False))
    bus_1.add_seat(Seat('A13', False))
    bus_1.add_seat(Seat('A14', False))
    bus_1.add_seat(Seat('A15', False))
    bus_1.add_seat(Seat('A16', False))
    bus_1.add_seat(Seat('A17', False))
    bus_1.add_seat(Seat('A18', False))
    bus_1.add_seat(Seat('A19', False))
    bus_1.add_seat(Seat('A20', False))
    bus_1.add_seat(Seat('A21', False))
    bus_1.add_seat(Seat('A22', False))
    bus_1.add_seat(Seat('A23', False))
    bus_1.add_seat(Seat('A24', False))
    bus_1.add_seat(Seat('A25', False))
    bus_1.add_seat(Seat('A26', False))
    bus_1.add_seat(Seat('A27', False))
    bus_1.add_seat(Seat('A28', False))
    bus_1.add_seat(Seat('A29', False))
    bus_1.add_seat(Seat('A30', False))
    bus_1.add_seat(Seat('A31', False))
    bus_1.add_seat(Seat('A32', False))
    bus_1.add_seat(Seat('A33', False))
    bus_1.add_seat(Seat('A34', False))
    bus_1.add_seat(Seat('A35', False))
    bus_1.add_seat(Seat('A36', False))
    
    bus_2.add_seat(Seat('A01', False))
    bus_2.add_seat(Seat('A02', False))
    bus_2.add_seat(Seat('A03', False))
    bus_2.add_seat(Seat('A04', False))
    bus_2.add_seat(Seat('A05', False))
    bus_2.add_seat(Seat('A06', False))
    bus_2.add_seat(Seat('A07', False))
    bus_2.add_seat(Seat('A08', False))
    bus_2.add_seat(Seat('A09', False))
    bus_2.add_seat(Seat('A10', False))
    bus_2.add_seat(Seat('A11', False))
    bus_2.add_seat(Seat('A12', False))
    bus_2.add_seat(Seat('A13', False))
    bus_2.add_seat(Seat('A14', False))
    bus_2.add_seat(Seat('A15', False))
    bus_2.add_seat(Seat('A16', False))
    bus_2.add_seat(Seat('A17', False))
    bus_2.add_seat(Seat('A18', False))
    bus_2.add_seat(Seat('A19', False))
    bus_2.add_seat(Seat('A20', False))
    bus_2.add_seat(Seat('A21', False))
    bus_2.add_seat(Seat('A22', False))
    bus_2.add_seat(Seat('A23', False))
    bus_2.add_seat(Seat('A24', False))
    bus_2.add_seat(Seat('A25', False))
    bus_2.add_seat(Seat('A26', False))
    bus_2.add_seat(Seat('A27', False))
    bus_2.add_seat(Seat('A28', False))
    bus_2.add_seat(Seat('A29', False))
    bus_2.add_seat(Seat('A30', False))
    bus_2.add_seat(Seat('A31', False))
    bus_2.add_seat(Seat('A32', False))
    bus_2.add_seat(Seat('A33', False))
    bus_2.add_seat(Seat('A34', False))
    bus_2.add_seat(Seat('A35', False))
    bus_2.add_seat(Seat('A36', False))
    
    bus_3.add_seat(Seat('A01', False))
    bus_3.add_seat(Seat('A02', False))
    bus_3.add_seat(Seat('A03', False))
    bus_3.add_seat(Seat('A04', False))
    bus_3.add_seat(Seat('A05', False))
    bus_3.add_seat(Seat('A06', False))
    bus_3.add_seat(Seat('A07', False))
    bus_3.add_seat(Seat('A08', False))
    bus_3.add_seat(Seat('A09', False))
    bus_3.add_seat(Seat('A10', False))
    bus_3.add_seat(Seat('A11', False))
    bus_3.add_seat(Seat('A12', False))
    bus_3.add_seat(Seat('A13', False))
    bus_3.add_seat(Seat('A14', False))
    bus_3.add_seat(Seat('A15', False))
    bus_3.add_seat(Seat('A16', False))
    bus_3.add_seat(Seat('A17', False))
    bus_3.add_seat(Seat('A18', False))
    bus_3.add_seat(Seat('A19', False))
    bus_3.add_seat(Seat('A20', False))
    bus_3.add_seat(Seat('A21', False))
    bus_3.add_seat(Seat('A22', False))
    bus_3.add_seat(Seat('A23', False))
    bus_3.add_seat(Seat('A24', False))
    bus_3.add_seat(Seat('A25', False))
    bus_3.add_seat(Seat('A26', False))
    bus_3.add_seat(Seat('A27', False))
    bus_3.add_seat(Seat('A28', False))
    bus_3.add_seat(Seat('A29', False))
    bus_3.add_seat(Seat('A30', False))
    bus_3.add_seat(Seat('A31', False))
    bus_3.add_seat(Seat('A32', False))
    bus_3.add_seat(Seat('A33', False))
    bus_3.add_seat(Seat('A34', False))
    bus_3.add_seat(Seat('A35', False))
    bus_3.add_seat(Seat('A36', False))

create_instance()

# bus_controller.add_booking('chamaiporn',
#                            'credit card',
#                            540,
#                            '10-02-2024')

# bus_controller.add_ticket('01',
#                           'booking',
#                           'A01')

## check add schdule ##
# schedule = bus_controller.add_schedule('กรุงเทพมหานคร', '')


print("-----------------------------------------------------------------")
# check search route by province
province_route = bus_controller.search_route_by_province('กระบี่')
for province in province_route:
    for route in province.get_route_lst:
        print(f"ต้นทาง : {province.get_province_name} - {route.get_source_station}")
        print(f"ปลายทาง : {route.get_destination_province} - {route.get_destination_station}")
        print("-----------------------------------------------------------------")
        break

    
# # check search ticket by ticket id
# ticket_list = bus_controller.search_ticket_by_ticket_id('01')
# for ticket_id, schedule, seat_number in ticket_list:
#     print(f"{ticket_id} รอบรถคือ {schedule} หมายเลขที่นั่ง {seat_number}")
#     print("-----------------------------------------------------------------")
#     break

# # check search bus by bus license
# bus_lst = bus_controller.search_bus_by_bus_license('1นค5463')
# for bus_license, location, seat_lst  in bus_lst:
#     print(f"เลขทะเบียนนรถ {bus_license} สถานที่รถอยู่ปัจจุบัน {location}")
#     for seat_number, status_seat in seat_lst:
#         print(f"เลขที่นั่ง {seat_number} สถานะ {status_seat}")
#         print("-----------------------------------------------------------------")
#         break

# check add passenger when passenger paid
# passenger = bus_controller.add_passenger('0001',
#                                          'chamaiporn',
#                                          'female',
#                                          '090393820',
#                                          'hdjgjedr@gmail.com',
#                                          True)

# for user_id, username, password, name, gender, tel, email, status_payment in passenger:
#     print(f"{user_id} รอบรถคือ {username} หมายเลขที่นั่ง {password}")
#     print("-----------------------------------------------------------------")
#     break
