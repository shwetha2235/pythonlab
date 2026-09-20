"""
Program 4: Interactive Command-Line Task Scheduler
with Lazy Evaluation

This micro-tool manages a running queue of tasks.
It uses Boolean logic operators such as and, or, and
not along with if-elif-else statements to decide
whether a task can be executed. The program continues
running until the user selects the exit option.
"""

# Create an empty task queue
tasks = []


def add_task():
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ").lower()
    status = input("Is the task ready? (yes/no): ").lower()

    task = {
        "name": task_name,
        "priority": priority,
        "ready": status == "yes"
    }

    tasks.append(task)

    print("Task added successfully.")


def display_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== TASK QUEUE ==========")

    for index, task in enumerate(tasks, start=1):
        print(
            index,
            ".",
            task["name"],
            "| Priority:",
            task["priority"],
            "| Ready:",
            task["ready"]
        )


def execute_task():
    if not tasks:
        print("\nNo tasks available for execution.")
        return

    print("\nChecking tasks using Boolean logic...")

    for task in tasks:

        # Short-circuit evaluation using AND and OR
        can_execute = (
            task["ready"]
            and (
                task["priority"] == "high"
                or task["priority"] == "medium"
            )
        )

        if can_execute:
            print("\nExecuting task:", task["name"])
            tasks.remove(task)
            return

    print("\nNo task is currently ready for execution.")


def remove_task():
    if not tasks:
        print("\nNo tasks available.")
        return

    display_tasks()

    try:
        number = int(input("\nEnter task number to remove: "))

        if number >= 1 and number <= len(tasks):
            removed = tasks.pop(number - 1)
            print("Removed task:", removed["name"])

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    print("==========================================")
    print("   INTERACTIVE COMMAND-LINE TASK")
    print("             SCHEDULER")
    print("==========================================")

    while True:

        print("\n---------- MENU ----------")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Execute Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            display_tasks()

        elif choice == "3":
            execute_task()

        elif choice == "4":
            remove_task()

        elif choice == "5":
            print("\nExiting Task Scheduler...")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()