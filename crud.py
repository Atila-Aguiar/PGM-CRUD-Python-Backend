from sqlalchemy.orm import Session
from models import TarefaModel
from schemas import TarefaCreate, TarefaUpdate


def listar_tarefas(db: Session):
    return db.query(TarefaModel).all()


def obter_tarefa(db: Session, tarefa_id: int):
    return db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()


def criar_tarefa(db: Session, tarefa: TarefaCreate):
    nova_tarefa = TarefaModel(
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        concluido=tarefa.concluido
    )
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa


def atualizar_tarefa(db: Session, tarefa_id: int, dados: TarefaUpdate):
    tarefa = db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()

    if not tarefa:
        return None

    if dados.titulo is not None:
        tarefa.titulo = dados.titulo

    if dados.descricao is not None:
        tarefa.descricao = dados.descricao

    if dados.concluido is not None:
        tarefa.concluido = dados.concluido

    db.commit()
    db.refresh(tarefa)
    return tarefa


def excluir_tarefa(db: Session, tarefa_id: int):
    tarefa = db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()

    if not tarefa:
        return None

    db.delete(tarefa)
    db.commit()
    return tarefa