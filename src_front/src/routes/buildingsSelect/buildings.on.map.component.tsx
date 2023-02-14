import { useState, useEffect } from "react";
import { Map, Marker, Point } from "pigeon-maps";
import { Building } from "../../store/buildings/buildings.types";

type BuildingsOnMapProps = {
    buildings: Building[];
    toggleSelectBuilding: (building: Building) => void;
}

export function BuildingsOnMap(props: BuildingsOnMapProps) {
    const [hue] = useState<number>(0);
    const color = `hsl(${hue % 360}deg 39% 70%)`;
    const colorSelected = `hsl(${60 % 360}deg 39% 70%)`;
    const [mapHeight, setMapHeight] = useState(window.innerHeight * 0.8);
    const [defaultCenter, setDefaultCenter] = useState<Point>([45.8150, 15.9819]);

    /**
     * "If the props object has a buildings property that is an array with at least one element, then
     * return the average longitude and latitude of the buildings in the array, otherwise return the
     * longitude and latitude of Zagreb, Croatia."
     * @returns An array of two numbers.
     */
    const getAverageMapPosition = () => {
        let point_:Point=[45.8150, 15.9819] as Point;
        if (props && props.buildings && props.buildings.length>0) {
            let long = 0;
            let lat = 0;
            props.buildings.forEach(building => {
                long += building.longitude;
                lat += building.latitude;
            });
            long = long / props.buildings.length;
            lat = lat / props.buildings.length;
            point_ = [long, lat] as Point;
        }
        return point_;
    }

    // Add this hook to run the function whenever the window is resized
    useEffect(() => {
        // Add an event listener for the 'resize' event
        window.addEventListener('resize', handleResize);

        // Return a function to clean up the event listener when the component is unmounted
        return () => {
            window.removeEventListener('resize', handleResize);
        };
    });

    // Define a function to handle the 'resize' event
    const handleResize = () => {
        // Update the mapHeight state variable with the new window height
        setMapHeight(window.innerHeight * 0.8);
    }

    /* It's a React hook that runs sets the initial map center position whenever the value of props.buildings changes. */
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


