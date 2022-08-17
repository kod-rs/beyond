window.onload = () => {
    (async () => {
        await map_drivers();
    })();
}

async function map_drivers() {
    await set_position();
    show_markers();
}

function get_markers() {
    return {
        "2": {
            lon: "15.97357328039518",
            lat: "45.79500836301531",
            listing_id: "listing_1"
        },
        "3": {
            lon: "15.951257301391397",
            lat: "45.79644458901876",
            listing_id: "listing_2"
        },
        "4": {
            lon: "15.938554359496676",
            lat: "45.80996723511464",
            listing_id: "3"
        },
        "5": {
            lon: "15.994859291137193",
            lat: "45.820376239569896",
            listing_id: "4"
        },
    }
}

function show_markers() {
    let markers = get_markers();
    var map_inst = SingletonFactory.getInstance();

    for (const key in markers) {
        map_inst.add_marker(
            markers[key].lon,
            markers[key].lat,
            markers[key].listing_id
        )
    };
}

function href_jump(h) {
    document.getElementById(h).scrollIntoView();
}


var SingletonFactory = (function () {
    class SingletonClass {

        constructor() {
            const JELACIC = {
                lat: 45.813138,
                lng: 15.977264
            };

            var lat = JELACIC.lat;
            var lon = JELACIC.lng;
            this.zoom = 13;

            this.fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984
            this.toProjection = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection
            var position = new OpenLayers.LonLat(lon, lat).transform(this.fromProjection, this.toProjection);

            this.map = new OpenLayers.Map("Map");
            var mapnik = new OpenLayers.Layer.OSM();
            this.map.addLayer(mapnik);

            this.markers = new OpenLayers.Layer.Markers("Markers");
            this.map.addLayer(this.markers);

            this.map.setCenter(position, this.zoom);
        }

        add_user_marker(lon, lat) {
            let position = new OpenLayers.LonLat(lon, lat).transform(this.fromProjection, this.toProjection);
            let marker = new OpenLayers.Marker(position);
            marker["icon"]["url"] = "../resources/OpenLayers-2.13.1/img/marker-blue.png"
            this.markers.addMarker(marker);
            let title = "title "

            marker.events.register("click", marker, function (e) {
                let marker_id = marker["icon"]["imageDiv"]["id"]
            });
        }

        add_marker(lon, lat, listing_id) {
            let position = new OpenLayers.LonLat(lon, lat).transform(this.fromProjection, this.toProjection);
            let marker = new OpenLayers.Marker(position);
            this.markers.addMarker(marker);

            marker.events.register("click", marker, function (e) {
                href_jump(listing_id);

                try {
                    let selected_marker = document.getElementById("selected_marker")
                    selected_marker.id = selected_marker.tmp
                    selected_marker.src = "../resources/OpenLayers-2.13.1/img/marker.png"
                } catch (e) {
                }
                let marker_id = marker["icon"]["imageDiv"]["id"]
                document.getElementById(marker_id + "_innerImage").src = "../resources/OpenLayers-2.13.1/img/marker-green.png"
                document.getElementById(marker_id + "_innerImage").tmp = marker_id + "_innerImage"
                document.getElementById(marker_id + "_innerImage").id = "selected_marker"
            });
        }
        set_position(lon, lat) {
            var position = new OpenLayers.LonLat(lon, lat).transform(this.fromProjection, this.toProjection);
            this.map.setCenter(position, this.zoom);
        }

        single_click() {
            let is_first = true;
            let clicked_val =
                OpenLayers.Control.Click = OpenLayers.Class(OpenLayers.Control, {
                    defaultHandlerOptions: {
                        'single': true,
                        'double': false,
                        'pixelTolerance': 0,
                        'stopSingle': false,
                        'stopDouble': false
                    },
                    initialize: function (options) {
                        this.handlerOptions = OpenLayers.Util.extend(
                            {}, this.defaultHandlerOptions
                        );
                        OpenLayers.Control.prototype.initialize.apply(
                            this, arguments
                        );
                        this.handler = new OpenLayers.Handler.Click(
                            this, {
                            'click': this.trigger
                        },
                            this.handlerOptions
                        );
                    },

                    trigger: function (e) {
                        var lonlat = this.map.getLonLatFromViewPortPx(e.xy)
                        lonlat.transform(
                            new OpenLayers.Projection("EPSG:900913"),
                            new OpenLayers.Projection("EPSG:4326")
                        );
                        if (is_first) {
                            is_first = false;
                        } else {
                        }
                    }
                });
            var click = new OpenLayers.Control.Click();
            this.map.addControl(click);
            click.activate();
        }
    }
    var instance;
    return {
        getInstance: function () {
            if (instance == null) {
                instance = new SingletonClass();
                instance.constructor = null;
            }
            return instance;
        }
    };
})();


async function get_user_position(cb) {
    const JELACIC = {
        lat: 45.813138,
        lon: 15.977264
    };
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                cb(position.coords.longitude,
                    position.coords.latitude);
            },
            () => {
                cb(JELACIC.lon, JELACIC.lat);
            }
        );
    } else {
        cb(JELACIC.lon, JELACIC.lat);
    }
}

async function set_position() {
    get_user_position((lon, lat) => {
        let map_inst = SingletonFactory.getInstance();
        map_inst.add_user_marker(lon, lat);

    })
}

