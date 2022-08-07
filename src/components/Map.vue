<template>
    <ol-map :loadTilesWhileAnimating="true" :loadTilesWhileInteracting="true" style="height:400px">
        <ol-view ref="view" :center="center" :rotation="rotation" :zoom="zoom" :projection="projection" />

        <ol-tile-layer>
            <ol-source-osm />
        </ol-tile-layer>

        <ol-vector-layer>
            <ol-source-vector ref="vectors">
                <ol-interaction-draw @drawstart="drawstart" :type="drawType">
                </ol-interaction-draw>
            </ol-source-vector>

            <ol-style>
                <ol-style-icon :src="markerIcon" :scale="2"></ol-style-icon>
            </ol-style>
        </ol-vector-layer>

    </ol-map>
</template>

<script>
import markerIcon from './../assets/login_logo.png'
import { ref } from "vue";

export default {
    name: "test",
    setup() {
        const center = ref([54.1966794, 31.8797732])
        const projection = ref('EPSG:4326')
        const zoom = ref(6)
        const rotation = ref(0)

        const markers = ref(null);
        const drawType = ref("Point")

        const drawedMarker = ref()
        const vectors = ref(null);

        const drawstart = (event) => {
            vectors.value.source.removeFeature(drawedMarker.value);
            drawedMarker.value = event.feature;
            console.log(vectors.value.source)
        }

        return {
            vectors,
            drawstart,
            center,
            projection,
            zoom,
            rotation,
            markerIcon,
            markers,
            drawType
        }
    },
}
</script>