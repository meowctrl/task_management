from datetime import datetime

# Import validation functions
from .validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    error = validate_task_title(title)
    if error:
        print(error)
        return
    error = validate_task_description(description)
    if error:
        print(error)
        return
    error = validate_due_date(due_date)
    if error:
        print(error)
        return
    try:
        task = {
            'title': title,
            'description': description,
            'due_date': due_date,
            'status': 'pending'
        }
        tasks.append(task)
        print("Task added successfully!")
    except Exception as e:
        print(f"Error adding task: {e}")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index):
    try:
        if 0 <= index < len(tasks):
            tasks[index]['status'] = 'completed'
            print("Task marked as complete!")
        else:
            print("Invalid index")
    except (IndexError, TypeError) as e:
        print(f"Error marking task as complete: {e}")
    
# Implement view_pending_tasks function
def view_pending_tasks():
    try:
        pending = [t for t in tasks if t.get('status') == 'pending']
        if not pending:
            print("No pending tasks.")
        else:
            for i, task in enumerate(pending):
                title = task.get('title', 'Unknown')
                desc = task.get('description', 'No description')
                due = task.get('due_date', 'No due date')
                print(f"{i+1}. {title} - {desc} - Due: {due}")
    except Exception as e:
        print(f"Error viewing pending tasks: {e}")

# Implement calculate_progress function
def calculate_progress(tasks_list):
        if not tasks_list:
            return 0
        completed = sum(1 for t in tasks_list if t.get('status') == 'completed')
        return (completed / len(tasks_list)) * 100