from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workoutapi.contrib.repositorio.models import AtletaModel, BaseModel



class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'

    pk_id : Mapped(int) = mapped_column(Integer, primary_key=True) # type: ignore
    nome : Mapped(str) = mapped_column(String(50), nullable=False)
    endereço : Mapped(str) = mapped_column(String(60), nullable=False)
    proprietario: Mapped(str) = mapped_column(String(30), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates="centro_treinamento")