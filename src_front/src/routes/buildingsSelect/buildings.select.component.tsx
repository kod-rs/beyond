import { Outlet, useNavigate } from 'react-router-dom';


const BuildingsSelect = () => {
    const navigate = useNavigate();
    const toHistory=()=>{
        navigate("/history");
    }   
    
    return (
        <>
            <div>BUILDINGS</div>
            <div>SELECT</div>
            <button onClick={toHistory}>To History</button>
            <Outlet />
        </>
    );

};

export default BuildingsSelect;