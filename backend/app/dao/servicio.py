from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

from db import Base


class Servicio(Base):
    __tablename__ = "servicio"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String(15), nullable=False, unique=True, index=True)
    unit_cost = Column(Float, nullable=False)
    category_service = Column(String(15), nullable=False)

    def __repr__(self):
        return 'ItemModel(service_name=%s, unit_cost=%s, category_service=%s)' % (self.service_name, self.unit_cost, self.category_service)

    def fetch_by_id(db: Session, _id):
        return db.query(Servicio).filter(Servicio.id == _id).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Servicio).offset(skip).limit(limit).all()
