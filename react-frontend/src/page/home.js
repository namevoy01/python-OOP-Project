import React, { useState, useEffect } from 'react';
import Date from '../component/date';
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';
// import { withRouter } from 'react-router-dom';

function Home() {

    // function goBack() {
    //     // window.history.go(-1);
    //     // console.log('ควย');
    // };

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
                    setSourceStation('');
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

    const [selectedDestination, setSelectedDestination] = useState('');
    const [source_destination, set_source_destination] = useState([]);
    useEffect(() => {
        const fetchData = async () => {
            if (selectedStation) {
                try {
                    setSelectedDestination('');
                    const response = await fetch(`http://127.0.0.1:8000/api/destination_province?source_province=${encodeURIComponent(selectedProvince)}&source_station=${encodeURIComponent(selectedStation)}`);
                    const data = await response.json();
                    set_source_destination(data);
                } catch (error) {
                    console.error('Error fetching source stations:', error);
                }
            }
        };

        fetchData();
    }, [selectedStation, selectedProvince]); // Include selectedProvince in the dependency array




    const [selectedDestinationStation, setSelectedDestinationStation] = useState('');
    const [source_destination_station, set_source_destination_station] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            if (selectedDestination) {
                try {
                    setSelectedDestinationStation('');
                    const response = await fetch(`http://127.0.0.1:8000/api/destination_station?source_province=${encodeURIComponent(selectedProvince)}&source_station=${encodeURIComponent(selectedStation)}&destination_province=${encodeURIComponent(selectedDestination)}`);
                    const data = await response.json();
                    set_source_destination_station(data);
                } catch (error) {
                    console.error('Error fetching destination stations:', error);
                }
            }
        };

        fetchData();
    }, [selectedStation, selectedProvince, selectedDestination]);


    const handleProvinceChange = (event) => {
        const selectedValue = event.target.value;
        setSelectedProvince(selectedValue);

    };

    const handleStationChange = (event) => {
        const selectedStation = event.target.value;
        setSourceStation(selectedStation);

    };

    const handleDestinationChange = (event) => {
        const selectedDestination = event.target.value;
        setSelectedDestination(selectedDestination);

    };

    const handleDestinationStation = (event) => {
        const selectedDestinationStation = event.target.value;
        setSelectedDestinationStation(selectedDestinationStation);

    };

    const [selectedDateFromDatePicker, setSelectedDateFromDatePicker] = useState(null);

    const handleDatePickerChange = (date) => {
        setSelectedDateFromDatePicker(date);
    };
    return (
        <div>
            {/* <button onClick={goBack}>Go Back</button> */}

            {/* <select id="station" onChange={handleDestinationStation} value={selectedDestinationStation} className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option selected>เลือกจุดขึ้นรถ</option>
                {source_destination_station.map((destination_station, index) => (
                    <option key={index} value={destination_station}>{destination_station}</option>
                ))}
            </select> */}

            {/* <p>จังหวัดที่เลือก: {selectedDestinationStation}</p> */}

            {/* {source_destination_station.map((destination_station, index) => (
                <option key={index} value={destination_station}>{destination_station}</option>
            ))} */}

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
                                    <option id='source_station'>เลือกจังหวัดต้นทาง</option>
                                    {source_province.map((province, index) => (
                                        <option key={index} value={province}>{province}</option>
                                    ))}

                                </select>
                            </form>
                        </div>
                        <div>
                            จุดขึ้นรถ
                            <form className="mt-3">
                                <select id="station"
                                    value={selectedStation}
                                    onChange={handleStationChange}
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option id='source_station'>เลือกจังหวัดต้นทาง</option>
                                    {source_station.map((station, index) => (
                                        <option key={index} value={station}>{station}</option>
                                    ))}
                                </select>
                            </form>

                        </div>
                        <div className='mt-5'>
                            จังหวัดปลายทาง
                            <form className="mt-3">
                                <select id="Destination"
                                    value={selectedDestination}
                                    onChange={handleDestinationChange}
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option id='source_destination'>เลือกจังหวัดต้นทาง</option>
                                    {source_destination.map((destination, index) => (
                                        <option key={index} value={destination}>{destination}</option>
                                    ))}
                                </select>
                            </form>
                        </div>

                        <div className='mt-5'>
                            จุดลงรถ
                            <form className="mt-3">
                                <select id="station"
                                    value={selectedDestinationStation}
                                    onChange={handleDestinationStation}
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option id='source_destination_station'>เลือกจังหวัดต้นทาง</option>
                                    {source_destination_station.map((destination_station, index) => (
                                        <option key={index} value={destination_station}>{destination_station}</option>
                                    ))}
                                </select>
                            </form>
                        </div>

                        <div className='mt-5'>
                            วันเดินทางไป
                            <Date onDateChange={handleDatePickerChange} />
                        </div>
                    </div>
                    {selectedProvince === 'เลือกจังหวัดต้นทาง' || selectedProvince === '' || selectedStation === '' || selectedStation === 'เลือกจุดขึ้นรถ' || selectedDestination === '' || selectedDestination === 'เลือกจังหวัดปลายทาง' || selectedDestinationStation === '' || selectedDestinationStation === 'เลือกจังหวัดปลายทาง' || selectedDateFromDatePicker === null ? (
                        <div className='flex justify-center'>

                            <button
                                type="button"
                                className="text -white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg disabled:opacity-50 disabled:cursor-not-allowed"
                                disabled
                            >
                                ค้นหาเที่ยวรถ
                            </button>

                        </div>
                    )
                        : (
                            <div className='flex justify-center'>
                                <Link to="/travel"><button type="button" className="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg">ค้นหาเที่ยวรถ</button></Link>
                            </div>
                        )}

                </div>

            </div>


        </div>
    );
}

export default Home;
