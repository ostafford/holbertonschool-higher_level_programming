import json
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        # Load existing tasks when creating TaskManager
        self.load_tasks()
    
    def add_task(self, title, description, due_date=None):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()  # Save after adding
        return task
    
    def save_tasks(self):
        # Convert tasks to dictionary format
        tasks_dict = [
            {
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
                "completed": task.completed,
                "created_at": task.created_at
            }
            for task in self.tasks
        ]
        
        # Save to file
        with open(self.filename, 'w') as f:
            json.dump(tasks_dict, f, indent=2)
    
    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                tasks_dict = json.load(f)
                
            # Convert dictionaries back to Task objects
            self.tasks = []
            for task_dict in tasks_dict:
                task = Task(
                    task_dict["title"],
                    task_dict["description"],
                    task_dict["due_date"]
                )
                task.completed = task_dict["completed"]
                task.created_at = task_dict["created_at"]
                self.tasks.append(task)
        except FileNotFoundError:
            self.tasks = []  # Start with empty list if no file exists

    def list_tasks(self):
        return self.tasks

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            self.save_tasks()
            return True
        return False

# Let's use our TaskManager:
def main():
    manager = TaskManager()
    
    # Add some tasks
    manager.add_task(
        "Learn Serialization", 
        "Practice Python serialization with JSON",
        "2024-02-20"
    )
    manager.add_task(
        "Build Project", 
        "Create a small project using new skills"
    )
    
    # List all tasks
    print("\nCurrent Tasks:")
    for i, task in enumerate(manager.list_tasks()):
        status = "✓" if task.completed else " "
        print(f"{i+1}. [{status}] {task.title} - {task.description}")
        print(f"   Created: {task.created_at}")
        if task.due_date:
            print(f"   Due: {task.due_date}")
        print()
    
    # Mark first task as completed
    manager.mark_completed(0)
    
    # List tasks again to see the change
    print("\nAfter marking first task complete:")
    for i, task in enumerate(manager.list_tasks()):
        status = "✓" if task.completed else " "
        print(f"{i+1}. [{status}] {task.title}")

if __name__ == "__main__":
    main()
