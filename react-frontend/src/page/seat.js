import React, { useState, useEffect } from 'react';
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';
import { useParams } from 'react-router-dom';

const useSeatSelect = () => {
    const { bus_license } = useParams();
    console.log(bus_license);

    const [busLicenseData, setBusLicenseData] = useState([]);

    const [selectedSeat, setSelectedSeat] = useState(null);

    useEffect(() => {
        const fetchBusLicenseData = async () => {
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/seat?bus_license=${encodeURIComponent(bus_license)}`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                setBusLicenseData(data);
            } catch (error) {
                console.error('Error fetching bus license data:', error);
            }
        };

        fetchBusLicenseData();
    }, []);
    console.log(selectedSeat);
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
                                <div className='text-pink-400'>เลือกที่นั่ง</div>
                                <div className='mx-2'>--</div>
                                <div className='text-gray-400'>ผู้โดยสารและชำระเงิน</div>
                                <div className='mx-2'>--</div>
                                <div className='text-gray-400'>กำหนดการเดินทาง</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="max-w-screen-2xl mx-auto xl:w-10/12 lg: w-10/12">

                    <div className="py-8 px-8 bg-white rounded-xl border-solid border-2 border-gray-100 shadow-md  space-y-2 mt-5">
                        <div >
                            <b> เลือกที่นั่ง</b>
                        </div>
                        <div className='flex justify-center'>
                            <div className='flex justify-center w-4/12'>
                                <div className="flex flex-wrap justify-center gap-4 ">



                                    {busLicenseData.map(seat => (
                                        seat.status_seat ? (
                                            <div key={seat.id} className="relative flex items-start py-4 ml-2 flex-shrink-0">
                                                <input
                                                    id={`seat_${seat.id}`}
                                                    type="radio"
                                                    className={`hidden peer preferred-seat ${seat.status_seat ? '' : 'opacity-50 cursor-not-allowed'}`}
                                                    name="preferred_seat"
                                                    onChange={() => setSelectedSeat(seat.seat_number)}
                                                    value={seat.seat_number}
                                                />
                                                <label htmlFor={`seat_${seat.id}`} className={`inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer ${seat.status_seat ? 'bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2' : 'bg-red-500 text-white border-red-500 peer-checked:border-red-400 peer-checked:bg-red-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2'}`}>
                                                    <div className="text-sm text-brand-black m-3">{seat.seat_number}</div>
                                                </label>
                                            </div>
                                        ) : (
                                            <div key={seat.id} className="relative flex items-start py-4 ml-2 flex-shrink-0">
                                                <input
                                                    id={`seat_${seat.id}`}
                                                    type="radio"
                                                    className={`hidden peer preferred-seat ${seat.status_seat ? '' : 'opacity-50 cursor-not-allowed'}`}
                                                    name="preferred_seat"
                                                    value={seat.seat_number}
                                                    disabled
                                                />
                                                <label htmlFor={`seat_${seat.id}`} className={`inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer ${seat.status_seat ? 'bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2' : 'bg-red-500 text-white border-red-500 peer-checked:border-red-400 peer-checked:bg-red-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2'}`}>
                                                    <div className="text-sm text-brand-black m-3">{seat.seat_number}</div>
                                                </label>
                                            </div>
                                        )
                                    ))}
                                </div>
                            </div>
                        </div>

                    </div>

                    <div className='flex justify-center'>
                        <Link to="/travel"><button type="button" className="text-white bg-gradient-to-r from-gray-400 via-gray-500 to-gray-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-gray-300 dark:focus:ring-gray-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2   text-lg mt-5">กลับไปเลือกเที่ยวรถ</button></Link>
                        
                        {selectedSeat !== null ? (
                            <Link to='/inputfill'>
                                <button
                                    type="button"
                                    className="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg mt-5"
                                >
                                    ชำระเงิน
                                </button>
                            </Link>
                        ) : (
                            <button
                                type="button"
                                className="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg mt-5 disabled:opacity-50 disabled:cursor-not-allowed"
                                disabled>
                                ชำระเงิน
                            </button>
                        )}                    </div>


                </div>
            </div>
        </div>
    );
};

export default useSeatSelect;
