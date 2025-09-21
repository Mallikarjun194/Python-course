
todos = {}
current_id = 1

def create(title):
    global current_id
    todo = {
        "id": current_id,
        "title": title,
        "completed": False
    }
    todos[current_id] = todo
    current_id = current_id + 1
    return todo