#!flask/bin/python
from flask import Flask, jsonify, make_response, abort
from formula import *

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/neato', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
    
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
	
@app.route('/chitown/<int:distance>/<int:velocity>', methods=['GET'])
def get_wait(distance, velocity):
    wait = chi_town_wait(distance, velocity)
    return jsonify({'wait': wait})
    
if __name__ == '__main__':
    app.run(debug=True)