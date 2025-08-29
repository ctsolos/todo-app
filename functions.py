FILEPATH = "todos.txt"

def get_todos(filename=FILEPATH):
    """Returns the existing todos in my file"""
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filename=FILEPATH):
    """Writes the new items on my file"""
    with open(filename, 'w') as file:
        file.writelines(todos_arg)

#