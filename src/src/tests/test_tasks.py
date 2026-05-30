import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
import app
from app import create_task, list_tasks, update_task, delete_task, tasks


@pytest.fixture(autouse=True)
def reset():
    tasks.clear()
    app.next_id = 1
    yield
    tasks.clear()


def test_criar_tarefa_simples():
    t = create_task("Minha tarefa")
    assert t.title == "Minha tarefa"
    assert t.id == 1
    assert t.priority == "Media"
    assert t.status == "A Fazer"

def test_criar_tarefa_prioridade_alta():
    t = create_task("Urgente", priority="Alta")
    assert t.priority == "Alta"

def test_criar_tarefa_com_deadline():
    t = create_task("Entrega", deadline="30/05/2025")
    assert t.deadline == "30/05/2025"

def test_titulo_vazio_levanta_erro():
    with pytest.raises(ValueError):
        create_task("")

def test_ids_sequenciais():
    t1 = create_task("T1")
    t2 = create_task("T2")
    assert t1.id == 1
    assert t2.id == 2

def test_listar_tarefas_vazia():
    assert list_tasks() == []

def test_listar_retorna_todas():
    create_task("A"); create_task("B")
    assert len(list_tasks()) == 2

def test_atualizar_status():
    create_task("Tarefa")
    t = update_task(1, status="Em Progresso")
    assert t.status == "Em Progresso"

def test_atualizar_inexistente_retorna_none():
    assert update_task(999, status="Concluido") is None

def test_deletar_tarefa():
    create_task("Deletar")
    assert delete_task(1) is True
    assert len(list_tasks()) == 0

def test_deletar_inexistente_retorna_false():
    assert delete_task(999) is False
