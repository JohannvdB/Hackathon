import { useState, useEffect } from 'react'
import axios from 'axios'
import {Form} from "react-router-dom"

export default function Login() {

  let [info, setInfo] = useState
  ({
    username: '',
    password: '',
  });

  let infoChange = (e) => {
    e.preventDefault();

    let { name, value } = e.target;

    setInfo((prevInfo) => ({ ...prevInfo, [name]: value }))
  }

  let submit = (e) => {
    e.preventDefault();

    axios
    .post("http://127.0.0.1:8000/api/auth/login/", {
      username: info.username,
      password: info.password
    })
    .then((res) => {
      localStorage.setItem('accessToken', res.data.access_token);
      localStorage.setItem('refreshToken', res.data.refresh_token);
      this.props.history.push('/' + res.data.role);
    })
    .catch((err) => console.log(err))
  }
  

  return (
    <>
      <h1>BKAERY</h1>
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
        <label htmlFor='password'>Password: </label>
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