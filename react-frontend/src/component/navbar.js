import { Link } from 'react-router-dom';


const Navbar = () => {
    const storedUserData = JSON.parse(localStorage.getItem('userData'));
    const handleLogout = () => {
        localStorage.removeItem('userData');

        window.location.href = '/';
    };
    return (

        <nav className="bg-white border-gray-200 dark:bg-gray-900 dark:border-gray-700 shadow-md">

            <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">

                {storedUserData ? (
                    <div className='flex'>
                        <img className='rounded-full' style={{ width: "100%", height: '70px' }}
                            src="https://media.discordapp.net/attachments/1204425495962324992/1217183769304371260/Pink_Cute_Simple_Textured_Gaming_Twitch_Logo_.gif?ex=660319b8&is=65f0a4b8&hm=fb61cc8859109a6ed4e58e8a822508dfb76095d2d5b7ab26609f3aa3158c352f&=&width=662&height=662" alt="Description" />

                        <span className="ms-3 self-center text-2xl font-semibold whitespace-nowrap dark:text-white">ThaiTour Admin</span>
                    </div>
                ) : (
                    <Link to='/' className='flex'>
                        <img className='rounded-full' style={{ width: "100%", height: '70px' }}
                            src="https://media.discordapp.net/attachments/1204425495962324992/1217183769304371260/Pink_Cute_Simple_Textured_Gaming_Twitch_Logo_.gif?ex=660319b8&is=65f0a4b8&hm=fb61cc8859109a6ed4e58e8a822508dfb76095d2d5b7ab26609f3aa3158c352f&=&width=662&height=662" alt="Description" />

                        <span className="ms-3 self-center text-2xl font-semibold whitespace-nowrap dark:text-white">ThaiTour</span>
                    </Link>
                )}

                {storedUserData ? (
                    <div className="hidden w-full md:block md:w-auto" id="navbar-multi-level">
                        <ul className="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                            <li>
                               <button type="button" onClick={handleLogout} class=" text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 px-20 text-lg">ออกจากระบบ</button>
                            </li>
                        </ul>
                    </div>
                ) : (
                    <div className="hidden w-full md:block md:w-auto" id="navbar-multi-level">
                        <ul className="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                            <li>
                                <Link to='/ticketremove'> <button type="button" class="text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 px-20 text-lg">ยกเลิกตั๋ว</button></Link>
                            </li>
                            <li>
                                <Link to='/searchticket'> <button type="button" class="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 px-20 text-lg">พิมพ์ตั๋ว</button></Link>
                            </li>
                            <li>
                                <Link to='/login'> <button type="button" class="text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 px-20 text-lg">เจ้าหน้าที่</button></Link>
                            </li>
                        </ul>
                    </div>
                )}


            </div>

        </nav>
    );
};

export default Navbar;
