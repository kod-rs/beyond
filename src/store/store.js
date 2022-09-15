import { createStore } from 'vuex'

export const store = createStore({
    state() {
        return {
            // count: 0,
            synchronizerToken: "",

            // user lon lat
            latitude: 0,
            longitude: 0,

            // todo where is this used? navbar?
            username: "",

            // todo, this is in .env
            appMode: "development",

            // selectedPortfolio: { "id": -1 },
            // selectedPortfolio: createEmptyPortfolio(),
            // nextId: 1

            portfolios: {},
            map: undefined,

            location: undefined,

            charts: [],
        }
    },
    actions: {
        setMap(context, map) {
            context.commit("setMap", map);
        },
        setPortfolios(context, portfolios) {
            context.commit("setPortfolios", portfolios);
        },

        // updatePortfolioColour(context, pl) {
        //     context.commit("UPDATE_PORTFOLIO_COLOUR", pl);
        // },
        // addPortfolio(context, portfolio) {
        //     context.commit("ADD_PORTFOLIO", portfolio);
        // },
        // selectPortfolio(context, portfolio) {
        //     context.commit("SELECT_PORTFOLIO", portfolio);
        // },
        // deletePortfolio(context, name) {
        //     context.commit("DELETE_PORTFOLIO", name);

        // },
        // updatePortfolio(context, portfolio) {
        //     context.commit("UPDATE_PORTFOLIO", portfolio);
        // }
    },
    mutations: {
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



        // ADD_PORTFOLIO(state, portfolio) {
        //     // portfolio.id = state.nextId++;
        //     state.portfolios[portfolio.name] = portfolio;
        //     // state.portfolios.push(portfolio);
        //     state.selectedPortfolio = portfolio;
        // },
        // SELECT_PORTFOLIO(state, portfolio) {
        //     state.selectedPortfolio = portfolio;
        // },
        // DELETE_PORTFOLIO(state, id) {
        //     delete state.portfolios[id];
        // },
        // UPDATE_PORTFOLIO(state, portfolio) {
        //     console.log("todo", state, portfolio)
        // }

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
        // selectedPortfolio(state) {
        //     return state.selectedPortfolio;
        // }
    }

})


