import streamlit as st
from functions import get_todos, set_todos


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    set_todos(todos)


def complete_todo():
    for i in range(len(todos)):
        if st.session_state[f"{i}"]:
            del todos[i]
            break

    set_todos(todos)
    # todo = st.session_state["todo"]
    # index = todos.index(todo)
    # del todos[index]
    # set_todos(todos)


todos = get_todos()

st.title("App de tarefas")
st.write("Este app foi feito somente para aprendizado.")


for key, todo in enumerate(todos):
    st.checkbox(todo, key=key, on_change=complete_todo)

st.text_input(
    label="",
    placeholder="Digite uma tarefa e pressione enter...",
    on_change=add_todo,
    key="new_todo",
)
