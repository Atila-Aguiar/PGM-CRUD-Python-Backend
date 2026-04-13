# CRUD de Tarefas

Aplicação de gerenciamento de tarefas (To-Do List), desenvolvida com **FastAPI** no backend e **SQLite** como banco de dados.

---

## Estrutura da Tarefa

Cada tarefa possui os seguintes atributos:

- **ID** (int)
- **Título** (string)
- **Descrição** (string)
- **Concluído** (boolean)

---

## Funcionalidades

### Backend (API - FastAPI)

| Método | Endpoint | Descrição |
|--------|--------|----------|
| GET | `/api/tarefas` | Listar todas as tarefas |
| GET | `/api/tarefas/{id}` | Obter uma tarefa pelo ID |
| POST | `/api/tarefas` | Criar uma nova tarefa |
| PUT | `/api/tarefas/{id}` | Atualizar uma tarefa existente |
| DELETE | `/api/tarefas/{id}` | Excluir uma tarefa |

---

## ▶️ Como Executar o Projeto

### 📦 Backend

No terminal, execute:

```bash
pip install -r requirements.txt
uvicorn main:app --reload