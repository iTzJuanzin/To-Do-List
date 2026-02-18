import json
from models import Tarefa

ARQUIVO = "tarefas.json"


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(
            [t.__dict__ for t in tarefas],
            f,
            indent=4,
            ensure_ascii=False
        )


def carregar_tarefas():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return [Tarefa(**t) for t in dados]
    except FileNotFoundError:
        return []
