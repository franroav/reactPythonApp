export interface Response {
  statusCode: number;
  data: serviceResponse;
}

export interface serviceResponse {
  title: string;
  statusCode: number;
  payload: [Array<any>];
}
