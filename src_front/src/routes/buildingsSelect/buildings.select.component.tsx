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
import { selectBuildingsForCurrentUser, selectIsLoadingBuildings } from '../../store/buildings/buildings.selector';
import { getBuildingsStart, setBuildings } from '../../store/buildings/buildings.action';
import {
    Loader,
} from "@progress/kendo-react-indicators";
import cloneDeep from 'lodash/cloneDeep';

const BuildingsSelect = () => {
    const currentUser = useSelector(selectCurrentUser);
    const buildings = useSelector(selectBuildingsForCurrentUser);
    const isLoading = useSelector(selectIsLoadingBuildings);
    const [reload, setReload] = useState<boolean>(false);
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const toHistory = () => {
        navigate("/history");
    } 

    /* Checking if the current user is logged in and if the buildings are null. If they are null, it
    will dispatch the getBuildingsStart action. If the current user is null or undefined, it will
    navigate to the auth page. 
    */
    useEffect(() => {
        if (currentUser && buildings == null) {            
            dispatch(getBuildingsStart(currentUser));
        }

        if(currentUser === null || currentUser === undefined) {
            navigate("/auth");
        }
    }, [currentUser]);

    /**
     * "If the building_id of the building in the array is the same as the building_id of the item
     * passed in, then toggle the selected property of the building in the array, otherwise set the
     * selected property of the building in the array to the value of the selected property of the
     * building in the array."
     * 
     * I'm not sure if that's the best way to explain it, but I hope it helps.
     * @param {Building} item - Building =&gt; the item that is being selected
     */
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

    /**
     * I'm going to take the buildings array, clone it, then iterate over each building and set the
     * selected property to the value of the switch.
     * @param {SwitchChangeEvent} event - SwitchChangeEvent - this is the event that is triggered when
     * the switch is toggled.
     */
    const toggleSelectAll = (event: SwitchChangeEvent) => {
        let tmpB = cloneDeep(buildings);
        tmpB!.forEach((building) => {
            building.selected = event.target.value;
        });
        dispatch(setBuildings(tmpB!));
        setReload(!reload);
    }

    /**
     * I'm a function that takes a ListViewItemProps object as an argument and returns a React
     * component.
     * @param {ListViewItemProps} props - ListViewItemProps
     * @returns A React component that is a function that returns a JSX element.
     */
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
                {isLoading && <Loader size="large"  type="converging-spinner" />}
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


