import {Link} from "react-router-dom"

export default function Root() {

    return (
        <>
            <Link to="/Convener"><h1>Convener</h1></Link>
            <Link to="/Academic"><h1>Academic</h1></Link>
            <Link to="/Student"><h1>Student</h1></Link>
        </>
    )
}