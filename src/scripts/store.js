import { createStore } from 'vuex'

export const store = createStore({
    state() {
        return {
            count: 0,
            synchronizerToken: ""
        }
    },
    mutations: {
        increment(state) {
            state.count++
        },
        setSynchronizerToken(state, newValue) {
            state.synchronizerToken = newValue;
        }
    },
    // getters: {
    //     getSynchronizerToken(state) {
    //         return 
    //     }
    // }
})

