import React, { Fragment, useState, useEffect, useRef } from "react";
/*=============================================
        =       COMPONENTE TARJETA          =
  =============================================*/

const Tarjetas = (props) => {
  console.log({ dfadsfdsf: props.income });
  const incomes = props.income;
  let totalBencina;
  let totalAceite;
  let totalPresion;
  let totalLavado;
  if (incomes.length) {
    const bencina = incomes.filter((x) => x.service_name.includes("bencina"));

    const amountBencima = bencina.reduce(
      (total, fuel) => total + fuel.total_maintenance_cost,
      0
    );
    totalBencina = amountBencima.toLocaleString("es-CL", {
      style: "currency",
      currency: "CLP",
    });
    console.log({ amountBencima });
    const aceite = incomes.filter((x) => x.service_name.includes("aceite"));
    const amountAceite = aceite.reduce(
      (total, fuel) => total + fuel.total_maintenance_cost,
      0
    );
    totalAceite = amountAceite.toLocaleString("es-CL", {
      style: "currency",
      currency: "CLP",
    });
    console.log({ aceite: amountAceite });
    const presion = incomes.filter((x) => x.service_name.includes("presion"));
    const amountPresion = presion.reduce(
      (total, fuel) => total + fuel.total_maintenance_cost,
      0
    );
    console.log({ presion: amountPresion });
    totalPresion = amountPresion.toLocaleString("es-CL", {
      style: "currency",
      currency: "CLP",
    });
    const lavado = incomes.filter((x) => x.service_name.includes("lavado"));
    const amountLavado = lavado.reduce(
      (total, fuel) => total + fuel.total_maintenance_cost,
      0
    );
    totalLavado = amountLavado.toLocaleString("es-CL", {
      style: "currency",
      currency: "CLP",
    });
  }
  console.log({ bencina: totalBencina });
  console.log({ aceite: totalAceite });

  return (
    <>
      <div className="col-md-3">
        <div className="card">
          <div className="card bg-dark text-center">
            <h4 className="card-title">
              <span className="badge badge-secondary">Bencina</span>
            </h4>
            <h3 className="card-text text-white"> {totalBencina}</h3>
          </div>
        </div>
      </div>
      <div className="col-md-3">
        <div className="card">
          <div className="card bg-success text-center">
            <h4 className="card-title ">
              <span className="badge badge-secondary">Aceite</span>
            </h4>
            <b>
              <h3 className="card-text text-white">{totalAceite}</h3>
            </b>
          </div>
        </div>
      </div>
      <div className="col-md-3">
        <div className="card">
          <div className="card bg-primary text-center">
            <h4 className="card-title">
              <span className="badge badge-secondary">Presión</span>
            </h4>
            <h3 className="card-text text-white">{totalPresion}</h3>
          </div>
        </div>
      </div>
      <div className="col-md-3">
        <div className="card">
          <div className="card bg-warning text-center">
            <h4 className="card-title">
              <span className="badge badge-secondary">Lavado</span>
            </h4>
            <h3 className="card-text text-dark">{totalLavado}</h3>
          </div>
        </div>
      </div>
    </>
  );
};

export default Tarjetas;
