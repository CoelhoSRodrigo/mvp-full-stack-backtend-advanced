from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from flask_cors import CORS
from models.doghouse import Doghouse
from models import Session
from schemas.doghouse_schema import *
from schemas.error_schema import *

info = Info(title="MVP PUC-Rio Doghouses", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

tag_doghouse = Tag(name="Doghouse", description="API para operações em canis.")

@app.after_request
def disable_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response

# -------------------------------------
# Definição da documentação do Swagger
# -------------------------------------
@app.route(
    "/",
)
def documentacao():
    return redirect("openapi/swagger")


# ----------------------------------
# método de requisição POST Doghouse
# ----------------------------------
@app.post(
    "/doghouse",
    tags=[tag_doghouse],
    summary="Cria um novo canil.",
    description="Cria um canil na base de dados.",
    responses={"201": DoghouseCreate, "400": ErrorSchema},
)
def create_doghouse(form: DoghouseCreate):
    session = Session()
    data = request.get_json()

    dogs = []
    for dog_data in data.get("dogs", []):
        dog = {"name": dog_data.get("name"), "image": dog_data.get("image")}
        dogs.append(dog)

    try:
        session.add(Doghouse(dogs=dogs))
        session.commit()
        return {"message": "Canil criado com sucesso"}, 201
    except Exception as e:
        error_msg = e.args
        return {"error": error_msg}, 400


# ---------------------------------
# método de requisição GET ALL doghouses
# ---------------------------------
@app.get(
    "/doghouses",
    tags=[tag_doghouse],
    summary="Lista todos os canis.",
    description="List todos os canis da base de dados.",
    responses={"200": DoghouseSchemaList, "400": ErrorSchema},
)
def list_doghouses():
    session = Session()
    doghouses = session.query(Doghouse).all()
    return apresenta_doghouses(doghouses), 200


# ---------------------------------------
# método de requisição Doghouse POR ID
# ---------------------------------------
@app.get(
    "/doghouse",
    tags=[tag_doghouse],
    summary="Canil by ID.",
    description="Este método retorna um canil pelo seu ID.",
    responses={"200": DoghouseSchemaView, "404": ErrorSchema},
)
def get_doghouse_by_id(query: DoghouseSchemaById):
    doghouse_id = query.id
    session = Session()
    doghouse = session.query(Doghouse).filter(Doghouse.id == doghouse_id).first()
    if doghouse:
        return apresenta_doghouse(doghouse), 200
    else:
        return {"message": "Canil não encontrado."}, 404


# ------------------------------------------
# método de requisição DELETE Store POR ID
# ------------------------------------------
@app.delete(
    "/doghouse",
    tags=[tag_doghouse],
    summary="Deleta canil por ID.",
    description="Este método deleta um canil pelo seu ID.",
    responses={"200": DoghouseSchemaDelete, "404": ErrorSchema},
)
def delete_doghouse(query: DoghouseSchemaById):
    session = Session()
    doghouse_id = query.id
    doghouse = session.query(Doghouse).filter(Doghouse.id == doghouse_id).first()

    if doghouse:
        session.delete(doghouse)
        session.commit()
        return {"message": "Canil deletado com sucesso.", "id": doghouse_id}, 200
    else:
        error_msg = "Canil não encontrado."
        return {"error": error_msg}, 404


# ---------------------------------------
# método de requisição PUT UPDATE STATUS
# ---------------------------------------
@app.put(
    "/doghouse",
    tags=[tag_doghouse],
    summary="Atualiza canil by ID.",
    description="Este método atualiza um canil pelo seu ID.",
    responses={"200": DoghouseSchemaUpdate, "404": ErrorSchema},
)
def update_doghouse(query: DoghouseSchemaById, form: DoghouseCreate):
    session = Session()
    doghouse_id = query.id
    doghouse = session.query(Doghouse).filter(Doghouse.id == doghouse_id).first()
    data = request.get_json()
    dogs = []

    for dog_data in data.get("dogs", []):
        dog = {"name": dog_data.get("name"), "image": dog_data.get("image")}
        dogs.append(dog)

    if doghouse:
        doghouse.dogs = dogs
        session.commit()
        return apresenta_doghouse(doghouse), 200
    else:
        error_msg = "Canil não encontrado."
        return {"error": error_msg}, 404


##############################################################################
# EXECUTAR APLICAÇÃO
##############################################################################
if __name__ == "__main__":
    app.run(debug=True)
