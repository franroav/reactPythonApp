from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

from db import Base


class Taxi(Base):
    __tablename__ = "taxi"

    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String(10), nullable=False, unique=True, index=True)
    ano = Column(Integer, nullable=False)
    marca = Column(String(10), nullable=False)
    km = Column(Integer, nullable=False)
    oil_tank = Column(Integer, nullable=False)
    gasoline_tank = Column(Integer, nullable=False)
    presion = Column(Integer, nullable=False)

    def __repr__(self):
        return 'ItemModel(modelo=%s, ano=%s, marca=%s, km=%s, oil_tank=%s, gasoline_tank=%s, presion=%s)' % (self.modelo, self.ano, self.marca, self.km, self.oil_tank, self.gasoline_tank, self.presion)

    def fetch_by_id(db: Session, _id):
        return db.query(Taxi).filter(Taxi.id == _id).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Taxi).offset(skip).limit(limit).all()
