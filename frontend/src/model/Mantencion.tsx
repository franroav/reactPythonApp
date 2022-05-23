class Mtmo {
  private id_auto: number;
  private id_servicio: number;
  private fecha_servicio: Date;
  constructor(id_auto: number, id_servicio: number, fecha_servicio: Date) {
    this.id_auto = id_auto;
    this.id_servicio = id_servicio;
    this.fecha_servicio = fecha_servicio;
  }
}

export class Mantencion extends Mtmo {
  constructor(id_auto: number, id_servicio: number, fecha_servicio: Date) {
    super(id_auto, id_servicio, fecha_servicio);
  }
}
