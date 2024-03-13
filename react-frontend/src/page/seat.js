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

                    {/* <div className="py-8 px-8 bg-white rounded-xl border-solid border-2 border-gray-100 shadow-md  space-y-2 mt-5">
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

                        <div class='max-w-md mx-auto flex justify-items-end'>
                            <div class="relative flex items-start py-4 ml-2 w-6/12">
                                <input id="1" type="checkbox" class="hidden peer" name="preferred_activities[]" value="1" />
                                <label for="1" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-brand-light text-brand-black border-violet-500 peer-checked:border-violet-400 peer-checked:bg-violet-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                    <div class="flex items-center justify-center w-full">
                                        <div class="text-sm text-brand-black">A01</div>
                                    </div>
                                </label>
                            </div>

                            <div class="relative flex items-start py-4 ml-2 w-6/12">
                                <input id="2" type="checkbox" class="hidden peer" name="preferred_activities[]" value="2" />
                                <label for="2" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-brand-light text-brand-black border-violet-500 peer-checked:border-violet-400 peer-checked:bg-violet-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                    <div class="flex items-center justify-center w-full">
                                        <div class="text-sm text-brand-black">A02</div>
                                    </div>
                                </label>
                            </div>

                            <div class="relative flex items-start py-4 ml-2 w-6/12">
                                <input id="3" type="checkbox" class="hidden peer" name="preferred_activities[]" value="3" />
                                <label for="3" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-brand-light text-brand-black border-violet-500 peer-checked:border-violet-400 peer-checked:bg-violet-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                    <div class="flex items-center justify-center w-full">
                                        <div class="text-sm text-brand-black">A03</div>
                                    </div>
                                </label>
                            </div>

                        </div>

                    </div> */}
                    <div className="py-8 px-8 bg-white rounded-xl border-solid border-2 border-gray-100 shadow-md  space-y-2 mt-5">
                        <div >
                            <b> เลือกที่นั่ง</b>
                        </div>
                        <div className='flex justify-center'>
                            <div class="flex flex-wrap  gap-2 w-4/12">
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0 ">
                                    <input id="1" type="checkbox" class="hidden peer " name="preferred_activities[]" value="1" />
                                    <label for="1" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black m-3">A01</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="2" type="checkbox" class="hidden peer" name="preferred_activities[]" value="2" />
                                    <label for="2" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A02</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="3" type="checkbox" class="hidden peer" name="preferred_activities[]" value="3" />
                                    <label for="3" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A03</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0 ">
                                    <input id="4" type="checkbox" class="hidden peer" name="preferred_activities[]" value="4" />
                                    <label for="4" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A04</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="5" type="checkbox" class="hidden peer" name="preferred_activities[]" value="5" />
                                    <label for="5" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A05</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="6" type="checkbox" class="hidden peer" name="preferred_activities[]" value="6" />
                                    <label for="6" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A06</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0 ">
                                    <input id="1" type="checkbox" class="hidden peer " name="preferred_activities[]" value="1" />
                                    <label for="1" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black m-3">A01</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="2" type="checkbox" class="hidden peer" name="preferred_activities[]" value="2" />
                                    <label for="2" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A02</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="3" type="checkbox" class="hidden peer" name="preferred_activities[]" value="3" />
                                    <label for="3" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A03</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0 ">
                                    <input id="4" type="checkbox" class="hidden peer" name="preferred_activities[]" value="4" />
                                    <label for="4" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A04</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="5" type="checkbox" class="hidden peer" name="preferred_activities[]" value="5" />
                                    <label for="5" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A05</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="6" type="checkbox" class="hidden peer" name="preferred_activities[]" value="6" />
                                    <label for="6" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A06</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0 ">
                                    <input id="1" type="checkbox" class="hidden peer " name="preferred_activities[]" value="1" />
                                    <label for="1" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black m-3">A01</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="2" type="checkbox" class="hidden peer" name="preferred_activities[]" value="2" />
                                    <label for="2" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A02</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="3" type="checkbox" class="hidden peer" name="preferred_activities[]" value="3" />
                                    <label for="3" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A03</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0 ">
                                    <input id="4" type="checkbox" class="hidden peer" name="preferred_activities[]" value="4" />
                                    <label for="4" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A04</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="5" type="checkbox" class="hidden peer" name="preferred_activities[]" value="5" />
                                    <label for="5" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A05</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="6" type="checkbox" class="hidden peer" name="preferred_activities[]" value="6" />
                                    <label for="6" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A06</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0 ">
                                    <input id="1" type="checkbox" class="hidden peer " name="preferred_activities[]" value="1" />
                                    <label for="1" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black m-3">A01</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="2" type="checkbox" class="hidden peer" name="preferred_activities[]" value="2" />
                                    <label for="2" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A02</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="3" type="checkbox" class="hidden peer" name="preferred_activities[]" value="3" />
                                    <label for="3" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A03</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0 ">
                                    <input id="4" type="checkbox" class="hidden peer" name="preferred_activities[]" value="4" />
                                    <label for="4" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A04</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="5" type="checkbox" class="hidden peer" name="preferred_activities[]" value="5" />
                                    <label for="5" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A05</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="6" type="checkbox" class="hidden peer" name="preferred_activities[]" value="6" />
                                    <label for="6" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A06</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0 ">
                                    <input id="1" type="checkbox" class="hidden peer " name="preferred_activities[]" value="1" />
                                    <label for="1" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black m-3">A01</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="2" type="checkbox" class="hidden peer" name="preferred_activities[]" value="2" />
                                    <label for="2" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A02</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="3" type="checkbox" class="hidden peer" name="preferred_activities[]" value="3" />
                                    <label for="3" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A03</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0 ">
                                    <input id="4" type="checkbox" class="hidden peer" name="preferred_activities[]" value="4" />
                                    <label for="4" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A04</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="5" type="checkbox" class="hidden peer" name="preferred_activities[]" value="5" />
                                    <label for="5" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A05</div>
                                        </div>
                                    </label>
                                </div>
                                <div class="relative flex items-start py-4 ml-2 flex-shrink-0">
                                    <input id="6" type="checkbox" class="hidden peer" name="preferred_activities[]" value="6" />
                                    <label for="6" class="inline-flex items-center justify-between w-auto p-2 font-medium tracking-tight border rounded-lg cursor-pointer bg-pink-light text-brand-black border-pink-500 peer-checked:border-pink-400 peer-checked:bg-pink-700 peer-checked:text-white peer-checked:font-semibold peer-checked:underline peer-checked:decoration-brand-dark decoration-2">
                                        <div class="flex items-center justify-center w-full">
                                            <div class="text-sm text-brand-black  m-3">A06</div>
                                        </div>
                                    </label>
                                </div>
                               
                            
                              
                              
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
