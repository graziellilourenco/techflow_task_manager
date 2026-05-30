from models import Task
tasks = []
next_id = 1


def create_task(title, priority="Media", deadline=None):
    global next_id
    if not title or len(title.strip()) == 0:
        raise ValueError("O título da tarefa não pode ser vazio.")
    task = Task(id=next_id, title=title.strip(),
                priority=priority, deadline=deadline)
    tasks.append(task)
    next_id += 1
    return task
  
def list_tasks():
    """Retorna todas as tarefas cadastradas."""
    return tasks

def update_task(task_id, title=None, priority=None,
                status=None, deadline=None):
    for task in tasks:
        if task.id == task_id:
            if title:    task.title = title
            if priority: task.priority = priority
            if status:   task.status = status
            if deadline: task.deadline = deadline
            return task
    return None


def delete_task(task_id):
    global tasks
    original_len = len(tasks)
    tasks = [t for t in tasks if t.id != task_id]
    return len(tasks) < original_len


def print_tasks():
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return
    print(f"\n{'ID':<4} {'Título':<28} {'Prioridade':<10}"
          f" {'Status':<15} {'Prazo'}")
    print("-" * 70)
    for t in tasks:
        print(f"{t.id:<4} {t.title:<28} {t.priority:<10}"
              f" {t.status:<15} {t.deadline or '-'}")
      
if __name__ == "__main__":
    print("=== TechFlow Task Manager ===")
    create_task("Configurar servidor", "Alta", "30/05/2025")
    create_task("Mapear rotas de entrega", "Media", "15/06/2025")
    create_task("Treinar equipe", "Baixa")
    print_tasks()
    update_task(1, status="Em Progresso")
    update_task(2, status="Concluido")
    print("\nApós atualização:")
    print_tasks()
