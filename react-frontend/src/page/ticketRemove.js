import React, { useState } from 'react';
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';

function useTicketRemove() {
    const [showModal, setShowModal] = useState(false);



    return (
        <div>
            {/* <p>จังหวัดที่เลือก: {selectedProvince}</p>
            <p>{selectedStation}</p> */}

            <div >
                <Navbar />
                <div className="max-w-screen-2xl mx-auto xl:w-10/12 lg: w-10/12">

                    <div className='flex justify-between'>
                        <div className='mt-5 text-2xl mb-8'>
                            ยกเลิกตั๋ว
                        </div>
                        <div className='mt-5 '>
                            <div className='flex '>
                            <Link to='/'> <div className='text-pink-400'>กลับหน้าแรก</div></Link>
                            </div>
                        </div>
                    </div>
                    <div className='flex justify-center mt-5'>
                        <input class=" shadow appearance-none border rounded w-6/12 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="ใส่หมายเลขตั๋ว" />
                        <button onClick={() => setShowModal(true)} type="button" className="ms-3 text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2  text-lg ">
                            ยกเลิกตั๋ว
                        </button>
                    </div>
                </div>

            </div>
            {showModal ? (
                <>
                    <div className="fixed inset-0 z-10 overflow-y-auto">
                        <div
                            className="fixed inset-0 w-full h-full bg-black opacity-40"
                            onClick={() => setShowModal(false)}
                        ></div>
                        <div className="flex items-center min-h-screen px-4 py-8">
                            <div className="relative w-full max-w-lg p-4 mx-auto bg-white rounded-md shadow-lg">
                                <div className="mt-3 sm:flex">
                                    <div className="mt-2 text-center sm:ml-4 sm:text-left">
                                        <h4 className="text-lg font-medium text-gray-800">
                                            กรุณาใส่ข้อมูล
                                        </h4>
                                        <p className="mt-2 text-[15px] leading-relaxed text-gray-500">
                                            เลขบัญชี :

                                        </p>
                                        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="กรุณาใส่เลขบัญชี" />
                                        <p className="mt-7 text-[15px]  text-gray-500">
                                            การยกเลิกตั๋วจะหักค่าธรรมเนียมการคืนตั๋ว 10% จากอัตราค่าโดยสาร และ คิดค่าธรรมเนียมการโอนเงิน 30 บาท/ครั้ง
                                        </p>
                                        <div className="items-center gap-2 mt-3 sm:flex">
                                            <button
                                                className="w-full mt-2 p-2.5 flex-1 text-white bg-green-600 rounded-md outline-none ring-offset-2 ring-green-600 focus:ring-2"
                                                onClick={() =>
                                                    setShowModal(false)   
                                                }
                                                
                                            >
                                                ยืนยัน
                                            </button>
                                            <button
                                                className="w-full mt-2 p-2.5 flex-1 text-gray-800 rounded-md outline-none border ring-offset-2 ring-indigo-600 focus:ring-2"
                                                onClick={() =>
                                                    setShowModal(false)
                                                }
                                            >
                                                Cancel
                                            </button>
                                        </div>
                                    </div>
                                    {/* <div className="mt-2 text-center sm:ml-4 sm:text-left">
                                        <h4 className="text-lg font-medium text-gray-800">
                                            กรุณาใส่ข้อมูล
                                        </h4>
                                        <p className="mt-2 text-[15px] leading-relaxed text-gray-500">
                                            เลขบัญชี :

                                        </p>
                                        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="กรุณาใส่เลขบัญชี" />

                                        <div className="items-center gap-2 mt-3 sm:flex">
                                            <button
                                                className="w-full mt-2 p-2.5 flex-1 text-white bg-red-600 rounded-md outline-none ring-offset-2 ring-red-600 focus:ring-2"
                                                onClick={() =>
                                                    setShowModal(false)
                                                }
                                            >
                                                ยืนยัน
                                            </button>
                                            <button
                                                className="w-full mt-2 p-2.5 flex-1 text-gray-800 rounded-md outline-none border ring-offset-2 ring-indigo-600 focus:ring-2"
                                                onClick={() =>
                                                    setShowModal(false)
                                                }
                                            >
                                                Cancel
                                            </button>
                                        </div>
                                    </div> */}
                                </div>
                            </div>
                        </div>
                    </div>
                </>
            ) : null}

        </div>
    );
}

export default useTicketRemove;
