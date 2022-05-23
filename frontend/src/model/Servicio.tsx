class BusinessServiceClass {
  private service_name: string;
  private unit_cost: string;
  private category_service: string;
  constructor(
    service_name: string,
    unit_cost: string,
    category_service: string
  ) {
    this.service_name = service_name;
    this.unit_cost = unit_cost;
    this.category_service = category_service;
  }
}

export class Servicio extends BusinessServiceClass {
  constructor(
    service_name: string,
    unit_cost: string,
    category_service: string
  ) {
    super(service_name, unit_cost, category_service);
  }
}
