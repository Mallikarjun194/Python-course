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
