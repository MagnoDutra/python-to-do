import functions
import PySimpleGUI as sg

label = sg.Text("Digite uma tarefa")
input_box = sg.InputText(tooltip="Digite uma tarefa aqui", key="todo")
add_button = sg.Button("Adicionar")

window = sg.Window(
    "To-do App", layout=[[label], [input_box, add_button]], font=("Helvetica", 20)
)

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Adicionar":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.set_todos(todos)

window.close()
