import functions
import PySimpleGUI as sg

label = sg.Text("Digite uma tarefa")
input_box = sg.InputText(tooltip="Digite uma tarefa aqui", key="todo")
add_button = sg.Button("Adicionar")
list_box = sg.Listbox(
    values=functions.get_todos(), key="todoList", enable_events=True, size=[45, 10]
)
edit_button = sg.Button("Editar")


window = sg.Window(
    "To-do App",
    layout=[[label], [input_box, add_button], [list_box, edit_button]],
    font=("Helvetica", 20),
)

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Adicionar":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.set_todos(todos)
            window["todoList"].update(values=todos)
        case "Editar":
            todo_to_edit = values["todoList"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.set_todos(todos)
            window["todoList"].update(values=todos)
        case "todoList":
            window["todo"].update(value=values["todoList"][0])
        case sg.WIN_CLOSED:
            break

window.close()
