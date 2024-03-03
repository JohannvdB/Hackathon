import { useState, useEffect } from 'react'
import axios from 'axios'
import {Form} from "react-router-dom"

export default function Student() {

    let [info, setInfo] = useState
    ({
        name: '',
        modules: [],
        marks: []
    });

    let infoChange = (e) => {
        e.preventDefault();
    
        let { name, value } = e.target;
    
        setInfo((prevInfo) => ({ ...prevInfo, [name]: value }))
      }
    
    let students
    axios.get("http://127.0.0.1:8000/api/students")
    .then((res) => students = res)
    .catch((err) => console.log(err))
      
    return(
    <>
      <h1></h1>
      <Form method='post' onSubmit={submit}>
        <label htmlFor='username'>Username: </label>
        <input 
          id='username'
          name='username'
          value={info.username}
          type='text'
          placeholder='Username'
          onChange={infoChange}
          required
        />
        <label htmlFor='password'>Username: </label>
        <input 
          id='password'
          name='password'
          value={info.password}
          type='password'
          placeholder='Password'
          onChange={infoChange}
          required
        />
        <button id='submit' type='submit' className='submit'>Login</button>
      </Form>
    </>
    )
}