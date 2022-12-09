import { compose, createStore, applyMiddleware, Middleware } from 'redux';
import { persistStore, persistReducer, PersistConfig } from 'redux-persist';
import storage from 'redux-persist/lib/storage';
import logger from 'redux-logger';
import createSagaMiddleware from 'redux-saga';

import { rootSaga } from './root-saga';

import { rootReducer } from './root-reducer';

export type RootState = ReturnType<typeof rootReducer>;

/* Declaring the global window object and adding a property to it. */
declare global {
  interface Window {
    __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: typeof compose;
  }
}

type ExtendedPersistConfig = PersistConfig<RootState> & {
  whitelist: (keyof RootState)[];
};

/* Creating a persistConfig object that is used to create the persistedReducer object. */
const persistConfig: ExtendedPersistConfig = {
  key: 'root',
  storage,
  whitelist: [],
};

/* Creating a sagaMiddleware object. */
const sagaMiddleware = createSagaMiddleware();

/* Creating a persistedReducer object that is used to create the store. */
const persistedReducer = persistReducer(persistConfig, rootReducer);

/* Creating an array of middlewares. If the environment is not production, it will add the logger
middleware to the array. It will always add the sagaMiddleware to the array. It will then filter the
array to remove any falsy values. */
const middleWares = [
  process.env.NODE_ENV !== 'production' && logger,
  sagaMiddleware,
].filter((middleware): middleware is Middleware => Boolean(middleware));

/* Checking if the environment is not production and if the window object exists and if the window
object has the __REDUX_DEVTOOLS_EXTENSION_COMPOSE__ property. If it does, it will use that property
to compose the enhancers. If it doesn't, it will use the compose function. */
const composeEnhancer =
  (process.env.NODE_ENV !== 'production' &&
    window &&
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__) ||
  compose;

/* Creating a composedEnhancers object that is used to create the store. */
const composedEnhancers = composeEnhancer(applyMiddleware(...middleWares));

/* Creating a store object. */
export const store = createStore(
  persistedReducer,
  undefined,
  composedEnhancers
);

/* Running the rootSaga. */
sagaMiddleware.run(rootSaga);

/* Creating a persistor object that is used to persist the store. */
export const persistor = persistStore(store);
