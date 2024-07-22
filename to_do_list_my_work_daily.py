class ToDoList:
    def __init__(self, filename='todo_list.txt'):
        self.filename = filename
        self.tasks = self._load_tasks()

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self._save_tasks()
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            self._save_tasks()
            print(f"Task {task_number} updated to '{new_task}'.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            self._save_tasks()
            print(f"Task '{task['task']}' deleted.")
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self._save_tasks()
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")

    def _save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                completed = '1' if task["completed"] else '0'
                file.write(f"{task['task']}|{completed}\n")

    def _load_tasks(self):
        tasks = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    task, completed = line.strip().split('|')
                    tasks.append({"task": task, "completed": completed == '1'})
        except FileNotFoundError:
            pass
        return tasks

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Complete task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            task_number = int(input("Enter the task number to mark as complete: "))
            todo_list.complete_task(task_number)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
