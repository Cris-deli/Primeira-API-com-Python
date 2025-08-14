from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workoutapi.contrib.repositorio.models import AtletaModel, BaseModel



class CategoriaModel(BaseModel):
    __tablename__ = 'categoria'

    pk_id : Mapped(int) = mapped_column(Integer, primary_key=True) # type: ignore
    nome : Mapped(str) = mapped_column(String(50), nullable=False) # type: ignore
    atleta: Mapped['AtletaModel'] = relationship(back_populates="categoria")