import functions
import PySimpleGUI as sg

label = sg.Text("Digite uma tarefa")
input_box = sg.InputText(tooltip="Digite uma tarefa aqui")
add_button = sg.Button("Adicionar")

window = sg.Window("To-do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
