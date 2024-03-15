import React from 'react';

const NotFound = () => {
  return (
    <div className="flex items-center justify-center h-screen bg-gray-100">
      <div className="text-center">
        <h1 className="text-9xl font-bold text-gray-800">404</h1>
        <p className="text-2xl text-gray-600">Page Not Found</p>
        <a href="/" className="text-blue-500 hover:underline mt-4 inline-block">กลับสู่หน้าหลัก</a>
      </div>
    </div>
  );
};

export default NotFound;
