from sqlalchemy import String
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from workoutapi.atleta.models import AtletaModel
from workoutapi.atleta.schemas import AtletaOut
from workoutapi.categorias.models import CategoriaModel
from workoutapi.centro_treinamento.models import CentroTreinamentoModel
from workoutapi.configs.database import get_db
from fastapi_pagination import Page, paginate

router = APIRouter()

@router.get("/", response_model=Page[AtletaOut])
def list_atletas(
    nome: str = Query(None, description="Filtrar por nome"),
    cpf: str = Query(None, description="Filtrar por CPF"),
    db: Session = Depends(get_db),
):
    query = db.query(AtletaModel)
    if nome:
        query = query.filter(AtletaModel.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(AtletaModel.cpf == cpf)
    atletas = query.all()
    return paginate(atletas)

from pydantic import BaseModel

class AtletaListOut(BaseModel):
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates="atleta", lazy='selectin')
    categoria: Mapped['CategoriaModel'] = relationship(back_populates="atleta", lazy='selectin')           