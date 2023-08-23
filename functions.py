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
