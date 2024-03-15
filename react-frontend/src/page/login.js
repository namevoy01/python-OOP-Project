import React, { useState, useEffect } from 'react';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loginSuccess, setLoginSuccess] = useState(false);
    const [apiData, setApiData] = useState(null);
    const [loading, setLoading] = useState(false);

    localStorage.setItem('adminUsername', apiData); // เก็บ username ของ admin

    const handleUsernameChange = (event) => {
        setUsername(event.target.value);
    };

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await fetch(`http://127.0.0.1:8000/api/login?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (response.ok) {
                const data = await response.json();
                setApiData(data);
                setLoginSuccess(true);

                // เก็บ username ลงใน localStorage
            } else {
                setLoginSuccess(false);
            }
        } catch (error) {
            console.error('Error occurred:', error);
        }
    };
    console.log(loading);
    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/login?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`);
                if (response.ok) {
                    const data = await response.json();
                    setApiData(data);
                    setLoading(false);
                } else {
                    setLoading(false);
                }
            } catch (error) {
                console.error('Error occurred:', error);
                setLoading(false);
            }
        };

        if (loginSuccess) {
            fetchData();
        }
    }, [loginSuccess, username, password]);

    useEffect(() => {
        if (apiData !== null && apiData.length !== 0) {
            localStorage.setItem('userData', JSON.stringify(username));
            window.location.href = '/admin'; // เปลี่ยนหน้าไปยังหน้า admin โดยใช้ window.location.href
        }
    }, [apiData]);

    const backHome = () => {
        window.location.href = '/';
    };
    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
            <div className="max-w-md w-full space-y-8">
                <div>
                    <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Login</h2>
                </div>
                <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
                    <input type="hidden" name="remember" value="true" />
                    <div className="rounded-md shadow-sm -space-y-px">
                        <div>
                            <label htmlFor="username" className="sr-only">Username</label>
                            <input
                                id="username"
                                name="username"
                                type="text"
                                autoComplete="username"
                                required
                                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 focus:z-10 sm:text-sm"
                                placeholder="Username"
                                value={username}
                                onChange={handleUsernameChange}
                            />
                        </div>
                        <div>
                            <label htmlFor="password" className="sr-only ">Password</label>
                            <input
                                id="password"
                                name="password"
                                type="password"
                                autoComplete="current-password"
                                required
                                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 focus:z-10 sm:text-sm"
                                placeholder="Password"
                                value={password}
                                onChange={handlePasswordChange}
                            />
                        </div>
                    </div>

                    <div className='flex'>
                        <button type="submit" className="w-10/12 flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-pink-600 hover:bg-pink-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pink-500">
                            Login
                        </button>
                        <button type="submit" onClick={backHome} className="ms-3 w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-gray-600 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500">
                            หน้าแรก
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default Login;
