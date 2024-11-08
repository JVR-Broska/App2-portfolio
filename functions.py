import streamlit as st

def get_todo_list():
    try:
        with open('todos.txt', 'r') as local_file:
            local_todos = local_file.read()
            return local_todos
    except:
        local_file = open('todos.txt', 'w')
        local_file.close()
        local_todos = []
        return local_todos


def save_todo_list(todos):
    with open('todos.txt', 'w') as local_file:
        local_file.writelines(todos)
