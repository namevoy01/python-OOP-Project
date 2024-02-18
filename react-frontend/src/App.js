import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Fetch data from API endpoint
    fetch('http://127.0.0.1:8000/api/data')  // ระบุ URL ของ FastAPI Back-end
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <ul>
        {data.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>


      <div className='flex justify-center'>
        <div className="flex flex-col gap-6 w-100 p-20">
          <div className="relative h-11 w-full min-w-[500px]">
            <label for="countries" class="block mb-2 text-sm font-medium text-gray-900">จังหวัดต้นทาง</label>
            <select id="countries" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  ">
              <option selected>Choose a country</option>
              <option value="US">United States</option>
              <option value="CA">Canada</option>
              <option value="FR">France</option>
              <option value="DE">Germany</option>
            </select>
          </div>

          <div className="relative h-11 w-full min-w-[500px] mt-5">
            <label for="countries" class="block mb-2 text-sm font-medium text-gray-900">จุดขึ้นรถ</label>
            <select id="countries" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  ">
              <option selected>Choose a country</option>
              <option value="US">United States</option>
              <option value="CA">Canada</option>
              <option value="FR">France</option>
              <option value="DE">Germany</option>
            </select>
          </div>
          <div className="relative h-11 w-full min-w-[500px] mt-5">
            <label for="countries" class="block mb-2 text-sm font-medium text-gray-900">จังหวัดปลายทาง</label>
            <select id="countries" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  ">
              <option selected>Choose a country</option>
              <option value="US">United States</option>
              <option value="CA">Canada</option>
              <option value="FR">France</option>
              <option value="DE">Germany</option>
            </select>
          </div>
          <div className="relative h-11 w-full min-w-[500px] mt-5">
            <label for="countries" class="block mb-2 text-sm font-medium text-gray-900">จุดลงรถ</label>
            <select id="countries" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  ">
              <option selected>Choose a country</option>
              <option value="US">United States</option>
              <option value="CA">Canada</option>
              <option value="FR">France</option>
              <option value="DE">Germany</option>
            </select>
          </div>
          <div className="grid grid-cols-4 gap-4 mt-5">
            <div className="flex items-center ps-4 border border-gray-200 rounded ">
              <input id="bordered-radio-1" type="radio" value="" name="bordered-radio" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500  focus:ring-2 " />
              <label for="bordered-radio-1" className="w-full py-4 ms-2 text-sm font-medium text-gray-900 ">ไป-กลับ</label>
            </div>

            <div className="flex items-center ps-4 border border-gray-200 rounded ">
              <input id="bordered-radio-2" type="radio" value="" name="bordered-radio" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500  focus:ring-2 " />
              <label for="bordered-radio-2" className="w-full py-4 ms-2 text-sm font-medium text-gray-900 ">เที่ยวเดียว</label>
            </div>
          </div>

        </div>

      </div>



    </div>
  );
}

export default App;
