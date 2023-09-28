from pydantic import BaseModel
from typing import List
from datetime import date, datetime
from models.doghouse import Doghouse, Dog


class DoghouseCreate(BaseModel):
    """Classe que define como uma Doghouse deve ser cadastrada"""

    dogs: List[Dog]


class DoghouseSchemaView(BaseModel):
    """Classe que define como uma Store cadastrada é apresentada"""

    id: int
    data_criacao: date
    # data_edicao: datetime
    dogs: List[Dog]


class DoghouseSchemaList(BaseModel):
    """Define como serão apresentadas todas as Doghouses"""

    doghouses: List[DoghouseSchemaView]


class DoghouseSchemaById(BaseModel):
    """Define como buscar uma Doghouse pelo ID"""

    id: int


class DoghouseSchemaDelete(BaseModel):
    """Define como uma Doghouse será apresentada após deletada"""

    id: int


class DoghouseSchemaUpdate(BaseModel):
    """Este Schema mostra o que deve ser enviado na alteração do status da Doghouse"""

    status: bool


def apresenta_doghouse(doghouse: Doghouse) -> Doghouse:
    return {
        "id": doghouse.id,
        "dogs": doghouse.dogs,
        "data_criacao": formata_data(doghouse.data_criacao),
    }


def apresenta_doghouses(doghouses: List[Doghouse]) -> List[Doghouse]:
    doghouseList = []

    for doghouse in doghouses:
        doghouseList.append(
            {
                "id": doghouse.id,
                "data_criacao": formata_data(doghouse.data_criacao),
                "dogs": doghouse.dogs,
            }
        )
    return {"doghouseList": doghouseList}


def formata_data(dataBruta: date) -> date:
    """Função para apresentar a data formatada DD/MM/AAAA"""
    return dataBruta.strftime("%d/%m/%Y")
