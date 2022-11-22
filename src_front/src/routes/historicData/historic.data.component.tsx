import { FloatingActionButton, FloatingActionButtonAlign } from '@progress/kendo-react-buttons';
import { useSelector } from 'react-redux';
import { Outlet,useNavigate } from 'react-router-dom';
import { selectBuildingsForCurrentUser } from '../../store/buildings/buildings.selector';
import { selectCurrentUser } from '../../store/user/user.selector';
import { DatePickerContainer, GraphContainer, RowContainer } from './historic.data.styles';
import { DatePicker } from "@progress/kendo-react-dateinputs";
import { useState } from 'react';


const HistoricData = () => {
    const currentUser = useSelector(selectCurrentUser);
    const buildings = useSelector(selectBuildingsForCurrentUser);
    const today= new Date();
    const navigate = useNavigate();
    const toFlexRequests=()=>{
        navigate("/flex");
    }

    const toBuildings=()=>{
        navigate("/buildings");
    }

    return (
        <>
            <RowContainer>
                <DatePickerContainer>
                    <DatePicker defaultValue={today} format={"dd.MM.yyyy"} />
                </DatePickerContainer>
                <GraphContainer>
                </GraphContainer>
            </RowContainer>
            
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "end" } as FloatingActionButtonAlign}
                text={'Continue'}
                onClick={toFlexRequests}
            />
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "start" } as FloatingActionButtonAlign}
                text={'Back o Buildings'}
                onClick={toBuildings}
            />
            <Outlet />
        </>
    );
};

export default HistoricData;