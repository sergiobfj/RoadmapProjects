import json
import os
import sys
from datetime import date, datetime


DATA_FILE = 'expenses.json'

def ensure_file_exists():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', encoding="utf-8") as file:
            json.dump([], file)

def load_expenses():
    with open(DATA_FILE, 'r', encoding="utf-8") as file:
        data = json.load(file)
        if data is None:
            return []
        if not isinstance(data, list):
            raise ValueError("expenses.json deve conter uma lista de despesas.")
        return data

def save_expense(expenses):
    with open(DATA_FILE, 'w', encoding="utf-8") as file:
        json.dump(expenses, file, indent=2, ensure_ascii=False)

def add_expense(description, amount):
    ensure_file_exists()
    expenses = load_expenses()

    expense_id = len(expenses) + 1
    now = datetime.now().isoformat()

    expense = {
        "id": expense_id,
        "description": description,
        "amount": amount,
        "date": now
    }

    expenses.append(expense)
    save_expense(expenses)

def list_expenses():
    ensure_file_exists()
    expenses = load_expenses()

    if not expenses:
        print('Lista vazia')
        return
    
    print('ID - DESCRIÇÃO - AMOUNT - DATA')
    print('-='*30)

    for expense in expenses:
        print(f"[{expense['id']} - {expense['description']} - {expense['amount']} - {expense['date']}]")

def update_expense(expense_id, new_amount):
    ensure_file_exists()
    expenses = load_expenses()

    for expense in expenses:
        if expense['id'] == expense_id:
            expense['amount'] = new_amount
            save_expense(expenses)
            print('Valor atualizado.')
        
        print('Despesa não encontrada.')

def delete_expense(expense_id):
    ensure_file_exists()
    expenses = load_expenses()

    for expense in expenses:
        if expense['id'] == expense_id:
            expenses.remove(expense)
            save_expense(expense)
            print('Despesa removida.')
            return
        
    print('Despesa não encontrada.')

ensure_file_exists()
delete_expense(2)