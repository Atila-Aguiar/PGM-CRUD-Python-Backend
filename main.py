from fastapi import FastAPI, HTTPException

from schemas import Tarefa, TarefaCreate, TarefaUpdate
from database import tarefas, proximo_id

app = FastAPI(title="CRUD de Tarefas")

@app.get("/api/tarefas", response_model=list[Tarefa])
def listar_tarefas():
    return tarefas

@app.get("/api/tarefas/{id}", response_model=Tarefa)
def obter_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.post("/api/tarefas", response_model=Tarefa, status_code=201)
def criar_tarefa(nova_tarefa: TarefaCreate):
    global proximo_id

    tarefa = {
        "id": proximo_id,
        "titulo": nova_tarefa.titulo,
        "descricao": nova_tarefa.descricao,
        "concluido": nova_tarefa.concluido,
    }

    tarefas.append(tarefa)
    proximo_id += 1
    return tarefa


@app.put("/api/tarefas/{id}", response_model=Tarefa)
def atualizar_tarefa(id: int, tarefa_atualizada: TarefaUpdate):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            if tarefa_atualizada.titulo is not None:
                tarefa["titulo"] = tarefa_atualizada.titulo
            if tarefa_atualizada.descricao is not None:
                tarefa["descricao"] = tarefa_atualizada.descricao
            if tarefa_atualizada.concluido is not None:
                tarefa["concluido"] = tarefa_atualizada.concluido
            return tarefa

    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.delete("/api/tarefas/{id}")
def excluir_tarefa(id: int):
    for i, tarefa in enumerate(tarefas):
        if tarefa["id"] == id:
            tarefas.pop(i)
            return {"mensagem": "Tarefa excluída com sucesso"}

    raise HTTPException(status_code=404, detail="Tarefa não encontrada")