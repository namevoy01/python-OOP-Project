import React, { useState, useEffect } from 'react';
import Date from '../component/date';
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';

function Home() {

    const [selectedProvince, setSelectedProvince] = useState('');
    const [source_province, set_source_province] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/source_province')
            .then(response => response.json())
            .then(source_province => set_source_province(source_province))
            .catch(error => console.error('Error fetching source provinces:', error));
    }, []);

    const [selectedStation, setSourceStation] = useState('');
    const [source_station, set_source_station] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            if (selectedProvince) {
                try {
                    const response = await fetch(`http://127.0.0.1:8000/api/source_station?source_province=${encodeURIComponent(selectedProvince)}`);
                    const data = await response.json();
                    set_source_station(data);
                } catch (error) {
                    console.error('Error fetching source stations:', error);
                }
            }
        };

        fetchData();
    }, [selectedProvince]);


    const handleProvinceChange = (event) => {
        const selectedValue = event.target.value;
        setSelectedProvince(selectedValue);
        // เพิ่มโค้ดอื่น ๆ ที่คุณต้องการทำเมื่อมีการเลือกจังหวัด
    };

    const handleStationChange = (event) => {
        const selectedStation = event.target.value;
        setSourceStation(selectedStation);

        // เพิ่มโค้ดอื่น ๆ ที่คุณต้องการทำเมื่อมีการเลือกจังหวัด
        // เช่น การดึงข้อมูลจาก API หรือปรับแต่งการแสดงผล
    };

    return (
        <div>
            {/* <p>จังหวัดที่เลือก: {selectedProvince}</p>
            <p>{selectedStation}</p> */}

            <Navbar />
            <div className="max-w-screen-2xl mx-auto xl:w-10/12 lg: w-10/12">
                <div className='flex justify-between'>
                    <div className='mt-5 text-2xl mb-8'>
                        ค้นหาเที่ยวรถ
                    </div>
                    <div className='mt-5 '>
                        <div className='flex '>
                            <div className='text-pink-400'>ค้นหาเที่ยวรถ</div>
                            <div className=' mx-2'>--</div>
                            <div className='text-gray-400'>เลือกเที่ยวรถ</div>
                            <div className=' mx-2'>--</div>
                            <div className='text-gray-400'>เลือกที่นั่ง</div>
                            <div className=' mx-2'>--</div>
                            <div className='text-gray-400'>ผู้โดยสารและชำระเงิน</div>
                            <div className=' mx-2'>--</div>
                            <div className='text-gray-400'>กำหนดการเดินทาง</div>
                        </div>
                    </div>
                </div>
                <div className="py-8 px-8 bg-white rounded-xl border-solid border-2 border-gray-100 shadow-md  space-y-2 mt-5">
                    <div className="grid grid-cols-2 gap-4">
                        <div className=''>
                            จังหวัดต้นทาง
                            <form className="mt-3">
                                <select id="Province"
                                    value={selectedProvince}
                                    onChange={handleProvinceChange}
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option id='source_province'>เลือกจังหวัดต้นทาง</option>
                                    {source_province.map((province, index) => (
                                        <option key={index} value={province}>{province}</option>
                                    ))}

                                </select>
                            </form>
                        </div>
                        <div>
                            จุดขึ้นรถ
                            <form className="mt-3">
                                <select id="station" onChange={handleStationChange} value={selectedStation} className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option selected>เลือกจุดขึ้นรถ</option>
                                    {source_station.map((station, index) => (
                                        <option key={index} value={station}>{station}</option>
                                    ))}
                                </select>
                            </form>

                        </div>
                        <div className='mt-5'>
                            จังหวัดปลายทาง
                            <form className="mt-3">
                                <select id="countries" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option selected>Choose a country</option>
                                    <option value="US">United States</option>
                                    <option value="CA">Canada</option>
                                    <option value="FR">France</option>
                                    <option value="DE">Germany</option>
                                </select>
                            </form>
                        </div>

                        <div className='mt-5'>
                            จุดลงรถ
                            <form className="mt-3">
                                <select id="countries" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option selected>Choose a country</option>
                                    <option value="US">United States</option>
                                    <option value="CA">Canada</option>
                                    <option value="FR">France</option>
                                    <option value="DE">Germany</option>
                                </select>
                            </form>
                        </div>

                        <div className='mt-5'>
                            วันเดินทางไป
                            <Date />
                        </div>
                    </div>
                    <div className='flex justify-center'>
                        <Link to="/travel"><button type="button" className="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg">ค้นหาเที่ยวรถ</button></Link>
                    </div>
                </div>

            </div>
           

        </div>
    );
}

export default Home;
