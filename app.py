from flask import (
    Flask, 
    render_template, 
    request, 
    redirect
)
from bson.objectid import ObjectId
from db import Database

app = Flask(__name__)
db = Database('todoapp').db

@app.route('/', methods=['GET', 'POST'])
def index():
    task = None
    tasks = []
    if request.method == 'POST':
        if request.form['form_name'] == 'add':
            task = request.form['task']
            db.task.insert({"descript": task, "status": "TODO"})
            return redirect('/', code=302)

        if request.form['form_name'] == 'edit_task':
            old_task = request.form['old_task']
            new_task = request.form['task']
            db.task.update({'descript': old_task}, {'$set': {'descript': new_task}})
            return redirect('/', code=302)

        if request.form['form_name'] == 'delete_task':
            task_id = request.form['task_id']
            db.task.remove({'_id': ObjectId(task_id)})
            return redirect('/', code=302)

    for t in db.task.find():
        tasks.append(t)

    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
