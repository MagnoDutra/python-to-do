todo_list = []


def show_todo():
    file = open("todos.txt", "r")
    todo_list = file.readlines()
    file.close()
    for index, todo in enumerate(todo_list):
        print(f"{index + 1} - {todo}")


print("Bem vindo a sua lista de tarefas.")

while True:
    action = input("\nDigite adicionar, mostrar, editar, completar ou sair: ")
    action = action.strip()

    match action:
        case "adicionar":
            todo = input("Digite uma tarefa: ") + "\n"

            file = open("todos.txt", "r")
            todo_list = file.readlines()
            file.close()

            todo_list.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todo_list)
            file.close()
        case "mostrar":
            show_todo()
        case "editar":
            show_todo()
            index = int(input("Digite o número da tarefa que deseja editar: "))
            if index > len(todo_list):
                print("Digite um número válido! Voltando ao menu")
            else:
                todo_list[index - 1] = input("Digite a tarefa: ")
                print("Tarefa editada")
        case "completar":
            show_todo()
            index = int(input("Digite o número da tarefa que deseja completar: "))
            del todo_list[index - 1]
            print("Parabéns! Tarefa removida com sucesso.")
        case "sair":
            break
        case default:
            print("Digite um comando válido!")

print("Até logo!")
