import { createStore } from 'vuex'

// this.$store.dispatch(action, value);
// let curr = this.$store.getters[variable];


export const store = createStore({
    state() {
        return {
            // count: 0,
            // synchronizerToken: "",

            // user lon lat
            // latitude: 0,
            // longitude: 0,

            // todo where is this used? navbar?
            // username: "username_template",

            // todo, this is in .env
            appMode: "development",

            clickedLocation: undefined,
          

            portfolios: {},
            map: undefined,

            location: undefined,

            charts: [],

            zoomUserLocation: false,

            // user coordinates
            userCoordiantes: {},
     synchronizerToken: "",
 username: "",
        }
    },
    actions: {
setUserCoordinates(context, userCoordiantes) {
    context.commit("SET_USER_COORDINATES", userCoordiantes);
  
},
setSynchronizerToken(context, synchronizerToken) {
    context.commit("SET_SYNCHRONIZER_TOKEN", synchronizerToken); 
},
setUsername(context, username) {
    context.commit("SET_USERNAME", username);
},
        setMap(context, map) {
            context.commit("setMap", map);
        },
        setPortfolios(context, portfolios) {
            context.commit("setPortfolios", portfolios);
        },
        setZoomUserLocation(context, zoomUserLocation) {
            context.commit("SET_ZOOM_USER_LOCATION", zoomUserLocation);
        },
        setClickedLocation(context, clickedLocation) {
            context.commit("SET_CLICKED_LOCATION", clickedLocation);

        }

    },
    mutations: {
        SET_USER_COORDINATES(context, userCoordiantes) {
            context.userCoordiantes = userCoordiantes;
        },
        SET_USERNAME(context, username){
            context.username = username;

        },


        SET_SYNCHRONIZER_TOKEN(state, synchronizerToken) {
state.synchronizerToken = synchronizerToken;
        },
        SET_ZOOM_USER_LOCATION(state, zoomUserLocation) {
            state.zoomUserLocation = zoomUserLocation
        },
        SET_CLICKED_LOCATION(state, clickedLocation) {
            state.clickedLocation = clickedLocation;
        },


   
        // setLatitude(state, newValue) {
        //     state.latitude = newValue
        // },
        // setLongitude(state, newValue) {
        //     state.longitude = newValue
        // },
    

        setMap(state, map) {
            state.map = map;
        },
        setPortfolios(state, portfolios) {
            state.portfolios = portfolios;
        }

        ,

        selectLocation(state, location) {
            console.log("selecting location", location)
            state.location = location;
        },

        addChart(state, chart) {
            console.log("adding chart")
            state.charts.push(chart);
        }


    },
    getters: {
coordiantes(state) {
return state.coordiantes
},
synchronizerToken(state) {
    return state.synchronizerToken;
},
username(state) {
return state.username;
},

        map(state) {
            return state.map;
        },

        portfolios(state) {
            return state.portfolios;
        },

        location(state){
            return state.location;
        },
        charts(state) {
            return state.charts;
        },
        zoomUserLocation(state) {
            return state.zoomUserLocation;
        } ,
        clickedLocation(state) {
            return state.clickedLocation;
        }
        // selectedPortfolio(state) {
        //     return state.selectedPortfolio;
        // }
    }

})


