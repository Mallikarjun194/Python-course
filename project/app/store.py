
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

def getall():
    return list(todos.values())

def get_one(id):
    return todos.get(id)

def update(id, data):
    if id in todos:
        todos[id]["completed"] = data.get("completed", todos[id]["completed"])
        return todos[id]
    return None

def delete(id):
    return todos.pop(id, None)