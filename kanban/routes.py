from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from kanban import db, app

class database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(20))
    category = db.Column(db.String(20))
    
    def __init__(self, task, category):
        self.task = task
        self.category = category
        
#Run line below in case you lose the database for whatever reason
#db.create_all()
 


@app.route('/')
def main():
    tasks = database.query.filter_by(category='To do')
    tasks_doing = database.query.filter_by(category='Doing')
    tasks_done = database.query.filter_by(category='Done')
    all_data = database.query.all()
    return render_template('kanban.html', tasks=tasks, all_data=all_data, tasks_doing=tasks_doing, tasks_done=tasks_done)

@app.route('/add', methods=['POST'])
def add():
    if len(request.form['new_task']) == 0:
        return (redirect(url_for('main')))
    task = request.form['new_task']
    category = request.form['category']
    actual_task = database(task, category)
    db.session.add(actual_task)
    db.session.commit()
    return (redirect(url_for('main')))

@app.route('/move', methods=['POST'])
def move():
    if len(request.form['move_task']) == 0:
        return (redirect(url_for('main')))
    move_task = request.form['move_task']
    new_column = request.form['move_column']
    task = database.query.filter_by(task=move_task).first()
    task.category = new_column
    db.session.commit()
    return (redirect(url_for('main')))

	
@app.route('/delete', methods=['POST'])
def delete():
    task = request.form['delete_task']
    task = database.query.filter_by(task=task).first()
    db.session.delete(task)
    db.session.commit()
    return (redirect(url_for('main')))


