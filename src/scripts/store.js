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
        setLatitude(state, newValue) {
            console.log("set lat")
            state.latitude = newValue
        },
        setLongitude(state, newValue) {
            console.log("sta lon")
            state.longitude = newValue
        }

    },
    // getters: {
    //     getSynchronizerToken(state) {
    //         return 
    //     }
    // }
})

