import React from 'react';
import Navbar from '../component/navbar';
import { Link } from 'react-router-dom';

const Inputfill = () => {
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

                                        <select id="countries" className="col-start-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                            <option selected>บัตรประชาชน</option>
                                            <option value="US">United States</option>
                                            <option value="CA">Canada</option>
                                            <option value="FR">France</option>
                                            <option value="DE">Germany</option>
                                        </select>
                                        <input class="col-start-3 col-end-5 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="หมายเลขบัตร" />

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
                                        <div className='text-center'>(2 x 572.00)</div>
                                        <div className='text-end'>1,144.00 (บาท) </div>


                                        <dt class="text-sm font-medium text-gray-500">
                                            ค่าดำเนินการจัดการ
                                        </dt>
                                        <div className='text-center'>(2 x 20)</div>
                                        <div className='text-end'>40 (บาท) </div>

                                        <dt class="text-lg font-medium text-gray-500">
                                            <b> ราคารวม</b>
                                        </dt>
                                        <div className='text-lg col-start-2 col-end-4 text-end '><b> 1,184.00 (บาท) </b></div>

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
                                        <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
                                            <dt class="text-sm font-medium text-gray-500">
                                                ผู้ให้บริการ
                                            </dt>
                                            010101
                                        </div>
                                        <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
                                            <dt class="text-sm font-medium text-gray-500">
                                                เส้นทาง
                                            </dt>
                                            010101
                                        </div>
                                        <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
                                            <dt class="text-sm font-medium text-gray-500">
                                                รถออกจาก
                                            </dt>
                                            010101
                                        </div>
                                        <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
                                            <dt class="text-sm font-medium text-gray-500">
                                                จุดขึ้นรถ
                                            </dt>
                                            010101
                                        </div>
                                        <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
                                            <dt class="text-sm font-medium text-gray-500">
                                                ถึง
                                            </dt>
                                            010101
                                        </div>
                                        <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
                                            <dt class="text-sm font-medium text-gray-500">
                                                จุดลงรถ
                                            </dt>
                                            010101
                                        </div>
                                        <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
                                            <dt class="text-sm font-medium text-gray-500">
                                                รถออกวัน
                                            </dt>
                                            010101
                                        </div>
                                        <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
                                            <dt class="text-sm font-medium text-gray-500">
                                                เวลาต้นทาง
                                            </dt>
                                            010101
                                        </div>
                                        <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
                                            <dt class="text-sm font-medium text-gray-500">
                                                มาตรฐาน
                                            </dt>
                                            010101
                                        </div>

                                    </dl>
                            </div>
                            
                        </div>
                    </div>
                </div>
            </div>

            <div className='flex justify-center mt-20'>
                <Link to="/seat">
                    <button type="button" className="text-white bg-gradient-to-r from-gray-400 via-gray-500 to-gray-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-gray-300 dark:focus:ring-gray-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg mt-5">
                        กลับไปเลือกที่นั่ง
                    </button>
                </Link>
                <Link to="/ticket"><button type="button" className="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg mt-5">
                    กำหนดการเดินทาง
                </button></Link>
            </div>
        </div>
    );
};

export default Inputfill;

// import React from 'react';
// import Navbar from '../component/navbar';
// import { Link } from 'react-router-dom';

// const Inputfill = () => {
//     return (
//         <div>

//             <Navbar />
//             <div className="max-w-screen-2xl mx-auto xl:w-10/12 lg: w-10/12">
//                 <div className='flex justify-between'>
//                     <div className='mt-5 text-2xl mb-8'>
//                         ผู้โดยสารและชำระเงิน
//                     </div>
//                     <div className='mt-5'>
//                         <div className='flex '>
//                             <div className='text-gray-400'>ค้นหาเที่ยวรถ</div>
//                             <div className=' mx-2'>--</div>
//                             <div className='text-gray-400'>เลือกเที่ยวรถ</div>
//                             <div className=' mx-2'>--</div>
//                             <div className='text-gray-400'>เลือกที่นั่ง</div>
//                             <div className=' mx-2'>--</div>
//                             <div className='text-pink-400'>ผู้โดยสารและชำระเงิน</div>
//                             <div className=' mx-2'>--</div>
//                             <div className='text-gray-400'>กำหนดการเดินทาง</div>
//                         </div>

