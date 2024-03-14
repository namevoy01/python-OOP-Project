// src/components/404Error.js
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';
import Login from './login';
import React, { useEffect } from 'react';

const Admin = () => {
    const storedUserData = JSON.parse(localStorage.getItem('userData'));
   
    console.log(storedUserData);
    const handleLogout = () => {
        localStorage.removeItem('userData');
        // ทำการออกจากหน้า admin หรือทำการ redirect ไปยังหน้าอื่นตามต้องการ
    };
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
                                Admin
                            </div>
                           
                        </div>


                        <div class="relative overflow-y-auto h-80">
                            <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 ">
                                <thead class="text-xs text-gray-700 uppercase bg-pink-100 dark:bg-gray-700 dark:text-gray-400 ">
                                    <tr className='text-lg'>
                                        <th scope="col" class="px-6 py-3">
                                            ทะเบียนรถยนต์
                                        </th>
                                        <th scope="col" class="px-6 py-3">
                                            ที่นั่งทั้งหมด
                                        </th>


                                        <th scope="col" class="px-6 py-3 text-center">
                                            เลือก
                                        </th>
                                    </tr>
                                </thead>
                                <tbody className=''>
                                    <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                            กก 999
                                        </th>
                                        <td class="px-6 py-4">
                                            ที่นั่งทั้งหมด
                                        </td>

                                        <td class=" py-4 flex justify-center">
                                            <button type="button" className="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center text-lg">รายละเอียด</button>
                                        </td>
                                    </tr>

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
