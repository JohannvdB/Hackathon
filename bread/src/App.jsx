import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'

function App() {
  const [academics, setAcademics] = useState([])

  useEffect (() => {
      axios
      .get("//localhost:8000/api/academics")
      .then((res) => setAcademics(res.data))
      .catch((err) => console.log(err))
    }, []) // reason for empty dependency array as axios arg: https://stackoverflow.com/a/72357701

  return (
    <>
      <h1>BKAERY</h1>
      <ul>
        {academics.map((academic) => {
          return <li key={academic.id}>{academic.name}</li>
        })}
      </ul>
    </>
  )
}

export default App
