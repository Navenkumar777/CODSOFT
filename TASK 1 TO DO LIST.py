import json
from datetime import datetime

# Initial Data
tasks = []
mood_priority_map = {
    "Energetic": "high",
    "Calm": "medium",
    "Stressed": "low",
    "Tired": "low"
}


# Function to Add a Task
def add_task():
    title = input("Enter task title: ")
    deadline = input("Enter task deadline (YYYY-MM-DD): ")
    difficulty = input("Enter task difficulty (low, medium, high): ")
    tasks.append({
        "id": len(tasks) + 1,
        "title": title,
        "deadline": deadline,
        "difficulty": difficulty.lower(),
        "completed": False
    })
    print("Task added successfully!")


# Function to View Tasks
def view_tasks():
    print("\nYour Tasks:")
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        print(f"{task['id']}. {task['title']} (Deadline: {task['deadline']}, Difficulty: {task['difficulty']}, Completed: {status})")


# Function to Mark a Task as Completed
def complete_task():
    task_id = int(input("Enter the task ID to mark as completed: "))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("Task marked as completed!")
            return
    print("Task not found!")


# Function to Prioritize Tasks Based on Mood
def prioritize_tasks(mood):
    mood = mood.capitalize()
    if mood not in mood_priority_map:
        print("Invalid mood! Using default priority.")
        return tasks

    sorted_tasks = sorted(
        tasks,
        key=lambda x: (
            x["difficulty"] == mood_priority_map[mood],  # Match mood priority
            x["deadline"]  # Sort by deadline
        )
    )
    return sorted_tasks


# Function to Log Mood
def log_mood(mood):
    with open("mood_log.txt", "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Mood: {mood}\n")
    print("Mood logged!")


# Main Menu
def main_menu():
    while True:
        print("\n--- Mood-Based To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete a Task")
        print("4. Prioritize Tasks Based on Mood")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            mood = input("How are you feeling? (Energetic, Calm, Stressed, Tired): ").capitalize()
            prioritized_tasks = prioritize_tasks(mood)
            log_mood(mood)
            print("\nPrioritized Tasks:")
            for task in prioritized_tasks:
                status = "✓" if task["completed"] else "✗"
                print(f"{task['id']}. {task['title']} (Deadline: {task['deadline']}, Difficulty: {task['difficulty']}, Completed: {status})")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the Application
if __name__ == "__main__":
    main_menu()
