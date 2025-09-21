from flask import Blueprint, request, jsonify
from . import store

todo_bluePrint = Blueprint("todos", __name__)

@todo_bluePrint.route("/", methods=["POST"])
def create_todo():
    data = request.json
    if not data or "title" not in data:
        # 400 status code for bad request
        return jsonify({"err": "Title is required to serve this request"}), 400
    todo = store.create(data["title"])
    # 201 created status code for POST API
    return jsonify(todo), 201

@todo_bluePrint.route("/", methods=["GET"])
def get_todos():
    return jsonify(store.getall())

@todo_bluePrint.route("/<int:id>", methods=["GET"])
def get_todo(id):
    todo = store.get_one(id)
    if not todo:
        return jsonify({"error": "id not present in todo list!"}), 404
    return jsonify(todo)

@todo_bluePrint.route("/<int:id>", methods=["PUT"])
def update_todo(id):
    data = request.json
    todo = store.update(id, data)
    if not todo:
        return jsonify({"error": "id not present in todo list!"}), 404
    return jsonify(todo)

@todo_bluePrint.route("/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = store.delete(id)
    if not todo:
        return jsonify({"error": "id not present in todo list!"}), 404
    return jsonify({"msg ": "todo deleted successfully!!"})