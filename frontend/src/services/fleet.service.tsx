import axios from "axios";
//http://localhost:5000/api/subscription/register
const baseUrl = `http://localhost:8000/api/`;

const newGuestClient = async (body: any, code: string) => {
  try {
    return axios({
      method: "post",
      url: `http://localhost:5000/api/register/invite/${code}`,
      headers: {
        "Content-Type": "application/json",
      },
      data: JSON.stringify(body),
    }).then(
      (result) => {
        return result;
      },
      (error) => {
        console.log({ error: "Error: " + error.message });
        return { error: "Error: " + error.message };
      }
    );
  } catch (err) {
    return { error: "Error: " + JSON.stringify(err) };
  }
};

const requestInvitation = async (body: any) => {
  try {
    return axios({
      method: "post",
      url: baseUrl + "/register",
      headers: {
        "Content-Type": "application/json",
      },
      data: JSON.stringify(body),
    }).then(
      (result) => {
        if (result.status === 200) {
          return result.data.subscription;
        }
      },
      (error) => {
        console.log({ error: "Error: " + error.message });
        return { error: "Error: " + error.message };
      }
    );
  } catch (err) {
    return { error: "Error: " + JSON.stringify(err) };
  }
};

const get_service_topten = async () => {
  try {
    return axios({
      method: "get",
      url: baseUrl + "service_topten",
    }).then(
      (result) => {
        console.log({ result });
        if (result.status === 200) {
          return result.data.data.payload;
        }
        return [];
      },
      (error) => {
        console.log({ error: "Error: " + error.message });
        return { error: "Error: " + error.message };
      }
    );
  } catch (err) {
    return { error: "Error: " + JSON.stringify(err) };
  }
};

const get_service_count = async () => {
  try {
    return axios({
      method: "get",
      url: baseUrl + "service_count",
    }).then(
      (result) => {
        console.log({ result });
        if (result.status === 200) {
          return result.data.data.payload;
        }
        return [];
      },
      (error) => {
        console.log({ error: "Error: " + error.message });
        return { error: "Error: " + error.message };
      }
    );
  } catch (err) {
    return { error: "Error: " + JSON.stringify(err) };
  }
};

const get_service_cost = async () => {
  try {
    return axios({
      method: "get",
      url: baseUrl + "service_cost",
    }).then(
      (result) => {
        console.log({ result });
        if (result.status === 200) {
          return result.data.data.payload;
        }
        return [];
      },
      (error) => {
        console.log({ error: "Error: " + error.message });
        return { error: "Error: " + error.message };
      }
    );
  } catch (err) {
    return { error: "Error: " + JSON.stringify(err) };
  }
};
const getById = async (id: number) => {
  try {
    return axios({
      method: "get",
      url: baseUrl + `/${id}`,
    }).then(
      (result) => {
        return result.data.payload;
      },
      (error) => {
        console.log({ error: "Error: " + error.message });
        return { error: "Error: " + error.message };
      }
    );
  } catch (err) {
    return { error: "Error: " + JSON.stringify(err) };
  }
};

const create = async (body: any) => {
  try {
    return axios({
      method: "post",
      url: baseUrl,
      headers: {
        "Content-Type": "application/json",
      },
      data: JSON.stringify(body),
    }).then(
      (result) => {
        return result.data.payload;
      },
      (error) => {
        console.log({ error: "Error: " + error.message });
        return { error: "Error: " + error.message };
      }
    );
  } catch (err) {
    return { error: "Error: " + JSON.stringify(err) };
  }
};

const update = async (id: number, body: any) => {
  try {
    return axios({
      method: "put",
      url: baseUrl + `/${id}`,
      data: JSON.stringify(body),
    }).then(
      (result) => {
        return result.data.payload;
      },
      (error) => {
        console.log({ error: "Error: " + error.message });
        return { error: "Error: " + error.message };
      }
    );
  } catch (err) {
    return { error: "Error: " + JSON.stringify(err) };
  }
};

const deleteById = async (id: string) => {
  try {
    return axios({
      method: "delete",
      url: baseUrl + `/${id}`,
    }).then(
      (result) => {
        return result.data.payload;
      },
      (error) => {
        console.log({ error: "Error: " + error.message });
        return { error: "Error: " + error.message };
      }
    );
  } catch (err) {
    return { error: "Error: " + JSON.stringify(err) };
  }
};

export {
  get_service_topten,
  get_service_count,
  get_service_cost,
  getById,
  create,
  update,
  deleteById,
  requestInvitation,
  newGuestClient,
};
