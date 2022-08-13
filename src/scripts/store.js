import { createStore } from 'vuex'

// state : development / production

export const store = createStore({
    state() {
        return {
            count: 0,
            synchronizerToken: "",
            latitude: 0,
            longitude: 0,
            username: "",
            appMode: "development"
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
        }

    }
})

