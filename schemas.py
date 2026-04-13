from pydantic import BaseModel, Field
from typing import Optional

class TarefaBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=100)
    descricao: str = Field(..., min_length=1, max_length=500)
    concluido: bool = False


class TarefaCreate(TarefaBase):
    pass

class TarefaUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=100)
    descricao: Optional[str] = Field(None, min_length=1, max_length=500)
    concluido: Optional[bool] = None

class Tarefa(TarefaBase):
    id: int