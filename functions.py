FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """ Reads the to-dos saved in a text file
    """
    with open(filepath, 'r') as file:
        todos_get = file.readlines()
        return todos_get


def upd_todo(todos, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("Hello functions")

