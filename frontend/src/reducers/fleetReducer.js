import { createReducer, Types as ReduxSauceTypes } from "reduxsauce";
import {
  GET_ALL_SERVICE_TOPTEN,
  GET_ALL_SERVICE_COUNT,
  GET_ALL_SERVICE_COST,
  GET_ONE_FLEET,
  DELETE_ONE_FLEET,
  UPDATE_ONE_FLEET,
  CREATE_ONE_FLEET,
  FLEET_LOADING,
  FLEET_LOADING_OFF,
  RESET_FLEET_DATA,
} from "../actions/types";

const INITIAL_STATE = {
  fleets: {},
  servicetopten: {},
  servicedemand: {},
  serviceincome: {},
  loading: false,
};

const getServiceTopTenReducer = (state, action) => {
  return {
    ...state,
    servicetopten: action.servicetopten,
  };
};

const getServiceCountReducer = (state, action) => {
  return {
    ...state,
    servicedemand: action.servicedemand,
  };
};

const getServiceCostReducer = (state, action) => {
  return {
    ...state,
    serviceincome: action.serviceincome,
  };
};
const getOneFleet = (state, action) => {
  return {
    ...state,
    fleets: action.fleets,
  };
};

const createFleet = (state, action) => {
  return {
    ...state,
    fleets: action.fleets,
  };
};
const updateFleet = (state, action) => {
  return {
    ...state,
    fleets: action.fleets,
  };
};
const deleteFleet = (state, action) => {
  return {
    ...state,
    fleets: action.fleets,
  };
};

const resetData = (state = INITIAL_STATE) => ({
  ...state,
  fleets: {},
});

const loadingIni = (state = INITIAL_STATE) => ({
  ...state,
  loading: true,
});

const loadingOff = (state = INITIAL_STATE) => ({
  ...state,
  loading: false,
});

const HANDLERS = {
  [GET_ALL_SERVICE_TOPTEN]: getServiceTopTenReducer,
  [GET_ALL_SERVICE_COUNT]: getServiceCountReducer,
  [GET_ALL_SERVICE_COST]: getServiceCostReducer,
  [GET_ONE_FLEET]: getOneFleet,
  [CREATE_ONE_FLEET]: createFleet,
  [UPDATE_ONE_FLEET]: updateFleet,
  [DELETE_ONE_FLEET]: deleteFleet,
  [FLEET_LOADING]: loadingIni,
  [FLEET_LOADING_OFF]: loadingOff,
  [RESET_FLEET_DATA]: resetData,

  [ReduxSauceTypes.DEFAULT]: (state) => state,
};

export default createReducer(INITIAL_STATE, HANDLERS);
