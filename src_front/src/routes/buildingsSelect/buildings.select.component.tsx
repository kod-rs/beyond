import { useDispatch, useSelector } from 'react-redux';
import { Outlet, useNavigate } from 'react-router-dom';
import { selectCurrentUser } from '../../store/user/user.selector';
import { MapContainer, ListContainer, RowContainer, SwitchContainer } from './buildings.select.styles';
import { useEffect, useState } from 'react';
import { FloatingActionButton, FloatingActionButtonAlign } from '@progress/kendo-react-buttons'; 
import { ListView, ListViewItemProps } from "@progress/kendo-react-listview";
import { Switch, SwitchChangeEvent } from "@progress/kendo-react-inputs";
import { Label } from "@progress/kendo-react-labels";
import { BuildingsOnMap } from './buildings.on.map.component';
import { Building } from '../../store/buildings/buildings.types';
import { selectBuildingsForCurrentUser } from '../../store/buildings/buildings.selector';
import { getBuildingsStart, setBuildings } from '../../store/buildings/buildings.action';
import cloneDeep from 'lodash/cloneDeep';

const BuildingsSelect = () => {
    const currentUser = useSelector(selectCurrentUser);
    const buildings = useSelector(selectBuildingsForCurrentUser);
    const [reload, setReload] = useState<boolean>(false);
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const toHistory = () => {
        navigate("/history");
    } 

    useEffect(() => {
        if (currentUser && buildings == null) {
            //get buildings list from backend
            dispatch(getBuildingsStart(currentUser));
        }

        if(currentUser === null || currentUser === undefined) {
            navigate("/auth");
        }
    }, [currentUser]);

    const toggleSelectItem = (item: Building): void => {
        let tmpB = cloneDeep(buildings);
        tmpB!.forEach((building) => {
            let selected = building.selected ? true : false;
            if (building.building_id === item.building_id) {
                building.selected = !selected;
            } else {
                building.selected = selected;
            }
        });
        dispatch(setBuildings(tmpB!));
        setReload(!reload);
    };

    const toggleSelectAll = (event: SwitchChangeEvent) => {
        let tmpB = cloneDeep(buildings);
        tmpB!.forEach((building) => {
            building.selected = event.target.value;
        });
        dispatch(setBuildings(tmpB!));
        setReload(!reload);
    }

    const BuildingsListViewItemRender = (props: ListViewItemProps) => {
        let buildingData = props.dataItem;
        return (
            <RowContainer>
                <div>
                    {buildingData.building_name}
                </div>

                <div>
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
                    <SwitchContainer>
                        <Label>Select All</Label>
                        <Switch id={"selectAllSwitch"} onChange={toggleSelectAll} />
                    </SwitchContainer>
                    <ListView
                        data={buildings ? buildings : []}
                        item={BuildingsListViewItemRender}
                        style={{ width: "100%" }}
                    />
                </ListContainer>
            </RowContainer>
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "end" } as FloatingActionButtonAlign}
                text={'Confirm & start analytics '}
                onClick={toHistory}
            />
            <Outlet />
        </>
    );
};

export default BuildingsSelect;


