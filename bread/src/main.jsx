import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom"

import Login from "./routes/login"
import Convener from "./routes/convener";
import Academic from "./routes/Academic";
import './index.css'


let router = createBrowserRouter([
  {
    path: "/",
    element: <Convener />
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
