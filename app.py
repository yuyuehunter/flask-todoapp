from flask import (
    Flask, 
    render_template, 
    request, 
    redirect
)
from db import Database

app = Flask(__name__)
db = Database('todoapp').db

@app.route('/', methods=['GET', 'POST'])
def index():
    task = None
    tasks = []
    if request.method == 'POST':
        task = request.form['task']
        db.task.insert({"descript": task, "status": "TODO"})
        return redirect('/', code=302)

    for t in db.task.find():
        tasks.append(t)

    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
