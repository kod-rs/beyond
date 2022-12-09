import { Middleware } from 'redux';

import { RootState } from '../store';

/**
 * It takes a store, returns a function that takes a next function, which returns a function that takes
 * an action, which returns a function that logs the action type, payload, current state, and next
 * state
 * @param store - The store instance.
 * @returns A function that takes a store and returns a function that takes a next and returns a
 * function that takes an action and returns a function that takes a store and returns a function that
 * takes a next and returns a function that takes an action and returns a function that takes a store
 * and returns a function that takes a next and returns a function that takes an action and returns a
 * function that takes a store and returns
 */
export const loggerMiddleware: Middleware<{}, RootState> =
  (store) => (next) => (action) => {
    if (!action.type) {
      return next(action);
    }

    console.log('type: ', action.type);
    console.log('payload: ', action.payload);
    console.log('currentState: ', store.getState());

    next(action);

    console.log('next state: ', store.getState());
  };
