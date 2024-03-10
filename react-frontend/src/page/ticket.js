import React from 'react';
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';

const ticket = () => {
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
                        <div className="grid grid-cols-2 gap-4">
                            <div className="col-start-1 col-end-3">
                                <b> รหัสตั๋ว : 1150</b>
                            </div>

                            <div>
                                <form className="mt-3 flex">
                                    <div className='mt-1.5 me-2'> จาก</div>
                                    <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" value='10/3/2024 09:00 จังหวัด:กรุงเทพ จุดขึ้น:หมอชิต' disabled />
                                </form>
                            </div>
                            <div>
                                <form className="mt-3 flex">
                                    <div className='mt-1.5 me-3'>ไป</div>
                                    <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" value='จังหวัด:กระบี่ จุดลง:จุดจอดอำเภอลำทับ' disabled />

                                </form>

                            </div>
                            <div>
                                <form className="mt-3 flex">
                                    <div className='mt-1.5 me-3'>นาย สมชาย สองมือ</div>

                                </form>

                            </div>
                            <div>
                                <form className="mt-3 flex">
                                    <div className='mt-1.5 me-3'>สถานะ:
                                        <span class="ms-2 inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">Paid</span>

                                    </div>

                                </form>

                            </div>
                            <div className=" col-start-1  mt-3 col-end-3">
                                <b><div className='mt-1.5 me-3'>รายละเอียดข้อมูลติดต่อ:
                                </div></b>
                            </div>
                            <div className="mt-4">
                                เบอร์โทร: 099-999-9999 
                            </div>
                            <div className="mt-4">
                                อีเมล: 123@gmail.com 
                            </div>
                        </div>
                        <div className='flex justify-center'>
                            <Link to="/"><button type="button" className="mt-5 text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg">กลับหน้าแรก</button></Link>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    );
};

export default ticket;
