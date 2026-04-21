from datetime import datetime

def validate_task_title(title):
    if not title or not isinstance(title, str):
        return "Title must be a non-empty string."
    return None
    
def validate_task_description(description):
    if not description or not isinstance(description, str):
        return "Description must be a non-empty string."
    return None    
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, '%Y-%m-%d')
        return None
    except ValueError:
        return "Due date must be in YYYY-MM-DD format."