//                     </div>
//                 </div>


//                 <div class="grid grid-flow-row-dense grid-cols-3 grid-rows-3">
//                     <div class="col-span-2">
//                         <div class="bg-white max-w-full shadow overflow-hidden sm:rounded-lg">
//                             <div class="px-4 py-5 sm:px-6">
//                                 <h3 class="text-lg leading-6 font-medium text-gray-900 ">
//                                     ข้อมูลผู้โดยสารที่เดินทาง

//                                 </h3>
//                             </div>
//                             <div class="border-t border-gray-200 ">
//                                 <dl>
//                                     <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
//                                         <dt class="text-sm font-medium text-gray-500">
//                                             ที่นั่ง
//                                         </dt>
//                                         <select id="countries" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
//                                             <option selected>ระบุเพศ</option>
//                                             <option value="US">United States</option>
//                                             <option value="CA">Canada</option>
//                                             <option value="FR">France</option>
//                                             <option value="DE">Germany</option>
//                                         </select>
//                                         <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="ชื่อ" />
//                                         <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="นามสกุล" />

//                                         <select id="countries" className="col-start-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
//                                             <option selected>บัตรประชาชน</option>
//                                             <option value="US">United States</option>
//                                             <option value="CA">Canada</option>
//                                             <option value="FR">France</option>
//                                             <option value="DE">Germany</option>
//                                         </select>
//                                         <input class="col-start-3 col-end-5 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="หมายเลขบัตร" />

//                                     </div>


//                                 </dl>
//                             </div>
//                         </div>

//                         <div class="mt-7 bg-white max-w-full shadow overflow-hidden sm:rounded-lg">
//                             <div class="px-4 py-5 sm:px-6">
//                                 <h3 class="text-lg leading-6 font-medium text-gray-900 ">
//                                     ข้อมูลผู้ติดต่อ

//                                 </h3>
//                             </div>
//                             <div class="border-t border-gray-200 ">
//                                 <dl>
//                                     <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
//                                         <dt class="text-sm font-medium text-gray-500">
//                                             ข้อมูลผู้ติดต่อ
//                                         </dt>

//                                         <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="ชื่อ" />
//                                         <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="นามสกุล" />
//                                         <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="โทรศัพทร์มือถือ" />
//                                         <dt class="text-sm font-medium text-gray-500">
//                                             อีเมล
//                                         </dt>

//                                         <input class="col-start-2 col-end-5 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="กรอกอีเมล เพื่อรับข้อมูลการจอง" />




//                                     </div>


//                                 </dl>
//                             </div>

//                         </div>
//                         <div class="mt-7 bg-white max-w-full shadow overflow-hidden sm:rounded-lg">
//                             <div class="px-4 py-5 sm:px-6">
//                                 <h3 class="text-lg leading-6 font-medium text-gray-900 ">
//                                     ยอดเงินรวมที่ต้องชำระ


//                                 </h3>
//                             </div>
//                             <div class="border-t border-gray-200 ">
//                                 <dl>
//                                     <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
//                                         <dt class="text-sm font-medium text-gray-500">
//                                             ราคาตั๋ว
//                                         </dt>
//                                         <div className='text-center'>(2 x 572.00)</div>
//                                         <div className='text-end'>1,144.00 (บาท) </div>


//                                         <dt class="text-sm font-medium text-gray-500">
//                                             ค่าดำเนินการจัดการ
//                                         </dt>
//                                         <div className='text-center'>(2 x 20)</div>
//                                         <div className='text-end'>40 (บาท) </div>

//                                         <dt class="text-lg font-medium text-gray-500">
//                                             <b> ราคารวม</b>
//                                         </dt>
//                                         <div className='text-lg col-start-2 col-end-4 text-end '><b> 1,184.00 (บาท) </b></div>

