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
    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'status': 'pending'
    }
    tasks.append(task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]['status'] = 'completed'
        print("Task marked as complete!")
    else:
        print("Invalid index")
    
# Implement view_pending_tasks function
def view_pending_tasks():
    pending = [t for t in tasks if t['status'] == 'pending']
    if not pending:
        print("No pending tasks.")
    else:
        for i, task in enumerate(pending):
            print(f"{i+1}. {task['title']} - {task['description']} - Due: {task['due_date']}")

# Implement calculate_progress function
def calculate_progress():
    if not tasks:
        return 0
    completed = sum(1 for t in tasks if t['status'] == 'completed')
    return (completed / len(tasks)) * 100