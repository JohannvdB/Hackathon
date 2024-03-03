import { useState, useEffect, useCallback } from 'react'
import axios from 'axios'
import {Form} from "react-router-dom"
import Select from "react-dropdown-select"

export default function Academic() {
    
    let [academic, setAcademic] = useState ({
        name: '',
        specialisation: [],
    });

    let [students, setStudents] = useState([])

    let [modules, setModule] = useState([])

    let [mark, setMark] = useState('')

    let [chosenStudent, setChosenStudent] = useState(0)

    let [chosenModule, setChosenModule] = useState('')

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/academic_students/1')
        .then((res) => setStudents(res.data.students))
        .catch((err) => console.log(err))
    }, [])

    let studentChange = (e) => {
        e.preventDefault();

        let {name, value} = e.target

        setStudents((prevStudent) => ({...prevStudent, [name]: value}))
    }

    let submit = (target) => {
        target.preventDefault();

        axios.post("http://127.0.0.1:8000/assign_mark", {
            "student_id": chosenStudent,
            "mark": mark,
            "module": chosenModule
        })
        .then((res) => console.log(res))
        .catch((err) => console.log(err))
    }
    
    let StudentInput = (values) => {
        setChosenStudent(values[0].urn);
        axios.get('http://127.0.0.1:8000/student_marks/' + values[0].urn)
        .then((res) => {
            // Assuming the response contains an array of module objects
            // Extract module labels from the response and update modules state
            const moduleLabels = res.data.map(({ moduleCode }) => ({
                value: moduleCode,
                label: moduleCode
            }));
            setModule(moduleLabels);
        })
        .catch((error) => {
            // Handle error if the API call fails
            console.error('Error fetching modules:', error);
            setModule([]); // Set modules to an empty array or handle error state accordingly
        });
    }

    let ModuleChoice = values => {
        setChosenModule(values[0].value)
    }

return(
    <>
        <h1>Academic</h1>

        <Form method='post' onSubmit={submit}>
            Select Student: <Select options={students} labelField='urn' valueField='name' onChange={StudentInput} />
                
            Select Module: <Select options={modules} onChange={ModuleChoice} />

            <label htmlFor='mark'>Mark: </label>
            <input 
                type='number'
                id='mark'
                name='mark'
                value={mark}
                onChange={e => setMark(e.target.value)}
                placeholder='Marks'
                min={0}
                max={100}
                required
            />

            <button id='submit' type='submit' className='submit'>Submit</button>
        </Form>
    </>
)
}