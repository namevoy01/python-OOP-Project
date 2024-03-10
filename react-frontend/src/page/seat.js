import React from 'react';
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';

const seat = () => {
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
                        <div className="grid grid-cols-4 gap-4">
                            <div className="col-start-1 col-end-5">
                                <b> เลือกที่นั่ง</b>
                            </div>

                            <div>
                                ที่นั่งที่ 1
                                <form className=" flex">
                                    <select id="countries" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                        <option selected>กรุณาเลือก</option>
                                        <option value="US">United States</option>
                                        <option value="CA">Canada</option>
                                        <option value="FR">France</option>
                                        <option value="DE">Germany</option>
                                    </select>                                </form>
                            </div>
                            <div>
                                ที่นั่งที่ 2
                                <form className=" flex">
                                    <select id="countries" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                        <option selected>กรุณาเลือก</option>
                                        <option value="US">United States</option>
                                        <option value="CA">Canada</option>
                                        <option value="FR">France</option>
                                        <option value="DE">Germany</option>
                                    </select>
                                </form>
                            </div>
                            <div>
                                ที่นั่งที่ 3
                                <form className=" flex">
                                    <select id="countries" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                        <option selected>กรุณาเลือก</option>
                                        <option value="US">United States</option>
                                        <option value="CA">Canada</option>
                                        <option value="FR">France</option>
                                        <option value="DE">Germany</option>
                                    </select>
                                </form>
                            </div>
                            <div>
                                ที่นั่งที่ 4
                                <form className=" flex">
                                    <select id="countries" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                        <option selected>กรุณาเลือก</option>
                                        <option value="US">United States</option>
                                        <option value="CA">Canada</option>
                                        <option value="FR">France</option>
                                        <option value="DE">Germany</option>
                                    </select>
                                </form>
                            </div>

                        </div>

                    </div>
                    <div className='flex justify-center'>
                        <Link to="/travel"><button type="button" class="text-white bg-gradient-to-r from-gray-400 via-gray-500 to-gray-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-gray-300 dark:focus:ring-gray-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2   text-lg mt-5">กลับไปเลือกเที่ยวรถ</button></Link>
                        <Link to="/inputfill"><button type="button" className="mt-5 text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg">ชำระเงิน</button></Link>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default seat;
