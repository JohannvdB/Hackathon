import { useState, useEffect } from 'react'
import axios from 'axios'
import {Form} from "react-router-dom"

export default function Student() {

    let [info, setInfo] = useState({});

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
    // let students
    // axios.get("http://127.0.0.1:8000/api/students")
    // .then((res) => students = res)
    // .catch((err) => console.log(err))
      
    // return(
    // <>
    //   <h1></h1>
    //   <Form method='post' onSubmit={submit}>
    //     <label htmlFor='username'>Username: </label>
    //     <input 
    //       id='username'
    //       name='username'
    //       value={info.username}
    //       type='text'
    //       placeholder='Username'
    //       onChange={infoChange}
    //       required
    //     />
    //     <label htmlFor='password'>Username: </label>
    //     <input 
    //       id='password'
    //       name='password'
    //       value={info.password}
    //       type='password'
    //       placeholder='Password'
    //       onChange={infoChange}
    //       required
    //     />
    //     <button id='submit' type='submit' className='submit'>Login</button>
    //   </Form>
    // </>
    // )
}