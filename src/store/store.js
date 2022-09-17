import { createStore } from 'vuex'

// this.$store.dispatch(action, value);
// let curr = this.$store.getters[variable];


export const store = createStore({
    state() {
        return {
            // count: 0,
            synchronizerToken: "",

            // user lon lat
            latitude: 0,
            longitude: 0,

            // todo where is this used? navbar?
            username: "username_template",

            // todo, this is in .env
            appMode: "development",

            clickedLocation: undefined,
          

            portfolios: {},
            map: undefined,

            location: undefined,

            charts: [],

            zoomUserLocation: false,
        }
    },
    actions: {
        // this.$store.dispatch("setZoomUserLocation", isSelected);

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
        SET_ZOOM_USER_LOCATION(state, zoomUserLocation) {
            state.zoomUserLocation = zoomUserLocation
        },
        SET_CLICKED_LOCATION(state, clickedLocation) {
            state.clickedLocation = clickedLocation;
        },


        // increment(state) {
        //     state.count++;
        // },
        // UPDATE_PORTFOLIO_COLOUR(state, pl) {
        //     state.portfolios[pl.portfolioName]["colour"] = pl.colourName
        // },

        setSynchronizerToken(state, newValue) {
            state.synchronizerToken = newValue;
        },
        setLatitude(state, newValue) {
            state.latitude = newValue
        },
        setLongitude(state, newValue) {
            state.longitude = newValue
        },
        setUsername(state, username) {
            state.username = username
        },


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


