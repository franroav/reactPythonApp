import React, { Fragment } from "react";
import "./App.css";
import Nav from "./components/Nav/Nav";

// +  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
//const store = createStore(reducer, composeWithDevTools(applyMiddleware(thunk)));

function App(): JSX.Element {
  return (
      <Fragment>
        <Nav></Nav>
      </Fragment>
  );
}

export default App;
