from datetime import date, datetime

from pandas import DatetimeIndex
from servicio import Servicio
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

from db import Base


class Mantencion(Base):
    __tablename__ = "mantencion"

    id = Column(Integer, primary_key=True, index=True)
    id_auto = Column(Integer, ForeignKey('taxi.id'), nullable=False)
    id_servicio = Column(Integer, ForeignKey('servicio.id'), nullable=False)
    fecha_servicio = Column(String, nullable=False)

    def __repr__(self):
        return 'ItemModel(id_auto=%s, id_servicio=%s, fecha_servicio=%s)' % (self.id_auto, self.id_servicio, self.fecha_servicio)

    def fetch_by_id(db: Session, _id):
        return db.query(Mantencion).filter(Mantencion.id == _id).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Mantencion).offset(skip).limit(limit).all()


class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False, unique=True)
    items = relationship(
        "Item", primaryjoin="Store.id == Item.store_id", cascade="all, delete-orphan")

    def __repr__(self):
        return 'Store(name=%s)' % self.name

    id_auto = relationship(
        "Taxi", primaryjoin="Mantencion.id_auto == Taxi.id", cascade="all, delete-orphan")
    id_servicio = relationship(
        "Servicio", primaryjoin="Mantencion.id_servicio == Servicio.id", cascade="all, delete-orphan")
