class Car {
  private modelo: string;
  private ano: number;
  private marca: string;
  private km: number;
  private oil_tank: number;
  private gasoline_tank: number;
  private presion: number;
  constructor(
    modelo: string,
    ano: number,
    marca: string,
    km: number,
    oil_tank: number,
    gasoline_tank: number,
    presion: number
  ) {
    this.modelo = modelo;
    this.ano = ano;
    this.marca = marca;
    this.km = km;
    this.oil_tank = oil_tank;
    this.gasoline_tank = gasoline_tank;
    this.presion = presion;
  }
}

export class Taxi extends Car {
  constructor(
    modelo: string,
    ano: number,
    marca: string,
    km: number,
    oil_tank: number,
    gasoline_tank: number,
    presion: number
  ) {
    super(modelo, ano, marca, km, oil_tank, gasoline_tank, presion);
  }
}
