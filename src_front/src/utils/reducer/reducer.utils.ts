import { AnyAction } from 'redux';

type Matchable<AC extends () => AnyAction> = AC & {
  type: ReturnType<AC>['type'];
  match(action: AnyAction): action is ReturnType<AC>;
};

/* Saying that the function takes a generic type AC that extends a function that returns an AnyAction
and has a type property of type string. It returns a Matchable type. */
export function withMatcher<AC extends () => AnyAction & { type: string }>(
  actionCreator: AC
): Matchable<AC>;

/* Saying that the function takes a generic type AC that extends a function that returns an AnyAction
and has a type property of type string. It returns a Matchable type. */
export function withMatcher<
  AC extends (...args: any[]) => AnyAction & { type: string }
>(actionCreator: AC): Matchable<AC>;

/**
 * It takes an action creator function and returns a new action creator function that has a `match`
 * method
 * @param {Function} actionCreator - A function that returns an action object.
 * @returns An object with the same properties as the actionCreator function, but with an additional
 * property called match.
 */
export function withMatcher(actionCreator: Function) {
  const type = actionCreator().type;
  return Object.assign(actionCreator, {
    type,
    match(action: AnyAction) {
      return action.type === type;
    },
  });
}

/**
 * ActionWithPayload is a type that takes two generic types, T and P, and returns an object with a type
 * property of type T and a payload property of type P.
 * @property {T} type - The type of the action.
 * @property {P} payload - P -&gt; The payload is the data that is being passed to the reducer.
 */
export type ActionWithPayload<T, P> = {
  type: T;
  payload: P;
};

/**
 * Action is a type that takes a type parameter T and is an object with a type property of type T.
 * @property {T} type - T;
 */
export type Action<T> = {
  type: T;
};

/* Saying that if the payload is not void, then the return type is ActionWithPayload<T, P> */
export function createAction<T extends string, P>(
  type: T,
  payload: P
): ActionWithPayload<T, P>;

/* A type guard. It is saying that if the payload is void, then the return type is Action<T> */
export function createAction<T extends string>(
  type: T,
  payload: void
): Action<T>;

/**
 * It takes a string and a payload and returns an object with the string as the type and the payload as
 * the payload
 * @param {T} type - T
 * @param {P} payload - P
 * @returns An object with a type and payload property.
 */
export function createAction<T extends string, P>(type: T, payload: P) {
  return { type, payload };
}
