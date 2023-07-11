import { takeLatest, put, all, call } from 'redux-saga/effects';
import { BUILDINGS_ACTION_TYPES } from './buildings.types';

import {
    getBuildingsSuccess,
    getBuildingsFailed, 
    setIsLoadingBuildings,
} from './buildings.action';

import {
    getBuildingsForUser,
} from '../../utils/api/api.utils';

/* A generator function that is called by the saga middleware. It is a generator function that is
called by the saga middleware. */
export function* getBuildingsForCurrentUser({ payload: { user } }) {
    try {
        yield put(setIsLoadingBuildings(true));
        let buildingsWrapper = yield call(
            getBuildingsForUser,
            user
        );
        if (buildingsWrapper) {
            let colors = generateRandomColors(buildingsWrapper.buildings.length);
            buildingsWrapper.buildings.forEach((element, index) => {
                element.color = colors[index];
            });
            yield put(getBuildingsSuccess(buildingsWrapper.buildings));
        } else {
            yield put(getBuildingsFailed("Buildings for user " + user.displayName + " were null!"));
        }
    } catch (error) {
        yield put(getBuildingsFailed(error));
    }
}

/* A function that generates "n" random colors */
function generateRandomColors(n) {
    var colors = [];
  
    while (colors.length < n) {
      var color = generateRandomColor();
  
      if (!colors.includes(color)) {
        colors.push(color);
      }
    }
  
    return colors;
  }

/* A function that generates random color */
function generateRandomColor() {
var webSafeColors = [
  "#800000", "#e6194B", "#f58231", "#ffe119", "#bfef45", "#42d4f4",
  "#911eb4", "#f032e6", "#469990", "#9A6324", "#3cb44b", "#4363d8",
  "#FF33FF", "#FFFF00"
];

var randomIndex = Math.floor(Math.random() * webSafeColors.length);
return webSafeColors[randomIndex];
}

/* A generator function that is called by the saga middleware. It is a generator function that is
called by the saga middleware.*/
export function* onGetBuildingsStart() {
    yield takeLatest(BUILDINGS_ACTION_TYPES.GET_BUILDINGS_START, getBuildingsForCurrentUser);
}

/* This is the root saga. It is the saga that is exported to the store. It is the saga that is run by
the saga middleware. */
export function* buildingsSagas() {
    yield all([
        call(onGetBuildingsStart),
    ]);
}
