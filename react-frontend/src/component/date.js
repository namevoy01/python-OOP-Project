import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { format } from 'date-fns';

const MyDatePicker = ({ onDateChange }) => {
  const [selectedDate, setSelectedDate] = useState(null);

  const handleDateChange = (date) => {
    setSelectedDate(date);
    if (date) {
      onDateChange(format(date, 'dd-MM-yyyy'));
    } else {
      onDateChange(null); // Handle the case when no date is selected
    }
  };

  return (
    <form className="mt-3">
      <DatePicker
        placeholderText='DD/MM/YYYY'
        selected={selectedDate}
        onChange={handleDateChange}
        dateFormat="dd/MM/yyyy"
        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        minDate={new Date()}
      />
    </form>
  );
};

export default MyDatePicker;
