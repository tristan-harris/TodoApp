from flask import request, render_template, redirect, current_app, jsonify, make_response
from flaskapp import db, app
from flaskapp.models import Todo
from flaskapp.utils import json_error_response



@app.route('/')
def index():
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', tasks=tasks)


@app.route('/api', methods=['POST'])
def api():
    req = request.get_json()
    res = make_response(jsonify({"message":"recieved"}), 200)
    return res


@app.route('/delete', methods=['POST'])
def delete():
    req = request.get_json()
    task_to_delete = Todo.query.get_or_404(req['todo-id'])
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        res = make_response(jsonify({"message":"todo deleted"}), 200)
        return res
    except:
        return json_error_response('There was a problem deleting that task')


@app.route('/completed', methods=['POST'])
def card_completed():
    req = request.get_json()
    task = Todo.query.get_or_404(req['todo-id'])
    task.completed = req['todo-completed']
    try:
        db.session.commit()
        res = make_response(jsonify({"message":"todo completed status updated"}), 200)
        return res
    except:
        return json_error_response('There was a problem updating that task')


@app.route('/create', methods=['POST'])
def create_todo():
    req = request.get_json()
    new_todo = Todo(content=req['todo-title']);
    try:
        db.session.add(new_todo)
        db.session.commit()
        res = make_response(jsonify({"message":"todo added"}), 200)
        return res
    except:
        return json_error_response('Could not create todo')
