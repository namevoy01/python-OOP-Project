import React, { useState, useEffect } from 'react';
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { format, parse } from 'date-fns';

function Travel() {
    const { province, station, destination, destinationstation, date } = useParams();

    const parsedDate = parse(date, 'dd-MM-yyyy', new Date());
    const formattedDate = format(parsedDate, 'dd/MM/yyyy');


    const [selectedTripId, setSelectedTripId] = useState(null);
    const [selectedTime, setSelectedTime] = useState(null);
    const [selectedAmount, setSelectedAmount] = useState(null);

    const [data, setData] = useState([]);

    const backToPreviousPage = () => {
        window.history.length > 1 ? window.history.go(-1) : window.location.href = '/';
    };

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/trip?source_province=${encodeURIComponent(province)}&source_station=${encodeURIComponent(station)}&destination_province=${encodeURIComponent(destination)}&destination_station=${encodeURIComponent(destinationstation)}&departure_date=${encodeURIComponent(formattedDate)}`, {
                    method: 'GET', // หรือ 'POST' หรือวิธีที่ต้องการ
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const result = await response.json();
                setData(result);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    data.map(e => {
        console.log(e);
    })

    const handleRadioChange = (tripId) => {
        setSelectedTripId(tripId);
        const selectedTrip = data.find(trip => trip.id === tripId);
        setSelectedBusLicense(selectedTrip ? selectedTrip.bus_license : null);
        setSelectedTime(selectedTrip ? selectedTrip.departure_time : null);
        setSelectedAmount(selectedTrip ? selectedTrip.price : null);

        
    };

    const [selectedBusLicense, setSelectedBusLicense] = useState(null);

    console.log('ddddd', selectedBusLicense);
    console.log('ddddd', selectedTime);
    console.log('ddddd', selectedAmount);

    // `http://127.0.0.1:8000/api/trip?source_province=${encodeURIComponent(province)}&source_station=${encodeURIComponent(station)}&destination_province=${encodeURIComponent(destination)}&destination_station=${encodeURIComponent(destinationstation)}&departure_date=${encodeURIComponent(date)}`
    return (

        // http://127.0.0.1:8000/api/trip?source_province=กรุงเทพมหานคร&source_station=สถานีขนส่งผู้โดยสารกรุงเทพฯ (หมอชิต 2)&destination_province=กาญจนบุรี&destination_station=จุดจอด%20อ.สังขละบุรี&departure_date=22%2F11%2F2024`
        <div>

            <Navbar />
            <div className="max-w-screen-2xl mx-auto xl:w-10/12 lg: w-10/12">
                <div className='flex justify-between'>
                    <div className='mt-5 text-2xl mb-8'>
                        เลือกเที่ยวรถ
                    </div>
                    <div className='mt-5'>
                        <div className='flex '>
                            <div className='text-gray-400'>ค้นหาเที่ยวรถ</div>
                            <div className=' mx-2'>--</div>
                            <div className='text-pink-400'>เลือกเที่ยวรถ</div>
                            <div className=' mx-2'>--</div>
                            <div className='text-gray-400'>เลือกที่นั่ง</div>
                            <div className=' mx-2'>--</div>
                            <div className='text-gray-400'>ผู้โดยสารและชำระเงิน</div>
                            <div className=' mx-2'>--</div>
                            <div className='text-gray-400'>กำหนดการเดินทาง</div>
                        </div>

                    </div>
                </div>

                <div class="relative overflow-y-auto h-80">
                    <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 ">
                        <thead class="text-xs text-gray-700 uppercase bg-pink-100 dark:bg-gray-700 dark:text-gray-400 ">
                            <tr className='text-lg'>
                                <th scope="col" class="px-6 py-3">
                                    รถออกต้นทาง
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    เส้นทาง
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    ปลายทาง
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    ที่นั่งว่าง
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    ทะเบียนรถ
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    เวลา
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    ราคา
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    เลือก
                                </th>
                            </tr>
                        </thead>
                        <tbody className=''>
                            {data.map((trip) => (
                                <tr key={trip.id} className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                                    <td scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                        {trip.source_province}
                                    </td>
                                    <td className="px-6 py-4">
                                        {trip.source_province} - {trip.destination_province}
                                    </td>
                                    <td className="px-6 py-4">
                                        {trip.destination_province}
                                    </td>
                                    <td className="px-6 py-4">
                                        {trip.count_seat}
                                    </td>
                                    <td className="px-6 py-4">
                                        {trip.bus_license}
                                    </td>
                                    <td className="px-6 py-4">
                                        {trip.departure_time}
                                    </td>
                                    <td className="px-6 py-4">
                                        {trip.price}
                                    </td>
                                    <td className="px-6 py-4">
                                        <input
                                            id={`default-radio-${trip.id}`}
                                            onChange={() => handleRadioChange(trip.id)}
                                            checked={selectedTripId === trip.id}
                                            type="radio"
                                            value={trip.id}
                                            name="default-radio"
                                            className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                                        />
                                    </td>
                                </tr>
                            ))}




                        </tbody>
                    </table>
                </div>
                <div className='flex justify-center mt-20'>
                   <button type="button" onClick={backToPreviousPage} class="text-white bg-gradient-to-r from-gray-400 via-gray-500 to-gray-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-gray-300 dark:focus:ring-gray-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2   text-lg mt-5">กลับไปค้นหาเที่ยวรถ</button>
                    {selectedTripId !== null ? (
                        <Link to={`/seat/${selectedBusLicense}/${province}/${station}/${destination}/${destinationstation}/${date}/${selectedTime}/${selectedAmount}`}>
                            <button
                                type="button"
                                className="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg mt-5"
                            >
                                เลือกที่นั่ง
                            </button>
                        </Link>
                    ) : (
                        <button
                            type="button"
                            className="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg mt-5 disabled:opacity-50 disabled:cursor-not-allowed"
                            disabled>
                            เลือกที่นั่ง
                        </button>
                    )}

                </div>
            </div>

        </div>

    );
}

export default Travel;
