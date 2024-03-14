// src/components/404Error.js
import Navbar from '../component/navbar';
import Login from './login';
import React, { useState, useEffect } from 'react';

const Admin = () => {
    const storedUserData = JSON.parse(localStorage.getItem('userData'));




    const [source_route, set_route] = useState([]);
    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/schedule')
            .then(response => response.json())
            .then(source_route => set_route(source_route))
            .catch(error => console.error('Error fetching source provinces:', error));
    }, []);

    console.log(source_route);

    return (

        <div>
            {storedUserData == null ? (
                <Login />
            ) : (
                <div>

                    <Navbar />
                    <div className="max-w-screen-2xl mx-auto xl:w-10/12 lg: w-10/12">
                        <div className='flex justify-between'>
                            <div className='mt-5 text-2xl mb-8'>
                                รายละเอียดเส้นทางทั้งหมด
                            </div>

                        </div>


                        <div class="relative overflow-y-auto h-80">
                            <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 ">
                                <thead class="text-xs text-gray-700 uppercase bg-pink-100 dark:bg-gray-700 dark:text-gray-400 ">
                                    <tr className='text-lg'>
                                        <th scope="col" class="px-6 py-3">
                                            ID
                                        </th>
                                        <th scope="col" class="px-6 py-3">
                                            ทะเบียนรถ
                                        </th>
                                        <th scope="col" class="px-6 py-3">
                                            จังหวัดต้นทาง
                                        </th>
                                        <th scope="col" class="px-6 py-3">
                                            จังหวัดปลายทาง
                                        </th>
                                        <th scope="col" class="px-6 py-3">
                                            เวลารถออก
                                        </th>
                                    </tr>
                                </thead>
                                <tbody className=''>
                                    {source_route.map((route) => (
                                        <tr key={route.id} className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                                            <td scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                                {route.id}
                                            </td>
                                            <td className="px-6 py-4">
                                                {route.bus_license}
                                            </td>
                                            <td className="px-6 py-4">
                                                {route.source_province}
                                            </td>
                                            <td className="px-6 py-4">
                                                {route.destination_province}
                                            </td>
                                            <td className="px-6 py-4">
                                                {route.departure_time}
                                            </td>
                                        </tr>
                                    ))}





                                </tbody>
                            </table>
                        </div>

                    </div>

                </div>
            )}


        </div>
    );
};

export default Admin;
