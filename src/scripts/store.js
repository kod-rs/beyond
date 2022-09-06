import { createStore } from 'vuex'

// state : development / production

// function createEmptyPortfolio() {
//     return {
//         id: -1,
//         name: "",
//         colour: "tmp colour"
//     };
// }

// function deleteFromDict(key) {
//     if (this.hasKey(key)) {
//         delete this.container[key];
//         return true;
//     }
//     return false;
// }

export const store = createStore({
    state() {
        return {
            count: 0,
            synchronizerToken: "",
            latitude: 0,
            longitude: 0,
            username: "",
            appMode: "development",

            portfolios: {},
            selectedPortfolio: { "id": -1 }
            // selectedPortfolio: createEmptyPortfolio(),
            // nextId: 1

        }
    },
    actions: {
        updatePortfolioColour(context, pl) {
            context.commit("UPDATE_PORTFOLIO_COLOUR", pl);
        },
        addPortfolio(context, portfolio) {
            context.commit("ADD_PORTFOLIO", portfolio);
        },
        selectPortfolio(context, portfolio) {
            context.commit("SELECT_PORTFOLIO", portfolio);
        },
        deletePortfolio(context, name) {
            context.commit("DELETE_PORTFOLIO", name);

        },
        updatePortfolio(context, portfolio) {
            context.commit("UPDATE_PORTFOLIO", portfolio);
        }
    },
    mutations: {
        increment(state) {
            state.count++;
        },
        UPDATE_PORTFOLIO_COLOUR(state, pl) {
            state.portfolios[pl.portfolioName]["colour"] = pl.colourName
        },

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

        ADD_PORTFOLIO(state, portfolio) {
            // portfolio.id = state.nextId++;
            state.portfolios[portfolio.name] = portfolio;
            // state.portfolios.push(portfolio);
            state.selectedPortfolio = portfolio;
        },
        SELECT_PORTFOLIO(state, portfolio) {
            state.selectedPortfolio = portfolio;
        },
        DELETE_PORTFOLIO(state, id) {
            delete state.portfolios[id];
        },
        UPDATE_PORTFOLIO(state, portfolio) {
            console.log("todo", state, portfolio)
        }

    },
    getters: {
        portfolios(state) {
            return state.portfolios;
        },
        selectedPortfolio(state) {
            return state.selectedPortfolio;
        }
    }

})


