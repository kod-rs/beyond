import { Outlet, useNavigate } from 'react-router-dom';


const InsightAnalytics = () => {
    const navigate = useNavigate();
    const toFlex=()=>{
        navigate("/flex");
    }
    
    
    return (
        <>
            <div>Insight</div>
            <div>Analytics</div>
            <button onClick={toFlex} title={"Back to flex requests"}>Back to flex requests</button>
            <Outlet />
        </>
    );

};

export default InsightAnalytics;