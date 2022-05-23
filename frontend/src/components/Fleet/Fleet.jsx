import {
  getServiceTopten,
  getServiceCount,
  getServiceCost,
} from "../../actions/fleetActions";
import "./Fleet.css";
import MaterialTable from "material-table";
import { Card } from "@material-ui/core";
import React, { Fragment, useState, useEffect, useRef } from "react";
import { connect } from "react-redux";
import { useHistory } from "react-router-dom";
import ChartBar from "./BarChart";
import Loading from "./Loading";
import Tarjetas from "./Tarjeta";

/*=============================================
        =       COMPONENTE FLEET          =
  =============================================*/

const Fleet = ({
  getServiceTopten,
  getServiceCount,
  getServiceCost,
  fleetReducer,
}) => {
  const [searchInReducer, setSearchInReducer] = useState(false);
  const { servicetopten, servicedemand, serviceincome } = fleetReducer;
  const [searchInChart, setSearchInChart] = useState(false);
  const history = useHistory();
  const listofTopTen = [];
  const listofIncome = [];
  const listofDemand = [];

  const columns = [
    {
      title: "Nombre servicio",
      field: "service_name",
      render: (rowData) => (
        <span className="badge badge-secondary">
          <i className="fa fa-gear pr-2 fa-spin"> </i> {rowData.service_name}
        </span>
      ),
    },
    {
      title: "$ Costo Mantenimiento",
      field: "total_maintenance_cost",
      render: (rowData) => (
        <span class="badge badge-primary">
          {rowData.total_maintenance_cost}
          <i className="fa fa-info-circle pl-2"> </i>
        </span>
      ),
    },
    {
      title: "$ Costo Mant. Mes anterior",
      field: "total_maintenance_cost_previous_month",
      render: (rowData) => (
        <small>
          <p className="text-lead">
            {rowData.total_maintenance_cost_previous_month.toLocaleString(
              "es-CL",
              {
                style: "currency",
                currency: "CLP",
              }
            )}
          </p>
        </small>
      ),
    },
    {
      title: "Fecha",
      field: "amount",
      render: (rowData) => (
        <small>
          <p className="text-lead">
            {rowData.actual_month + "-" + rowData.year}
          </p>
        </small>
      ),
    },
  ];

  if (searchInReducer) {
    console.log({ servicetopten });
    console.log({ servicedemand });
    console.log({ serviceincome });
    if (servicetopten !== undefined && servicetopten.length) {
      for (const topten of servicetopten) {
        listofTopTen.push({
          ...topten,
        });
      }
    }
    if (serviceincome !== undefined && serviceincome.length) {
      for (const income of serviceincome) {
        listofIncome.push({
          ...income,
        });
      }
    }
    if (servicedemand !== undefined && servicedemand.length) {
      for (const demand of servicedemand) {
        listofDemand.push({
          ...demand,
        });
      }
    }

    if (servicedemand.length && serviceincome.length && servicetopten.length) {
      setTimeout(() => {
        setSearchInChart(true);
      }, 3000);
    }
  } else {
    console.log("aun no hay data");
  }

  const userDetails = (row, caso) => {
    //history.push(`/service/${row.service_name}`);
  };
  useEffect(() => {
    const loadData = async () => {
      await getServiceTopten();
      await getServiceCount();
      await getServiceCost();
      setSearchInReducer(true);
    };

    loadData();
  }, [getServiceTopten]);

  if (searchInChart) {
    return (
      <Fragment>
        <section>
          <div className="container mb-5">
            <div className="row">
              <h3 className="text-center">Ingreso Mensual</h3>
            </div>
            <div className="row">
              <Tarjetas income={listofIncome} />
            </div>
          </div>
        </section>
        <section>
          <div className="container mb-5">
            <div className="row">
              <h3 className="text-center">Cantidad de servicios por mes</h3>
            </div>
            <div className="row">
              <div className="col-md-8">
                <ChartBar demand={listofDemand} />
              </div>
            </div>
          </div>
        </section>
        {/*MATERIAL TABLE -> 10 servicios más costosos*/}
        <section>
          <div className="row mt-5 material-table">
            <div className="col-md-8 offset-md-2">
              <Card>
                <MaterialTable
                  columns={columns}
                  data={listofTopTen}
                  title="10 servicios más costosos"
                  actions={[
                    {
                      //icon: "remove_red_eye",
                      icon: "remove_red_eye",
                      tooltip: "ver servicio",
                      onClick: (event, rowData) => userDetails(rowData, "view"),
                    },
                  ]}
                  options={{
                    actionsColumnIndex: -1,
                    filtering: true,
                    sorting: true,
                    exportButton: true,
                    fixedColumns: {
                      left: 1,
                      right: 0,
                    },
                  }}
                  localization={{
                    header: {
                      actions: "Acciones",
                    },
                  }}
                />
              </Card>
            </div>
          </div>
        </section>
      </Fragment>
    );
  } else {
    return (
      <>
        <Loading />
      </>
    );
  }
};

const mapStateProps = ({ fleetReducer, buttonReducer }) => ({
  fleetReducer,
  buttonReducer,
});

export default connect(mapStateProps, {
  getServiceTopten,
  getServiceCount,
  getServiceCost,
})(Fleet);
