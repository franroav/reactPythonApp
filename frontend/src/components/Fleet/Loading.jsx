import React, { Fragment, useState, useEffect, useRef } from "react";
/*=============================================
        =       COMPONENTE LOADING          =
  =============================================*/
const Loading = () => {
  return (
    <>
      <div className="spinner-grow text-primary" role="status">
        <span className="visually-hidden"></span>
      </div>
      <div className="spinner-grow text-secondary" role="status">
        <span className="visually-hidden"></span>
      </div>
      <div className="spinner-grow text-success" role="status">
        <span className="visually-hidden"></span>
      </div>
      <div className="spinner-grow text-danger" role="status">
        <span className="visually-hidden"></span>
      </div>
      <div className="spinner-grow text-warning" role="status">
        <span className="visually-hidden"></span>
      </div>
      <div className="spinner-grow text-info" role="status">
        <span className="visually-hidden"></span>
      </div>
      <div className="spinner-grow text-light" role="status">
        <span className="visually-hidden"></span>
      </div>
      <div className="spinner-grow text-dark" role="status">
        <span className="visually-hidden"></span>
      </div>
      <h3>espere porfavor estamos cargando el dashboard...</h3>
    </>
  );
};

export default Loading;
