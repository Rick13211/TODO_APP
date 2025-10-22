from flask import Blueprint, render_template, request,redirect,url_for,flash,session

from app import db
from app.models import Task

tasks_bp = Blueprint('tasks',__name__)

@tasks_bp.route('/')
def view_tasks():
  if 'user' not in session:
    return redirect(url_for('auth.login'))
  username = session['user']
  tasks = Task.query.filter_by(user_id=username).all()
  return render_template('tasks.html',tasks=tasks)

@tasks_bp.route('/add',methods=['POST'])
def add_task():
  if 'user' not in session:
    return redirect(url_for('auth.login'))
  username = session['user']
  title = request.form.get('title')
  if title:
    new_task = Task(title=title,status='Pending',user_id=username)
    db.session.add(new_task)
    db.session.commit()
    flash('Task Added Successfully','success')
  return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
  task = Task.query.get(task_id)
  if task:
    if task.status == 'Pending':
      task.status = 'Working'
    elif task.status == 'Working':
      task.status = 'Done'
    elif task.status == 'Done':
      task.status = 'Pending'
    db.session.commit()
  return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear',methods=['POST'])
def clear_tasks():
  username = session['user']
  Task.query.filter_by(user_id=username).delete()
  db.session.commit()
  flash('ALL TASKS CLEARED','info')
  return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
  task = Task.query.get(task_id)
  if task and task.user_id == session.get('user'):
    db.session.delete(task)
    db.session.commit()
    flash("Task Deleted Successfully",'info')
    
    flash('Task does not exist')
  return redirect(url_for('tasks.view_tasks'))

