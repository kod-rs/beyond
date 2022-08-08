onsole.log("hello from display_locations.js");

let map;

// koristi se u drop_down_activators
let formCheckoutToggleEnabled = false;

const JELACIC = { 
    lat: 45.813138, 
    lng: 15.977264
};

var userLocation = JELACIC;

// closest
var prozor;

// za generic
var infoWindow;

let locations;

// lokacija koja je pritisnuta na karti,
// koristi se u html_writers
let current_selected;


let markers = [];

var closestParking;
var distanceToClosestParking;


function display_locations() {
    console.log("display_locations/ display_locations")

    // Create XHR Object
    var xhr = new XMLHttpRequest();
 
    // OPEN - type, url/file, async
    xhr.open('GET', 'user/test', true);

    // OPTIONAL - used for loaders
    // xhr.onprogress = function(){
    // }

    xhr.onload = function(){

      if(this.status == 200){

        parkings = JSON.parse(this.responseText);

        formatted_locations = []

        for (var i  = 0 ; i < parkings.length; i++) {

            temp = {
                lat: parseFloat(parkings[i].lokacija.geosirina), 
                lng: parseFloat(parkings[i].lokacija.geoduzina),
                NumEmpty : parseFloat(parkings[i].brojslobmjesta)
            }

            // addParkingMarker(
            //    temp,
            //     map
            // );

            formatted_locations.push(temp);

        }

        locations = formatted_locations;

         
        for (let i = 0; i < locations.length; i++) {
            console.log(locations[i]);

            addParkingMarker(
                locations[i],
                map
            );
        }
       
      } else if(this.status = 404){

        console.log("not found");
        
      }

    }

    xhr.onerror = function(){
      console.log('Request Error...');
    }

    xhr.send();

}

// postavlja sve parkiralisne povrsine na kartu
// pozicionira korisnika na njegovu lokaciju ili na @JELACIC
async function initMap() {
    console.log("display_locations/ initMap")

    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 12,
        center: userLocation,
    });

    prozor = new google.maps.InfoWindow();
    infoWindow =  new google.maps.InfoWindow();

    // centriranje na lokaciju kompjutera ako je dopusteno lociranje 
    // stavljanje taga "vi ste ovdje!" na tu lokaciju
    if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(

            (position) => {

                userLocation = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };

                new google.maps.Marker({
                    position: userLocation,
                    map: map,
                });
            
                map.setCenter(userLocation);
            
            },
        
            () => {
                // TODO
                console.log("nije dat pristup lokaciji")

                userLocation = JELACIC;

                new google.maps.Marker({
                    position: userLocation,
                    map: map,
                });

            }

        );

    } 

    display_locations();

}

// dodavanje markera s ikonom slova P
function addParkingMarker(location, map) {
    console.log("display_locations/ addParkingMarker");

    var marker = new google.maps.Marker({
        position:  location,
        icon: "https://developers.google.com/maps/documentation/javascript/examples/full/images/parking_lot_maps.png",
        map: map,
    });

    google.maps.event.addListener(marker, 'click', function(){

        var distance = parseInt(calculateDistanceBetweenPoints(userLocation,
            location.lat, location.lng));

        current_selected = location;


        let dodatak = "";

        try {
                    checkoutFormWriter(location);

        } catch(error) {
            console.log("checkoutformwriter ne postoji");
            console.log("valjda smo na main pageu");
            dodatak = "broj slobodnih mjesta: " + location.NumEmpty + " <br> "
        }

      
        // infoWindow code
        infoWindow.close();
        prozor.close(); // Close previously opened infowindow
    
        if ( distance < 1000) {
            prozor.setContent(`<div id="prozor">${dodatak}${distance} m</div>`);
        } else {
            distance = +(distance / 1000).toFixed(1)
            prozor.setContent(`<div id="prozor">${dodatak}${distance} km</div>`);
        }

        prozor.open(map, marker);

    });

    markers.push(marker);

}

async function getClosestParking() {
    console.log("display_locations/ getClosestParking")

    // mora se opet pozvat da bi se radilo s aktualnim podatcima
    console.log(locations);

    closestParking = locations[0];
    
    distanceToClosestParking = calculateDistanceBetweenPoints(userLocation,
        closestParking.lat, closestParking.lng);
    

    var distance_ignoring_nine_spots_empty_filter = distanceToClosestParking;
    var closest_parking_ignoring_nine_spots_empty_filter = closestParking;
    var is_any_above_nine_spots = false;
    // sta ako su sva ispod 10 mjesta

    for (var i = 1; i < locations.length; i++) {

        console.log(locations[i]);

        let location = locations[i];

        console.log(location);

        var currDistance = calculateDistanceBetweenPoints(userLocation, location.lat,
            location.lng);

        if (location.NumEmpty >= 10) {
            is_any_above_nine_spots = true;

            if (distanceToClosestParking > currDistance) {
                closestParking = location;
                distanceToClosestParking = currDistance;
            }
        }   
    
        if (! is_any_above_nine_spots) {
            if (distance_ignoring_nine_spots_empty_filter > currDistance) {
                closest_parking_ignoring_nine_spots_empty_filter = location;
                distance_ignoring_nine_spots_empty_filter = currDistance;
            }
        }

    }
    prozor.close();
    infoWindow.close();

    if (is_any_above_nine_spots) {
        infoWindow.setPosition(closestParking); 
        current_selected = closestParking;
        
        checkoutFormWriter(closestParking);

    } else {   
        infoWindow.setPosition(closest_parking_ignoring_nine_spots_empty_filter);    
        current_selected = closest_parking_ignoring_nine_spots_empty_filter;
   
        checkoutFormWriter(closest_parking_ignoring_nine_spots_empty_filter);

    }

    infoWindow.setContent("najblizi parking");
    infoWindow.open(map);

}

// return: float: udaljenost u metrima izmedu lokacija
function calculateDistanceBetweenPoints(userLocation, locationLat, locationLng) {
    console.log("display_locations/ calculateDistanceBetweenPoints")
    var dLat = (locationLat - userLocation.lat) * Math.PI / 180;

    var dLong = (locationLng - userLocation.lng) * Math.PI / 180;
    
    var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) + 
        Math.cos((userLocation.lat) * Math.PI / 180) * Math.cos((locationLat) * Math.PI / 180) *
        Math.sin(dLong / 2) * Math.sin(dLong / 2);
    
    // 6378137 je radius zemlje za ovu mapu, razlikuje se od stvarnog ali je to ok
    // zato sto ova mapa ovako ocito funkcionira
    return 6378137 * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
}
