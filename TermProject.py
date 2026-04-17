import json
from datetime import datetime

# Global task list
tasks = []

# ----------------------------
# OOP CLASS
# ----------------------------
class Task:
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
        self.completed = False

    def mark_done(self):
        self.completed = True


# ----------------------------
# FUNCTIONS
# ----------------------------

def show_menu():
    print("\n====== SMART TASK MANAGER ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Check Overdue Tasks")
    print("8. Exit")


def add_task():
    try:
        title = input("Enter task title: ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")

        # Validate date
        datetime.strptime(deadline, "%Y-%m-%d")

        task = Task(title, deadline)
        tasks.append(task)

        print("✅ Task added successfully!")

    except ValueError:
        print("❌ Invalid date format! Use YYYY-MM-DD.")
    except Exception as e:
        print("❌ Error:", e)


def view_tasks():
    if not tasks:
        print("⚠️ No tasks available.")
        return

    print("\n--- TASK LIST ---")
    for i, task in enumerate(tasks):
        status = "✅ Done" if task.completed else "❌ Pending"
        print(f"{i+1}. {task.title} | Deadline: {task.deadline} | {status}")


def mark_complete():
    try:
        view_tasks()
        index = int(input("Enter task number to mark complete: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index].mark_done()
            print("✅ Task marked as completed!")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")
    except Exception as e:
        print("❌ Error:", e)


def delete_task():
    try:
        view_tasks()
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Task '{removed.title}' deleted.")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")
    except Exception as e:
        print("❌ Error:", e)


def save_tasks():
    try:
        data = []

        for task in tasks:
            data.append({
                "title": task.title,
                "deadline": task.deadline,
                "completed": task.completed
            })

        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)

        print("💾 Tasks saved successfully!")

    except Exception as e:
        print("❌ Error saving tasks:", e)


def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

        tasks = []
        for item in data:
            task = Task(item["title"], item["deadline"])
            task.completed = item["completed"]
            tasks.append(task)

        print("📂 Tasks loaded successfully!")

    except FileNotFoundError:
        print("⚠️ No saved file found. Starting fresh.")
    except Exception as e:
        print("❌ Error loading tasks:", e)


def check_overdue():
    if not tasks:
        print("⚠️ No tasks available.")
        return

    today = datetime.now().date()
    found = False

    print("\n--- OVERDUE TASKS ---")
    for task in tasks:
        deadline_date = datetime.strptime(task.deadline, "%Y-%m-%d").date()

        if deadline_date < today and not task.completed:
            print(f"⚠️ {task.title} (Deadline: {task.deadline})")
            found = True

    if not found:
        print("🎉 No overdue tasks!")


# ----------------------------
# MAIN FUNCTION
# ----------------------------
def main():
    load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            load_tasks()
        elif choice == "7":
            check_overdue()
        elif choice == "8":
            save_tasks()
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


# ----------------------------
# PROGRAM ENTRY POINT
# ----------------------------
if __name__ == "__main__":
    main()