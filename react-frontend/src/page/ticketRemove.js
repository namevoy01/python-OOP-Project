import React, { useState } from 'react';
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';
import Swal from 'sweetalert2';

function useTicketRemove() {
    const [showModal, setShowModal] = useState(false);
    const [ticketNumber, setTicketNumber] = useState('');
    const [loading, setLoading] = useState(false);
    const [ticketData, setTicketData] = useState(null); 

    const handleTicketNumberChange = (event) => {
        setTicketNumber(event.target.value);
    };

    const cancelTicket = async () => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/cancel?ticket_id=${ticketNumber}`, {
                method: 'DELETE', 
                headers: {
                    'Content-Type': 'application/json',
                    
                },

            });

            if (!response.ok) {
                throw new Error('ไม่สามารถยกเลิกตั๋วได้');
            }

        } catch (error) {
            console.error('เกิดข้อผิดพลาดในการยกเลิกตั๋ว:', error);
        }
    };

    const handleCancelTicket = () => {
        setLoading(true);
        fetch(`http://127.0.0.1:8000/api/ticket?ticket_id=${ticketNumber}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then(response => {
                setLoading(false);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data) {
                    setTicketData(data);
                    setShowModal(true);
                } else {
                    Swal.fire({
                        icon: "error",
                        title: "มีบางอย่างผิดพลาด",
                        text: "กรุณากรอก   หมายเลขตั๋วให้ถูกต้อง",
                    });;
                }
            })
            .catch(error => {
                setLoading(false);
                console.error('There was a problem with your fetch operation:', error);
            });
    };
    return (
        <div>
            <Navbar />
            <div className="max-w-screen-2xl mx-auto xl:w-10/12 lg: w-10/12">
                <div className='flex justify-between'>
                    <div className='mt-5 text-2xl mb-8'>
                        ค้นหาตั๋ว
                    </div>
                    <div className='mt-5 '>
                        <div className='flex '>
                            <Link to='/'> <div className='text-pink-400'>กลับหน้าแรก</div></Link>
                        </div>
                    </div>
                </div>
                <div className='flex justify-center mt-5'>
                    <input
                        onChange={handleTicketNumberChange}
                        value={ticketNumber}
                        className="shadow appearance-none border rounded w-6/12 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        id="ticketNumber"
                        type="text"
                        placeholder="ใส่หมายเลขตั๋วที่ต้องการยกเลิก"
                    />
                    {ticketNumber.length > 0 ? (
                        <button
                            onClick={handleCancelTicket}
                            disabled={loading}
                            type="button"
                            className="ms-3 text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2  text-lg ">
                            {loading ? 'กำลังโหลด...' : 'ค้นหา'}
                        </button>
                    ) : (
                        <button
                            onClick={handleCancelTicket}
                            disabled
                            type="button"
                            className="disabled:opacity-50 disabled:cursor-not-allowed ms-3 text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2  text-lg ">
                            {loading ? 'กำลังโหลด...' : 'ค้นหา'}
                        </button>
                    )}



                </div>
            </div>
            {showModal && ticketData && ticketData.length >= 1 ? (
                <div>
                    <div className="fixed inset-0 z-10 overflow-y-auto">
                        <div
                            className="fixed inset-0 w-full h-full bg-black opacity-40"
                            onClick={() => setShowModal(false)}
                        ></div>
                        <div className="flex items-center min-h-screen px-4 py-8">
                            <div className="relative w-full max-w-lg p-4 mx-auto bg-white rounded-md shadow-lg">
                                <div className="mt-3 sm:flex">
                                    <div className="mt-2 text-center sm:ml-4 sm:text-left">
                                        <h4 className="text-lg font-medium text-gray-800">
                                            ยกเลิกตั๋ว
                                        </h4>
                                        <div className="mt-2 text-[15px] leading-relaxed text-gray-500  mb-3">
                                            {ticketData.map((ticket) => (
                                                <span className='grid grid-cols-2 gap-4' key={ticket.ticket_id}>
                                                    <span className=''>รหัสตั๋ว:  {ticket.ticket_id}</span>
                                                    <span className=''>ทะเบียนรถ:  {ticket.bus_license}</span>
                                                    <span className=''>จังหวัดต้นทาง:  {ticket.source_province}</span>
                                                    <span className=''>จังหวัดปลายทาง:  {ticket.destination_province}</span>
                                                    <span className=''>จุดขึ้นรถ:  {ticket.source_station}</span>
                                                    <span className=''>จุดลงรถ:  {ticket.destination_station}</span>
                                                    <span className=''>เวลารถออก:  {ticket.departure_time}</span>
                                                    <span className='col-start-1 col-end-3'>ชื่อ: {ticket.name_passenger} นามสกุล: {ticket.surname_passenger}</span>
                                                    {ticket.status_payment == true ? (
                                                        <div className='col-start-1 col-end-3'>
                                                            สถานะการชำระเงิน:<span class="ms-2 inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">ชำระเงินแล้ว</span>
                                                        </div>
                                                    ) : (
                                                        <div className='col-start-1 col-end-3'>
                                                            สถานะการชำระเงิน: <span class=" ms-1 bg-yellow-100 text-yellow-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-yellow-900 dark:text-yellow-300">รอการชำระเงิน</span>
                                                        </div>
                                                    )}

                                                    <span className='col-start-1 col-end-3'>เบอร์โทร: {ticket.tel}</span>
                                                    <span className='col-start-1 col-end-3'>Email: {ticket.email}</span>

                                                </span>

                                            ))}

                                        </div>
                                        หักค่าธรรมเนียมการคืนตั๋ว 10% จากอัตราค่าโดยสาร และ คิดค่าธรรมเนียมการโอนเงิน 30 บาท/ครั้ง
                                        <button
                                            className="w-full mt-2 p-2.5 flex-1 text-white bg-red-600 rounded-md outline-none ring-offset-2 ring-red-600 focus:ring-2"
                                            onClick={() => {
                                                setShowModal(false);
                                                cancelTicket();

                                            }}
                                        >
                                            ยกเลิกตั๋ว
                                        </button>
                                        <button
                                            className="w-full mt-2 p-2.5 flex-1 text-gray-800 rounded-md outline-none border ring-offset-2 ring-indigo-600 focus:ring-2"
                                            onClick={() => setShowModal(false)}
                                        >
                                            Cancel
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            ) : (
                <div>
                </div>
            )}

        </div>
    );
}

export default useTicketRemove;
