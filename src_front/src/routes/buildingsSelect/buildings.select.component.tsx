import { useDispatch, useSelector } from 'react-redux';
import { Outlet, useNavigate } from 'react-router-dom';
import { selectCurrentUser } from '../../store/user/user.selector';
import { MapContainer, ListContainer, RowContainer } from './buildings.select.styles';
import { useEffect, useState } from 'react';
import { FloatingActionButton } from '@progress/kendo-react-buttons'; 
import { ListView, ListViewItemProps } from "@progress/kendo-react-listview";
import { Switch } from "@progress/kendo-react-inputs";
import { BuildingsOnMap } from './buildings.on.map.component';
import { Building } from '../../store/buildings/buildings.types';
import { selectBuildingsForCurrentUser } from '../../store/buildings/buildings.selector';
import { getBuildingsStart } from '../../store/buildings/buildings.action';

const BuildingsSelect = () => {
    const currentUser = useSelector(selectCurrentUser);
    const buildings = useSelector(selectBuildingsForCurrentUser);
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const toHistory = () => {
        navigate("/history");
    } 

    useEffect(() => {
        if (currentUser) {
            //get buildings list from backend
            dispatch(getBuildingsStart(currentUser));
        }
    }, [currentUser]);

    useEffect(() => {
        if (buildings) {
            console.log('buildings:');
            console.log(buildings);
            
        }
    }, [buildings]);

    const toggleSelectItem = (item: Building):void => {
        console.log(item);
    };

    const BuildingsListViewItemRender = (props: ListViewItemProps) => {
        let buildingData = props.dataItem;
        return (
            <RowContainer>
                <div className="col-2 align-left">
                    {buildingData.building_name}
                </div>

                <div className="col-2 align-right">
                    <div className="k-chip k-chip-md k-rounded-md k-chip-solid k-chip-solid-base ">
                        <Switch defaultChecked={buildingData.selected} onChange={() => { toggleSelectItem(buildingData) }} />
                    </div>
                </div>
            </RowContainer>
        );
    };
    
    return (
        <>
            <RowContainer>
                <MapContainer>
                    <BuildingsOnMap
                        toggleSelectBuilding={toggleSelectItem}
                        buildings={buildings ? buildings: []}
                    />
                </MapContainer>
                <ListContainer>
                    <ListView
                        data={buildings ? buildings : []}
                        item={BuildingsListViewItemRender}
                        style={{ width: "100%" }}
                    />
                </ListContainer>
            </RowContainer>
            <FloatingActionButton text={'Continue'} onClick={toHistory} />
            <Outlet />
        </>
    );
};

export default BuildingsSelect;


