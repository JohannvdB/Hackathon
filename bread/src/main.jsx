import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom"

import Login from "./routes/login"
import Convener from "./routes/convener";
import Academic from "./routes/Academic";
import Student from "./routes/student"
import Root from "./routes/root"
import './index.css'


let router = createBrowserRouter([
  {
    path: "/",
    element: <Root />
  },
  {
    path: "/convener",
    element: <Convener />
  },
  {
    path: "/academic",
    element: <Academic />
  },
  {
    path: "/student",
    element: <Student />
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
