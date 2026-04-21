from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        return "Title must be a non-empty string."
    if len(title) > 100:
        return "Title must be 100 characters or less."
    return None
    
def validate_task_description(description):
    if not isinstance(description, str) or not description.strip():
        return "Description must be a non-empty string."
    if len(description) > 500:
        return "Description must be 500 characters or less."
    return None    
    
def validate_due_date(due_date):
    try:
        parsed_date = datetime.strptime(due_date, '%Y-%m-%d')
        if parsed_date.date() < datetime.now().date():
            return "Due date cannot be in the past."
        return None
    except ValueError:
        return "Due date must be in YYYY-MM-DD format."