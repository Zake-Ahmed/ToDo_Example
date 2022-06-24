from application import app, db
from application.models import ToDos
from flask import redirect, url_for, render_template

@app.route('/')
def index():
    todo = ToDos.query.all()
    # empstr = ""
    # for t in todo:
    #     empstr += f'{t.id} {t.task}  {t.completed} <br>' 
    # return empstr
    return render_template("task.html", todos=todo)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/add/<t>')
def add(t):
    newtask = ToDos(task=t)
    db.session.add(newtask)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete(id):
    todo = ToDos.query.get(id)
    todo.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:id>')
def incomplete(id):
    todo = ToDos.query.get(id)
    todo.completed = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>/<newtask>')
def update(id, newtask):
    todo = ToDos.query.get(id)
    todo.task = newtask
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<deltask>')
def delete(deltask):
    todo = ToDos.query.filter_by(task=deltask).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))
