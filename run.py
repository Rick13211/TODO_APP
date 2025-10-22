
from app import createApp,db

from app.models import Task
app = createApp()

with app.app_context():
  db.drop_all()
  db.create_all()

if __name__ == "__main__":
  app.run(debug=True)