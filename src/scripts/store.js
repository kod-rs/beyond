import { createStore } from 'vuex'

export const store = createStore({
    state() {
        return {
            count: 0,
            synchronizerToken: "",
            latitude: 0,
            longitude: 0
        }
    },
    mutations: {
        increment(state) {
            state.count++;

        },
        setSynchronizerToken(state, newValue) {
            state.synchronizerToken = newValue;
        },
        latitude(state, newValue) {
            state.latitude = newValue
        },
        longitude(scripts, newValue) {
            store.longitude = newValue
        }

    },
    // getters: {
    //     getSynchronizerToken(state) {
    //         return 
    //     }
    // }
})

