import React, { useState, useEffect } from 'react';
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { format, parse } from 'date-fns';

const Inputfill = () => {
    const { bus_license, province, station, destination, destinationstation, date, time, amount,seat } = useParams();
    console.log(province, station, destination, destinationstation, date, time, bus_license, amount,seat);

    const parsedDate = parse(date, 'dd-MM-yyyy', new Date());
    const formattedDate = format(parsedDate, 'dd/MM/yyyy');

    const [source_info, set_info] = useState([]);

    const backToPreviousPage = () => {
        window.history.length > 1 ? window.history.go(-1) : window.location.href = '/';
    };

    const amountUp = parseInt(amount, 10) + 20;
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/info_trip?source_province=${encodeURIComponent(province)}&source_station=${encodeURIComponent(station)}&destination_province=${encodeURIComponent(destination)}&destination_station=${encodeURIComponent(destinationstation)}&departure_date=${encodeURIComponent(date)}&departure_time=${encodeURIComponent(time)}&bus_license=${encodeURIComponent(bus_license)}&seat_number=${encodeURIComponent(seat)}`);
                const data = await response.json();
                if (data && data.length > 0) {
                    set_info(data[0]); // Assuming the response is an array and you're interested in the first element
                } else {
                    console.error('Empty or invalid response from the API');
                }
            } catch (error) {
                console.error('Error fetching ticket data:', error);
            }
        };
    
        fetchData();
    }, []);

    console.log(source_info);
    return (
        <div>
            <Navbar />
            <div className="max-w-screen-2xl mx-auto xl:w-10/12 lg: w-10/12">
                <div className='flex justify-between'>
                    <div className='mt-5 text-2xl mb-8'>
                        ผู้โดยสารและชำระเงิน
                    </div>
                    <div className='mt-5'>
                        <div className='flex '>
                            <div className='text-gray-400'>ค้นหาเที่ยวรถ</div>
                            <div className='mx-2'>--</div>
                            <div className='text-gray-400'>เลือกเที่ยวรถ</div>
                            <div className='mx-2'>--</div>
                            <div className='text-gray-400'>เลือกที่นั่ง</div>
                            <div className='mx-2'>--</div>
                            <div className='text-pink-400'>ผู้โดยสารและชำระเงิน</div>
                            <div className='mx-2'>--</div>
                            <div className='text-gray-400'>กำหนดการเดินทาง</div>
                        </div>
                    </div>
                </div>

                <div className="flex">
                    <div className="flex-1">
                        <div className="bg-white max-w-full shadow overflow-hidden sm:rounded-lg">
                            <div className="px-4 py-5 sm:px-6">
                                <h3 class="text-lg leading-6 font-medium text-gray-900 ">
                                    ข้อมูลผู้โดยสารที่เดินทาง

                                </h3>
                            </div>
                            <div class="border-t border-gray-200 ">
                                <dl>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
                                        <dt class="text-sm font-medium text-gray-500">
                                            ที่นั่ง
                                        </dt>
                                        <select id="countries" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                            <option selected>ระบุเพศ</option>
                                            <option value="US">United States</option>
                                            <option value="CA">Canada</option>
                                            <option value="FR">France</option>
                                            <option value="DE">Germany</option>
                                        </select>
                                        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="ชื่อ" />
                                        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="นามสกุล" />

                                     
                                    </div>


                                </dl>
                            </div>

                        </div>

                        <div className="mt-7 bg-white max-w-full shadow overflow-hidden sm:rounded-lg">
                            <div className="px-4 py-5 sm:px-6">
                                <h3 class="text-lg leading-6 font-medium text-gray-900 ">
                                    ข้อมูลผู้ติดต่อ

                                </h3>
                            </div>
                            <div class="border-t border-gray-200 ">
                                <dl>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
                                        <dt class="text-sm font-medium text-gray-500">
                                            ข้อมูลผู้ติดต่อ
                                        </dt>

                                        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="ชื่อ" />
                                        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="นามสกุล" />
                                        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="โทรศัพทร์มือถือ" />
                                        <dt class="text-sm font-medium text-gray-500">
                                            อีเมล
                                        </dt>

                                        <input class="col-start-2 col-end-5 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="กรอกอีเมล เพื่อรับข้อมูลการจอง" />

                                    </div>

                                </dl>
                            </div>

                        </div>

                        <div className="mt-7 bg-white max-w-full shadow overflow-hidden sm:rounded-lg">
                            <div className="px-4 py-5 sm:px-6">
                                <h3 class="text-lg leading-6 font-medium text-gray-900 ">
                                    ยอดเงินรวมที่ต้องชำระ


                                </h3>
                            </div>
                            <div class="border-t border-gray-200 ">
                                <dl>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                                        <dt class="text-sm font-medium text-gray-500">
                                            ราคาตั๋ว
                                        </dt>
                                        <div className='text-center'>{amount}</div>
                                        <div className='text-end'>1,144.00 (บาท) </div>


                                        <dt class="text-sm font-medium text-gray-500">
                                            ค่าดำเนินการจัดการ
                                        </dt>
                                        <div className='text-center'>20</div>
                                        <div className='text-end'>20 (บาท) </div>

                                        <dt class="text-lg font-medium text-gray-500">
                                            <b> ราคารวม</b>
                                        </dt>
                                        <div className='text-lg col-start-2 col-end-4 text-end '><b> {amountUp} </b></div>

                                    </div>


                                </dl>
                            </div>
                        </div>

                        <div className="mt-7 bg-white max-w-full shadow overflow-hidden sm:rounded-lg">
                            <div className="px-4 py-5 sm:px-6">
                                <h3 className="text-lg leading-6 font-medium text-gray-900 ">
                                    วิธีการชำระเงิน
                                </h3>
                            </div>
                            <div class="border-t border-gray-200 ">
                                <dl>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-1 sm:gap-4 sm:px-6">

                                        <select id="countries" className=" bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                            <option selected>กรุณาเลือก</option>
                                            <option value="US">United States</option>
                                            <option value="CA">Canada</option>
                                            <option value="FR">France</option>
                                            <option value="DE">Germany</option>
                                        </select>



                                    </div>


                                </dl>
                            </div>
                        </div>
                    </div>


                    <div className="ms-5 ">
                        <div className="bg-white max-w-full shadow overflow-hidden sm:rounded-lg  py-5">
                            <h3 className="text-lg leading-6 font-medium text-gray-900 m-3">
                                ข้อมูลการเดินทาง
                            </h3>
                            <div class="border-t border-gray-200 ">
                                <dl>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-2 sm:gap-4 sm:px-6">
                                        <dt class="text-sm font-medium text-gray-500">
                                            จังหวัดต้นทาง
                                        </dt>
                                        {source_info.source_province}
                                    </div>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-2 sm:gap-4 sm:px-6">
                                        <dt class="text-sm font-medium text-gray-500">
                                            จุดขึ้น
                                        </dt>
                                        {source_info.source_station}

                                    </div>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-2 sm:gap-4 sm:px-6">
                                        <dt class="text-sm font-medium text-gray-500">
                                            จังหวัดปลายทาง
                                        </dt>
                                        {source_info.destination_province}

                                    </div>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-2 sm:gap-4 sm:px-6">
                                        <dt class="text-sm font-medium text-gray-500">
                                            จุดลงรถ
                                        </dt>
                                        {source_info.destination_station}
                                    </div>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-2 sm:gap-4 sm:px-6">
                                        <dt class="text-sm font-medium text-gray-500">
                                            วันที่จอง
                                        </dt>
                                        {formattedDate}
                                    </div>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-2 sm:gap-4 sm:px-6">
                                        <dt class="text-sm font-medium text-gray-500">
                                            เวลา
                                        </dt>
                                        {source_info.departure_time}
                                    </div>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-2 sm:gap-4 sm:px-6">
                                        <dt class="text-sm font-medium text-gray-500">
                                            หมายเลขทะเบียนรถ
                                        </dt>
                                        {source_info.bus_license}

                                    </div>
                                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-2 sm:gap-4 sm:px-6">
                                        <dt class="text-sm font-medium text-gray-500">
                                            ที่นั่ง
                                        </dt>
                                        {source_info.seat_number}
                                    </div>
                                   

                                </dl>
                            </div>

                        </div>
                    </div>
                </div>
            </div>

            <div className='flex justify-center mt-20'>

                    <button onClick={backToPreviousPage} type="button" className="text-white bg-gradient-to-r from-gray-400 via-gray-500 to-gray-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-gray-300 dark:focus:ring-gray-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg mt-5">
                        กลับไปเลือกที่นั่ง
                    </button>
                
                <Link to="/ticket"><button type="button" className="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg mt-5">
                    กำหนดการเดินทาง
                </button></Link>
            </div>
        </div>
    );
};

export default Inputfill;
