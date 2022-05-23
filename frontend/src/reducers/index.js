import { combineReducers } from "redux";
import messageReducer from "./messageReducer";
import buttonReducer from "./buttonReducer";
import fleetReducer from "./fleetReducer";

export default combineReducers({
  messageReducer,
  buttonReducer,
  fleetReducer,
});
