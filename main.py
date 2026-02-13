from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)


def show_menu():
    print("\n===== Task Manager =====")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. View Progress")
    print("5. Exit")


def main():

    tasks = []

    while True:

        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":

            title = input("Enter task title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            add_task(tasks, title, description, due_date)

        elif choice == "2":

            title = input("Enter task title to mark complete: ")
            mark_task_as_complete(tasks, title)

        elif choice == "3":

            view_pending_tasks(tasks)

        elif choice == "4":

            calculate_progress(tasks)

        elif choice == "5":

            print("Exiting program. Goodbye!")
            break

        else:

            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
