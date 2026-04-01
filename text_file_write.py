todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit :")
    user_action = user_action.strip()

    match user_action:
        case "add" :
            todo = input("Enter a todo:") + "\n"               # +\n -this is to enter a break line and this will give a space or line between ite

            todos.append(todo)

            file = open('todos.txt', 'w')                      #we use open() object for opening the txt files and W is for write operation and it also overwrites the file
            file.writelines(todos)                             # this is will write a input of todos to text file

        case "show"  :
            for index,item in enumerate(todos):
                row = f"{index}-{item}"
                print(row)

        case "edit":
            number = int(input("Number of the todo to edit:"))
            number = number-1
            new_todo = input("Enter a new todo:")
            todos[number] = new_todo

        case "complete" :
            number = int(input("Number of the todo to complete:"))
            todos.pop(number -1)

        case "exit":
            break

print("Bye!")


