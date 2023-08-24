import functions
import PySimpleGUI as sg
import time

clock = sg.Text("", key="clock")
label = sg.Text("Digite uma tarefa")
input_box = sg.InputText(tooltip="Digite uma tarefa aqui", key="todo")
add_button = sg.Button("Adicionar")
list_box = sg.Listbox(
    values=functions.get_todos(), key="todoList", enable_events=True, size=[45, 10]
)
edit_button = sg.Button("Editar")
complete_button = sg.Button("Completar")
exit_button = sg.Button("Sair")

layout = [
    [clock],
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button],
]

window = sg.Window(
    "To-do App",
    layout=layout,
    font=("Helvetica", 20),
)

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y - %H:%M:%S"))
    match event:
        case "Adicionar":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.set_todos(todos)
            window["todoList"].update(values=todos)
        case "Editar":
            try:
                todo_to_edit = values["todoList"][0]
                new_todo = values["todo"] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.set_todos(todos)
                window["todoList"].update(values=todos)
            except IndexError:
                sg.popup(
                    "Você precisa selecionar primeiro uma tarefa!",
                    font=("Helvetica", 20),
                )
        case "todoList":
            window["todo"].update(value=values["todoList"][0])
        case "Completar":
            try:
                todo_to_complete = values["todoList"][0]
                todos = functions.get_todos()

                index = todos.index(todo_to_complete)
                del todos[index]
                functions.set_todos(todos)
                window["todoList"].update(values=todos)
            except IndexError:
                sg.popup(
                    "Você precisa selecionar primeiro uma tarefa!",
                    font=("Helvetica", 20),
                )
        case "Sair":
            break
        case sg.WIN_CLOSED:
            break

window.close()
