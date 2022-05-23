import { INCREASE, DECREASE } from "./types";

const increaseButton = (counter) => (dispatch) => {
  dispatch(setIncrease());
};
const decreaseButton = (counter) => (dispatch) => {
  dispatch(setDecrese());
};
export { increaseButton, decreaseButton };

const setIncrease = (counter) => ({
  type: INCREASE,
});
const setDecrese = (counter) => ({
  type: DECREASE,
});
