import { useSelector } from 'react-redux';
import { Outlet, useNavigate } from 'react-router-dom';
import { selectCurrentUser } from '../../store/user/user.selector';
import { MapContainer, ListContainer } from './buildings.select.styles';
import { useEffect } from 'react';
import {
    FloatingActionButton,
    FloatingActionButtonItemProps,
} from '@progress/kendo-react-buttons'; 

const BuildingsSelect = () => {
    const currentUser = useSelector(selectCurrentUser);
    const navigate = useNavigate();
    const toHistory = () => {
        navigate("/history");
    } 

    useEffect(() => {
        if (currentUser) {
            //get buildings list from backend

        }
    });
    
    return (
        <>
            <h1>Select buildings</h1>
            <MapContainer>Map</MapContainer>
            <ListContainer>List</ListContainer>
            
            <FloatingActionButton text={'Continue'} onClick={toHistory} />
            <Outlet />
        </>
    );

};

export default BuildingsSelect;


