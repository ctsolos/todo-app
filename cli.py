#from functions import get_todos, write_todos
import functions # I have to call function as functions.get_todos()
import time

now = time.strftime("%b %d, %Y - %H:%M:%S")
print(f"It's:", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
#Commit Test
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo.capitalize() + "\n")
        todos.sort()

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        #Another way to strip is this:
        # new_todos = [item.strip('\n') for item in todos]

        for i, todo in enumerate(todos):
            list_to_show = f"{i+1}. {todo}"
            print(list_to_show.strip('\n'))

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            print(f"Replace {todos[number].strip()} with: ")
            edited_todo = input()
            todos[number] = edited_todo.capitalize() + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        completed = int(user_action[9:])

        todos = functions.get_todos()

        completed = completed - 1
        to_be_removed = todos[completed]
        todos.pop(completed)

        functions.write_todos(todos)

        message = f"Todo '{to_be_removed.strip()}' has been removed"
        print(message)
    elif user_action.startswith("exit"):
        break

    else:
        print("Give me something I asked for...")

print("Bye!")
