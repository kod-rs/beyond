import { Outlet,useNavigate } from 'react-router-dom';


const HistoricData = () => {
    const navigate = useNavigate();
    const toFlexRequests=()=>{
        navigate("/flex");
    }

    const toBuildings=()=>{
        navigate("/buildings");
    }

    return (
        <>
            <div>Historic</div>
            <div>Data</div>
            <button onClick={toFlexRequests} title={"To Flex requests"}>To Flex requests</button>
            <button onClick={toBuildings} title={"Back o Buildings"}>Back o Buildings</button>
            <Outlet />
        </>
    );
};

export default HistoricData;