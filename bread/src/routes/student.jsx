import { useState, useEffect } from 'react'
import axios from 'axios'
import {Form} from "react-router-dom"

export default function Student() {

    let [info, setInfo] = useState([]);

      useEffect(() => {
        axios.get("http://127.0.0.1:8000/student_marks/2424")
            .then((res) => {
                const transformedData = res.data.map(data => ({
                    moduleCode: data.moduleCode,
                    mark: data.mark,
                }));
                setInfo(transformedData);
            })
            .catch((err) => console.log(err));
    }, []);

    return (
      <div>
          <h1>Student Marks</h1>
          <ul>
              {info.map((item, index) => (
                  <li key={index}>
                      <span>Module Code: {item.moduleCode}</span><br></br>
                      <span>Mark: {item.mark !== null ? item.mark : 'Not available'}</span>
                  </li>
              ))}
          </ul>
      </div>
  )
}