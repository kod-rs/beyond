import { Outlet, useNavigate } from 'react-router-dom';


const FlexRequests = () => {
    const navigate = useNavigate();
    const toInsight=()=>{
        navigate("/insight");
    }    

    const toHistory=()=>{
        navigate("/history");
    }  
    
    return (
        <>
            <div>Flex</div>
            <div>Requests</div>
            <button onClick={toInsight} title={"To Insight"}>To Insight</button>
            <button onClick={toHistory} title={"Back To History"}>Back To History</button>
            <Outlet />
        </>
    );

};

export default FlexRequests;