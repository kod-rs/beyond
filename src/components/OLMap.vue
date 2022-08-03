<template>
    <div id="c">
        <div id="f">
            <div class="cell cell-map">
                a
                <!-- <MapContainer style="  height: calc(100vh - 100px); " :geojson="geojson"
                    v-on:select="selected = $event">
                </MapContainer> -->

                <MapContainer :geojson="geojson" v-on:select="selected = $event">
                </MapContainer>


            </div>
            <div class="cell cell-edit">
                <!-- b -->

                <form class="d-flex ms-auto my-3 my-lg-0">
                    <div class="input-group">
                        <input class="form-control" type="search" placeholder="Search" aria-label="Search" />

                    </div>
                </form>

                <!-- <Edit :geojson="geojson" v-on:change="geojson = $event"></Edit> -->
            </div>
            <div class="cell cell-inspect">
                c
                <!-- <Inspect :feature="selected"></Inspect> -->
            </div>
        </div>

    </div>
</template>

<script>
import MapContainer from './MapContainer'
import Edit from './Edit'
import Inspect from './Inspect'

export default {
    components: {
        Inspect,
        Edit,
        MapContainer
    },
    data: () => ({
        selected: undefined,
        geojson: {
            type: 'Feature',
            properties: {
                name: 'default object',
                quality: 'top'
            },
            geometry: {
                type: 'Polygon',
                coordinates: [
                    [
                        [
                            -27.0703125,
                            43.58039085560784
                        ],
                        [
                            -28.125,
                            23.563987128451217
                        ],
                        [
                            -10.8984375,
                            32.84267363195431
                        ],
                        [
                            -27.0703125,
                            43.58039085560784
                        ]
                    ]
                ]
            }
        }
    })
}
</script>

<style>
#c {
    height: 100%;
    margin: 0;
}

#f {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    height: 100%;
    display: grid;
    grid-template-columns: 100vh;
    grid-auto-rows: 1fr;
    grid-gap: 1rem;
    padding: 1rem;
    box-sizing: border-box;
}

.cell {
    border-radius: 4px;
    background-color: lightgrey;
}

.cell-map {
    grid-column: 1;
    grid-row-start: 1;
    grid-row-end: 3;
}

.cell-edit {
    grid-column: 2;
    grid-row: 1;
}

.cell-inspect {
    grid-column: 2;
    grid-row: 2;
}
</style>