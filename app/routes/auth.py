from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from app import db
from app.models import User 

auth_bp = Blueprint('auth',__name__)



@auth_bp.route('/login',methods=['POST','GET'])
def login():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.get(username)
    if user and password == user.password:
      session['user'] = username
      flash('Login Succesfull','success')
      return render_template('tasks.html')
    else:
      flash('Invalid username or password','danger')
  return render_template('login.html')

@auth_bp.route('/logout')
def logout():
  session.pop('user',None)
  flash('Logged Out','info')
  return redirect(url_for('auth.login'))

@auth_bp.route('/register',methods=['POST','GET'])
def register():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.get(username)
    if user:
      flash("User already exists please login\n")
      return redirect(url_for('auth.login'))
    else:
      new_user = User(username=username,password=password)
      db.session.add(new_user)
      db.session.commit()
      flash('Registered Successfully, Please login now\n')
      return redirect(url_for('auth.login'))
  return render_template('register.html')