//                                     </div>


//                                 </dl>
//                             </div>

//                         </div>
//                         <div class="mt-7 bg-white max-w-full shadow overflow-hidden sm:rounded-lg">
//                             <div class="px-4 py-5 sm:px-6">
//                                 <h3 class="text-lg leading-6 font-medium text-gray-900 ">
//                                     ยอดเงินรวมที่ต้องชำระ


//                                 </h3>
//                             </div>
//                             <div class="border-t border-gray-200 ">
//                                 <dl>
//                                     <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
//                                         <dt class="text-sm font-medium text-gray-500">
//                                             ราคาตั๋ว
//                                         </dt>
//                                         <div className='text-center'>(2 x 572.00)</div>
//                                         <div className='text-end'>1,144.00 (บาท) </div>


//                                         <dt class="text-sm font-medium text-gray-500">
//                                             ค่าดำเนินการจัดการ
//                                         </dt>
//                                         <div className='text-center'>(2 x 20)</div>
//                                         <div className='text-end'>40 (บาท) </div>

//                                         <dt class="text-lg font-medium text-gray-500">
//                                             <b> ราคารวม</b>
//                                         </dt>
//                                         <div className='text-lg col-start-2 col-end-4 text-end '><b> 1,184.00 (บาท) </b></div>

//                                     </div>


//                                 </dl>
//                             </div>

//                         </div>
//                     </div>

//                     <div class="ms-5 bg-white max-w-full  shadow overflow-hidden sm:rounded-lg">
//                         <div class="px-4 py-5 sm:px-6">
//                             <h3 class="text-lg leading-6 font-medium text-gray-900 ">
//                                 ข้อมูลการเดินทาง

//                             </h3>
//                         </div>
//                         <div class="border-t border-gray-200 ">
//                             <dl>
//                                 <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
//                                     <dt class="text-sm font-medium text-gray-500">
//                                         ผู้ให้บริการ
//                                     </dt>
//                                     010101
//                                 </div>
//                                 <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
//                                     <dt class="text-sm font-medium text-gray-500">
//                                         เส้นทาง
//                                     </dt>
//                                     010101
//                                 </div>
//                                 <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
//                                     <dt class="text-sm font-medium text-gray-500">
//                                         รถออกจาก
//                                     </dt>
//                                     010101
//                                 </div>
//                                 <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
//                                     <dt class="text-sm font-medium text-gray-500">
//                                         จุดขึ้นรถ
//                                     </dt>
//                                     010101
//                                 </div>
//                                 <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
//                                     <dt class="text-sm font-medium text-gray-500">
//                                         ถึง
//                                     </dt>
//                                     010101
//                                 </div>
//                                 <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
//                                     <dt class="text-sm font-medium text-gray-500">
//                                         จุดลงรถ
//                                     </dt>
//                                     010101
//                                 </div>
//                                 <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
//                                     <dt class="text-sm font-medium text-gray-500">
//                                         รถออกวัน
//                                     </dt>
//                                     010101
//                                 </div>
//                                 <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
//                                     <dt class="text-sm font-medium text-gray-500">
//                                         เวลาต้นทาง
//                                     </dt>
//                                     010101
//                                 </div>
//                                 <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-4 sm:gap-4 sm:px-6">
//                                     <dt class="text-sm font-medium text-gray-500">
//                                         มาตรฐาน
//                                     </dt>
//                                     010101
//                                 </div>

//                             </dl>
//                         </div>
//                     </div>
//                  </div>
//             </div>

//             <div className='flex justify-center mt-20'>
//                 <Link to="/"><button type="button" class="text-white bg-gradient-to-r from-gray-400 via-gray-500 to-gray-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-gray-300 dark:focus:ring-gray-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2   text-lg mt-5">กลับไปค้นหาเที่ยวรถ</button></Link>

//                 <button type="button" class="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 text-lg mt-5">ดำเนินการต่อ</button>
//             </div>
//         </div>


//     );
// };

// export default Inputfill;
