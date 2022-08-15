<template>
    <div id="popup" class="ol-popup">
        <a href="#" id="popup-closer" class="ol-popup-closer"></a>
        <div id="popup-content"></div>
    </div>
</template>

<script>
import Overlay from 'ol/Overlay';

export default {
    data() {
        return {
            content: undefined,
            overlay: undefined
        }
    },
    methods: {
        setText(hdms) {
            this.content.innerHTML = '<p>You clicked here:</p><code>' + hdms + '</code>';

        },
        setPosition(coordinate) {
            this.overlay.setPosition(coordinate);

        },
        getOverlay() {
            return this.overlay;
        }
    },

    mounted() {
        /**
      * Elements that make up the popup.
      */
        const container = document.getElementById('popup');
        this.content = document.getElementById('popup-content');
        const closer = document.getElementById('popup-closer');

        /**
         * Create an overlay to anchor the popup to the map.
         */
        this.overlay = new Overlay({
            element: container,
            autoPan: {
                animation: {
                    duration: 250,
                },
            },
        });

        /**
         * Add a click handler to hide the popup.
         * @return {boolean} Don't follow the href.
         */
        closer.onclick = function () {
            this.overlay.setPosition(undefined);
            closer.blur();
            return false;
        };

        // /**
        //  * Add a click handler to the map to render the popup.
        //  */
        // map.on('singleclick', function (evt) {
        //     console.log("clicked", evt)
        //     const coordinate = evt.coordinate;
        //     const hdms = toStringHDMS(toLonLat(coordinate));

        //     content.innerHTML = '<p>You clicked here:</p><code>' + hdms + '</code>';
        //     overlay.setPosition(coordinate);
        // });


    }
}

</script>

<style>
.ol-popup {
    position: absolute;
    background-color: white;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #cccccc;
    bottom: 12px;
    left: -50px;
    min-width: 280px;
}

.ol-popup:after,
.ol-popup:before {
    top: 100%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
}

.ol-popup:after {
    border-top-color: white;
    border-width: 10px;
    left: 48px;
    margin-left: -10px;
}

.ol-popup:before {
    border-top-color: #cccccc;
    border-width: 11px;
    left: 48px;
    margin-left: -11px;
}

.ol-popup-closer {
    text-decoration: none;
    position: absolute;
    top: 2px;
    right: 8px;
}

.ol-popup-closer:after {
    content: "✖";
}
</style>