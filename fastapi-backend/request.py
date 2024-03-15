import requests

requests.post('http://127.0.0.1:8000/api/info', data={
"name_passenger": "Chamaiporn",
"surname_passenger" : "Phomrasri",
"gender" : "Female",
"tel" : "0907379033",
"email" : "hix@gmail.com",
"status_payment" : False,
"payment_option" : "Credit Card",
"bus_license" : "1นค5463",
"seat_number" : "A02",
"source_province" : 'กรุงเทพมหานคร',
"source_station" : 'สถานีขนส่งผู้โดยสารกรุงเทพฯ(รังสิต)',
"destination_province" : 'ฉะเชิงเทรา',
"destination_station" : 'ท่าศรีราชา',
"departure_date" : "15/03/2024"
})