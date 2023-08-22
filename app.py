def get_todos():
    with open("todos.txt", "r") as file:
        todo_list = file.readlines()
    return todo_list


def set_todos(todos):
    with open("todos.txt", "w") as file:
        file.writelines(todos)


def show_todo():
    todo_list = get_todos()

    formated_list = [todo.strip("\n") for todo in todo_list]

    for index, todo in enumerate(formated_list):
        print(f"{index + 1} - {todo}")


print("Bem vindo a sua lista de tarefas.")

while True:
    action = input("\nDigite adicionar, mostrar, editar, completar ou sair: ")
    action = action.strip()

    if action.startswith("adicionar"):
        todo = action[10:]

        todo_list = get_todos()

        todo_list.append(todo + "\n")

        set_todos(todo_list)
    elif action.startswith("mostrar"):
        show_todo()
    elif action.startswith("editar"):
        try:
            todo_list = get_todos()
            index = int(action[7:])

            if index > len(todo_list):
                print("Digite um número válido! Voltando ao menu")
            else:
                todo_list[index - 1] = input("Digite a tarefa: ") + "\n"

                set_todos(todo_list)

                print("Tarefa editada")
        except ValueError:
            print("Digite somente o número da tarefa")
            continue
    elif action.startswith("completar"):
        try:
            todo_list = get_todos()

            index = int(action[10:])
            del todo_list[index - 1]

            set_todos(todo_list)

            print("Parabéns! Tarefa removida com sucesso.")
        except IndexError:
            print("Você digitou um número que não existe na lista, tente novamente")
            continue
        except ValueError:
            print("É necessário digitar somente o número desejado e nenhuma letra.")
            continue
    elif action.startswith("sair"):
        break
    else:
        print("Digite um comando válido!")

    # match action:
    #     case "adicionar":
    #         todo = input("Digite uma tarefa: ") + "\n"

    #         with open("todos.txt", "r") as file:
    #             todo_list = file.readlines()

    #         todo_list.append(todo)

    #         with open("todos.txt", "w") as file:
    #             file.writelines(todo_list)
    #     case "mostrar":
    #         show_todo()
    #     case "editar":
    #         show_todo()

    #         with open("todos.txt", "r") as file:
    #             todo_list = file.readlines()

    #         index = int(input("Digite o número da tarefa que deseja editar: "))
    #         if index > len(todo_list):
    #             print("Digite um número válido! Voltando ao menu")
    #         else:
    #             todo_list[index - 1] = input("Digite a tarefa: ") + "\n"

    #             with open("todos.txt", "w") as file:
    #                 file.writelines(todo_list)

    #             print("Tarefa editada")
    #     case "completar":
    #         show_todo()

    #         with open("todos.txt", "r") as file:
    #             todo_list = file.readlines()

    #         index = int(input("Digite o número da tarefa que deseja completar: "))
    #         del todo_list[index - 1]

    #         with open("todos.txt", "w") as file:
    #             file.writelines(todo_list)

    #         print("Parabéns! Tarefa removida com sucesso.")
    #     case "sair":
    #         break
    #     case default:
    #         print("Digite um comando válido!")

print("Até logo!")
