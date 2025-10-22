from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Pending')
    user_id = db.Column(db.String(100),db.ForeignKey('user.username'))
    def __repr__(self):
        return f"<Task {self.id} - {self.title}>"

class User(db.Model):
    username = db.Column(db.String(100), primary_key=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task',backref='user',lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"