import streamlit as st
from functions import get_todos, set_todos


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    set_todos(todos)


todos = get_todos()

st.title("App de tarefas")
st.write("Este app foi feito somente para aprendizado.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        set_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(
    label="",
    placeholder="Digite uma tarefa e pressione enter...",
    on_change=add_todo,
    key="new_todo",
)
