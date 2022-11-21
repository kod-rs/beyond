import React, { useState, useEffect } from "react";
import { Map, Marker, Point } from "pigeon-maps";
import { Building } from "../../store/buildings/buildings.types";

type BuildingsOnMapProps = {
    buildings: Building[];
    toggleSelectBuilding: (building: Building) => void;
}

export function BuildingsOnMap(props: BuildingsOnMapProps) {
    const [hue, setHue] = useState<number>(0);
    const color = `hsl(${hue % 360}deg 39% 70%)`;
    const colorSelected = `hsl(${60 % 360}deg 39% 70%)`;
    const [mapHeight, setMapHeight] = useState(window.innerHeight * 0.8);
    const [defaultCenter, setDefaultCenter] = useState<Point>([45.8150, 15.9819]);

    const getAverageMapPosition = () => {
        if (props.buildings && props.buildings.length>0) {
            let long = 0;
            let lat = 0;
            props.buildings.forEach(building => {
                long += building.longitude;
                lat += building.latitude;
            });
            long = long / props.buildings.length;
            lat = lat / props.buildings.length;
            return [long, lat] as Point;
        }
        return [45.8150, 15.9819] as Point;
    }

    useEffect(() => {
        setMapHeight(window.innerHeight * 0.8);
    }, [window.innerHeight]);

    useEffect(() => {

        if (props.buildings && props.buildings.length>0) {
            setDefaultCenter(getAverageMapPosition());
        }
        
    }, [props.buildings]);

    return (
        <Map height={mapHeight} defaultCenter={defaultCenter} defaultZoom={7}>
            {
                props.buildings &&
                    props.buildings.map((building:Building) => (
                        <Marker
                            key={building.building_id}
                            width={50}
                            anchor={[building.latitude, building.longitude]}
                            color={building.selected ? colorSelected : color}
                            onClick={() => { props.toggleSelectBuilding(building) }}
                        />
                    ))
            }
        </Map>
    )
}


