import json
import os
import sys
from datetime import datetime

DATA_FILE = "json.json"

def ensure_file_exists():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)

def load_tasks():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)

def add_task(description):
    ensure_file_exists()
    tasks = load_tasks()

    task_id = len(tasks) + 1
    now = datetime.now().isoformat()

    task = {
        "id": task_id,
        "description": description,
        "status": "Iniciar",
        "created_At": now,
        "updated_At": now

    }

    tasks.append(task)
    save_tasks(tasks)

def list_tasks(status_filter = None):
    ensure_file_exists()
    tasks = load_tasks()

    if not tasks:
        print('Lista vazia')
        return
    
    print('ID - DESCRIÇÃO - STATUS')
    print('-='*30)

    found = False
    for task in tasks:
        if status_filter is None or task["status"] == status_filter:
            print(f"[{task['id']} - {task['description']} - {task['status']}]")
            found = True

    if not found:
        print(f"Nenhuma task encontrada com o status {status_filter}.")



def update_tasks(task_id, new_status):
    ensure_file_exists()
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updated_At"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Status atualizado.")
            
    
    print("Tarefa não encontrada.")
        
def delete_task(task_id):
    ensure_file_exists()
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Tarefa removida")
            return
    
    print('Tarefa não encontrada.')


# =-=-=-=-=-=-=-=-=-=- SYS -=-=-=-=-=-=-=-=-=-=-=-=

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('Comando inválido.')
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Uso: python main.py 'Descrição da task' ")
    
        else:
            description = sys.argv[2]
            add_task(description)
            print('Task Adicionada.')
        
    elif command == "list":
        if len(sys.argv) == 2:
          list_tasks()
        else:
            status = sys.argv[2]
            list_tasks(status)        