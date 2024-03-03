import {useState, useEffect} from "react";
import axios from 'axios'
import {Form} from "react-router-dom"
import {Select} from "react-dropdown-select";

export default function Convener() {
    let [studentList, setStudentList] = useState([])
    let [academicList, setAcademicList] = useState([])
    let [student, setStudent] = useState({})
    let [academics, setAcademics] = useState([])
    let [moderator, setModerator] = useState()

    let insert = () => {

        if (student == null || academics == null) return

        axios
        .post("http://localhost:8000/assign_academics", {
            student_id: student[0].urn,
            academic_ids: academics.map(obj => obj.id),
            moderator_id: moderator[0].id
        })
        .then((res) => console.log(res.data))
        .catch((err) => console.log(err))
    }

    useEffect(() => {
        axios.get('http://localhost:8000/students')
        .then((res) => {
            const transformedData = res.data.map(student => ({
                urn: student.urn,
                name: student.name,
                specialisation: student.preferred_specialisation ? student.preferred_specialisation.specialisation : null
            }));
            setStudentList(transformedData);
        })
        .catch((error) => {
            console.error('Error fetching student data:', error);
            setStudentList([]);
        });

        axios.get('http://localhost:8000/academics')
        .then((res) => {
            const transformedData = res.data.map(academic => ({
                id: academic.id,
                name: academic.name
            }));
            setAcademicList(transformedData);
        })
        .catch((error) => {
            console.error('Error fetching student data:', error);
            setStudentList([]);
        });
    }, []);

    return (
        <>
            <h1>Convener</h1>
            <Form method='post' onSubmit={insert}>
                <label htmlFor='student'>Select Student: </label>
                <Select options={studentList} labelField="name" valueField="urn" onChange={(values) => setStudent(values)}/>
                <label htmlFor='academics'>Select Academics: </label>
                <Select options={academicList} labelField="name" valueField="id" onChange={(values) => setAcademics(values)} multi={true}/>
                <label htmlFor='moderator'>Select Moderator: </label>
                <Select options={academicList} labelField="name" valueField="id" onChange={(values) => setModerator(values)}/>
                <br></br>
                <button type='submit'>Submit</button>
            </Form>
        </>
    )
}