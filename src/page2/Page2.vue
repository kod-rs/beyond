<!-- <template>
    <div>
        <p>page 2</p>
    </div>

    <nav class="navbar navbar-light bg-light">
        <form class="form-inline">
            <input class="form-control mr-sm-2" type="search" placeholder="type location" aria-label="Search">
        </form>
    </nav>

    <div class="row">
        <div class="col p-3 bg-primary text-white">search


        </div>
        <div class="col p-3 bg-dark text-white">map placeholder</div>
        <div class="col p-3 bg-primary text-white">select options</div>
    </div>



</template>
 -->

<!-- 

<style>
@import './page2.css';
</style>  -->

<template>
    <div id="c">
        <div id="f">
            <div class="cell cell-map">
                a
                <!-- <MapContainer :geojson="geojson" v-on:select="selected = $event"></MapContainer> -->
            </div>
            <div class="cell cell-edit">
                b
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
import MapContainer from '../components/MapContainer'
import Edit from '../components/Edit'
import Inspect from '../components/Inspect'

export default {
    name: 'App',
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
    /* width: 100%;
    height: 100%; */

    height: 100%;
    /* height: 500px; */
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
