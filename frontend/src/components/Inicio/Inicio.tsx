import React, { Fragment } from "react";
import "./Inicio.css";

function Inicio(): JSX.Element {
  return (
    <Fragment>
      <div className="card">
        <div className="card-header">
          <div className="card-title">
            <h1>Bienvenidos!</h1>
          </div>
        </div>
        <div className="card-body">
          porfavor haga click en el boton Flota, para navegar por la aplicación,
          muchas gracias!
        </div>
      </div>
    </Fragment>
  );
}
export default Inicio;
