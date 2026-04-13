from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
from database import engine, SessionLocal
import models
import schemas

models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="CRUD de Tarefas")

origins = [
    "http://localhost:3000",
    "https://atila-aguiar.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/tarefas", response_model=list[schemas.TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
    return crud.listar_tarefas(db)

@app.get("/api/tarefas/{id}", response_model=schemas.TarefaResponse)
def obter_tarefa(id: int, db: Session = Depends(get_db)):
    tarefa = crud.obter_tarefa(db, id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

@app.post("/api/tarefas", response_model=schemas.TarefaResponse, status_code=201)
def criar_tarefa(tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    return crud.criar_tarefa(db, tarefa)


@app.put("/api/tarefas/{id}", response_model=schemas.TarefaResponse)
def atualizar_tarefa(id: int, dados: schemas.TarefaUpdate, db: Session = Depends(get_db)):
    tarefa = crud.atualizar_tarefa(db, id, dados)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


@app.delete("/api/tarefas/{id}")
def excluir_tarefa(id: int, db: Session = Depends(get_db)):
    tarefa = crud.excluir_tarefa(db, id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"mensagem": "Tarefa excluída com sucesso"}