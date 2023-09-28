from sqlalchemy import Column, Integer, Date, JSON
from datetime import date
from pydantic import BaseModel
from models.base import Base


class Dog(BaseModel):
    name: str
    image: str


class Doghouse(Base):
    __tablename__ = "doghouse"

    id = Column("pk_doghouse", Integer, primary_key=True)
    data_criacao = Column(Date, default=date.today)
    dogs = Column(JSON)

    def atualiza_data_edicao(self) -> None:
        self.data_edicao = date.today()
