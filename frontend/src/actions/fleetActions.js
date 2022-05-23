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
} from "./types";
import {
  get_service_topten,
  get_service_count,
  get_service_cost,
  getById,
  create,
  update,
  deleteById,
} from "../services/fleet.service";
import Swal from "sweetalert2";

export const getServiceTopten = (fleets, element) => (dispatch) => {
  get_service_topten()
    .then((response) => {
      console.log({ topten: response });
      dispatch(fetchServiceTopTen(response));
    })
    .catch(() => {});
};

export const getServiceCount = (fleets, element) => (dispatch) => {
  get_service_count()
    .then((response) => {
      console.log({ count: response });
      dispatch(fetchServiceCount(response));
    })
    .catch(() => {});
};

export const getServiceCost = (fleets, element) => (dispatch) => {
  get_service_cost()
    .then((response) => {
      console.log({ cost: response });
      dispatch(fetchServiceCost(response));
    })
    .catch(() => {});
};

export const getOneFleet = (fleets, element) => (dispatch) => {
  getById()
    .then((response) => {
      dispatch(getOneFleetReducer(response));
    })
    .catch(() => {});
};

export const createOneFleet = (fleets, element) => (dispatch) => {
  console.log({ fleets, element });

  create(fleets)
    .then((response) => {
      console.log(response);
      if (response.error) {
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: `El correo ${fleets.email} ya se se encuentra registrado!`,
          footer:
            '<p class="text-lead"><small>porfavor intentelo nuevamente con otro correo, muchas gracias</small></p>',
        });
      }
      if (response.data) {
        dispatch(createFleetReducer(response));
        Swal.fire({
          position: "top-end",
          icon: "success",
          title: "El subscriptor ha sido guardado exitosamente!",
          showConfirmButton: false,
          timer: 1500,
        });
      }
    })
    .catch(() => {});
};

export const updateOneFleet = (fleets, element) => (dispatch) => {
  update()
    .then((response) => {
      dispatch(updateFleetReducer(response.data));
    })
    .catch(() => {});
};

export const deleteOneFleet = (fleets, element) => (dispatch) => {
  deleteById()
    .then((response) => {
      dispatch(deleteOneFleetReducer(response.data));
    })
    .catch(() => {});
};

const loadingIni = () => ({
  type: FLEET_LOADING,
});

const loadingOff = () => ({
  type: FLEET_LOADING_OFF,
});

const fetchServiceTopTen = (servicetopten) => ({
  type: GET_ALL_SERVICE_TOPTEN,
  servicetopten,
});

const fetchServiceCount = (servicedemand) => ({
  type: GET_ALL_SERVICE_COUNT,
  servicedemand,
});

const fetchServiceCost = (serviceincome) => ({
  type: GET_ALL_SERVICE_COST,
  serviceincome,
});

const createFleetReducer = (fleets) => ({
  type: CREATE_ONE_FLEET,
  fleets,
});
const updateFleetReducer = (fleets) => ({
  type: UPDATE_ONE_FLEET,
  fleets,
});

const getOneFleetReducer = (fleets) => ({
  type: GET_ONE_FLEET,
  fleets,
});

const deleteOneFleetReducer = (fleets) => ({
  type: DELETE_ONE_FLEET,
  fleets,
});
const resetData = () => ({
  type: RESET_FLEET_DATA,
});
