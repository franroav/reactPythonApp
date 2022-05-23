import { DECREASE, INCREASE } from '../actions/types';
import { createReducer, Types as ReduxSauceTypes } from 'reduxsauce';

const INITIAL_STATE  = {
  counter: 0
}

const increaseCounter = (state = INITIAL_STATE, action) => ({
    ...state,
    counter: state.counter + 10,
});

const decreaseCounter = (state = INITIAL_STATE, action) => ({
    ...state,
    counter: state.counter - 10,
});


const HANDLERS = {
  [INCREASE]: increaseCounter,
  [DECREASE]: decreaseCounter,
  
  [ReduxSauceTypes.DEFAULT]: state => state
}

export default createReducer(INITIAL_STATE, HANDLERS);