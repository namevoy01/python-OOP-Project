import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Home from './page/home';
import Travel from './page/Travel';
import Seat from './page/seat';
import Inputfill from './page/Inputfill';
import Login from './page/login';
import Ticket from './page/ticket';
import Admin from './page/admin';
import TicketRemove from './page/ticketRemove';
import Error from './page/error404';
const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />
  },
  {
    path: "travel",
    element: <Travel />
  },
  {
    path: "admin",
    element: <Admin />
  },

  {
    path: "inputfill",
    element: <Inputfill />
  },
  {
    path: "ticketremove",
    element: <TicketRemove />
  },
  {
    path: "login",
    element: <Login />
  },
  {
    path: "ticket",
    element: <Ticket />
  },
  {
    path: "seat",
    element: <Seat />
  },

  {
    path: "*",
    element: <Error />
  }
])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>

);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
