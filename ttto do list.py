# Function to display the current todo list
def display_todo_list(todo_list):
    if not todo_list:
        print("Todo list is empty")
    else:
        print("Todo List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the todo list
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the todo list.")

# Function to remove a task from the todo list
def remove_task(todo_list, task_index):
    if task_index >= 1 and task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the todo list.")
    else:
        print("Invalid task index.")

# Main function to interact with the todo list
def main():
    todo_list = []

    while True:
        print("\nTodo List Menu:")
        print("1. Display Todo List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            task = input("Enter task to add: ")
            add_task(todo_list, task)
        elif choice == '3':
            task_index = int(input("Enter index of task to remove: "))
            remove_task(todo_list, task_index)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

