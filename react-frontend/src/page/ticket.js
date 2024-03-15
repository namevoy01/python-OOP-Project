import React, { useState, useEffect } from 'react';
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';

const Ticket = () => {

    const [source_ticket, set_ticket] = useState([]);
    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/ticket?ticket_id=35301073')
            .then(response => response.json())
            .then(data => {
                if (data && data.length > 0) {
                    set_ticket(data[0]); // Assuming the response is an array and you're interested in the first element
                } else {
                    console.error('Empty or invalid response from the API');
                }
            })
            .catch(error => console.error('Error fetching ticket data:', error));
    }, []);

    console.log(source_ticket);
    return (
        <div>
            <Navbar />
            <div>
                <div className="max-w-screen-2xl mx-auto xl:w-10/12 lg: w-10/12">
                    <div className='flex justify-between'>
                        <div className='mt-5 text-2xl mb-8'>
                            กำหนดการเดินทาง
                        </div>
                        <div className='mt-5'>
                            <div className='flex '>
                                <div className='text-gray-400'>ค้นหาเที่ยวรถ</div>
                                <div className='mx-2'>--</div>
                                <div className='text-gray-400'>เลือกเที่ยวรถ</div>
                                <div className='mx-2'>--</div>
                                <div className='text-gray-400'>เลือกที่นั่ง</div>
                                <div className='mx-2'>--</div>
                                <div className='text-gray-400'>ผู้โดยสารและชำระเงิน</div>
                                <div className='mx-2'>--</div>
                                <div className='text-pink-400'>กำหนดการเดินทาง</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="max-w-screen-2xl mx-auto xl:w-10/12 lg: w-10/12">

                    <div className="py-8 px-8 bg-white rounded-xl border-solid border-2 border-gray-100 shadow-md  space-y-2 mt-5">
                        <div className="grid grid-cols-2 gap-4 ">
                            <div className="col-span-2">
                                <b> รหัสตั๋ว : 35301074</b>
                            </div>

                            <div className="col-span-2">
                                <div className="flex">
                                    <div className="mt-1.5 me-2"> จาก </div>
                                    <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" value={`จ.กรุงเทพมหานคร จุดขึ้น สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)
`} disabled />
                                </div>
                            </div>

                            <div className="col-span-2">
                                <div className="flex">
                                    <div className="mt-1.5 me-3"> ถึง </div>
                                    <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" value={`จ.จันทบุรี จุดลง สถานีขนส่งผู้โดยสาร จ.จันทบุรี`} disabled />
                                </div>
                            </div>

                            <div className="col-span-2">
                                <div className="flex">
                                    <div className="mt-1.5 me-3"> รถออกเวลา : 11.40 น.</div>
                                </div>
                            </div>

                            <div className="col-span-2">
                                <div className="flex">
                                    <div className="mt-1.5 me-3"> หมายเลขทะเบียนรถ : 1นค5463</div>
                                </div>
                            </div>

                            <div className="col-span-2">
                                <div className="flex">
                                    <div className="mt-1.5 me-3"> {source_ticket.name_passenger} {source_ticket.surname_passenger}</div>
                                </div>
                            </div>

                            <div className="col-span-2">
                                <div className="flex">
                                    {source_ticket.status_payment == false ? (
                                        <div className="mt-1.5 me-3"> สถานะ: <span className="ms-2 inline-flex items-center rounded-md bg-yellow-50 px-2 py-1 text-xs font-medium text-yellow-700 ring-1 ring-inset ring-yellow-600/20">ยังไม่ชำระเงิน</span></div>
                                    ) : (
                                        <div className="mt-1.5 me-3"> สถานะ: <span className="ms-2 inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">Paid</span></div>
                                    )}
                                </div>
                            </div>

                            <div className="col-span-2">
                                <b><div className="mt-1.5 me-3"> รายละเอียดข้อมูลติดต่อ:</div></b>
                            </div>

                            <div className="col-span-2 mt-4">
                                เบอร์โทร: 0999999999
                            </div>

                            <div className="col-span-2 mt-4">
                                อีเมล: email@gmail.com
                            </div>

                            <div className="col-span-2 flex justify-center">
                                <Link to="/">
                                    <button type="button" className="mt-5 text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg">กลับหน้าแรก</button>
                                </Link>
                            </div>
                        </div>
                    </div>




                </div>
            </div>
        </div>
    );
};

export default Ticket;
