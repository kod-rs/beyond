import { createStore } from 'vuex'

// state : development / production

function createEmptyPortfolio() {
    return {
        id: -1,
        name: ""
    };
}

export const store = createStore({
    state() {
        return {
            count: 0,
            synchronizerToken: "",
            latitude: 0,
            longitude: 0,
            username: "",
            appMode: "development",

            portfolios: [],
            selectedPortfolio: createEmptyPortfolio(),
            nextId: 1

        }
    },
    actions: {
        addPortfolio(context, portfolio) {
            context.commit("ADD_PORTFOLIO", portfolio);
        },
        selectPortfolio(context, portfolio) {
            context.commit("SELECT_PORTFOLIO", portfolio);
        },
        deletePortfolio(context, id) {
            context.commit("DELETE_PORTFOLIO", id);

        },
        updatePortfolio(context, portfolio) {
            context.commit("UPDATE_PORTFOLIO", portfolio);
        }
    },
    mutations: {
        increment(state) {
            state.count++;
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
            portfolio.id = state.nextId++;
            state.portfolios.push(portfolio);
            state.selectedPortfolio = portfolio;
        },
        SELECT_PORTFOLIO(state, portfolio) {
            state.selectedPortfolio = portfolio;
        },
        DELETE_PORTFOLIO(state, id) {
            if (state.selectedPortfolio.id == id) {
                state.selectedPortfolio = createEmptyPortfolio();
            }
            state.portfolios = state.portfolios.filter(p => p.id != id);
        },
        UPDATE_PORTFOLIO(state, portfolio) {
            var store_p = state.portfolios.find(p => p.id == portfolio.id);
            if (store_p != null) {
                store_p.name = portfolio.name;
            }
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


