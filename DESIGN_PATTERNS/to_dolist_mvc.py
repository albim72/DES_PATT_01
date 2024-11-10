# Model
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"


class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Invalid task index")

    def get_tasks(self):
        return self.tasks


# View
class TaskView:
    def display_tasks(self, tasks):
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    def display_message(self, message):
        print(message)

    def display_error(self, error):
        print(f"Error: {error}")


# Controller
class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, description):
        self.model.add_task(description)
        self.view.display_message("Task added successfully.")

    def remove_task(self, index):
        try:
            self.model.remove_task(index - 1)  # Convert to 0-based index
            self.view.display_message("Task removed successfully.")
        except IndexError as e:
            self.view.display_error(e)

    def complete_task(self, index):
        try:
            self.model.tasks[index - 1].mark_complete()  # Convert to 0-based index
            self.view.display_message("Task marked as complete.")
        except IndexError as e:
            self.view.display_error(e)

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)


# Main logic to run the To-Do List MVC application
if __name__ == "__main__":
    # Create instances of the model, view, and controller
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    # Example interaction with the system
    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Complete a task")
        print("4. Show all tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter the task description: ")
            controller.add_task(description)
        elif choice == "2":
            try:
                index = int(input("Enter the task number to remove: "))
                controller.remove_task(index)
            except ValueError:
                view.display_error("Invalid input. Please enter a number.")
        elif choice == "3":
            try:
                index = int(input("Enter the task number to mark as complete: "))
                controller.complete_task(index)
            except ValueError:
                view.display_error("Invalid input. Please enter a number.")
        elif choice == "4":
            controller.show_tasks()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            view.display_error("Invalid choice. Please select a valid option.")
