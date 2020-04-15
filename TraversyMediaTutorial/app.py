from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import enum

app = Flask(__name__)

# ENV = 'dev'

# if ENV == 'dev':
#     app.debug = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/'
# else:
#     app.debug = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zdusfgilvmvztn:6a5c41e348a2a9449c38fd7c3532f0abacb26fdd3a305a7844e2ec490fc7461b@ec2-34-206-252-187.compute-1.amazonaws.com:5432/d518oc8r85gqr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Kinds(enum.Enum):
    Yoga = 1
    Running = 2
    Bodyweight = 3


class App(db.Model):
          __tablename__ = 'trainers'
          id = db.Column(db.Integer, primary_key=True)
          trainer = db.Column(db.String(200))
          kinds = db.Column(db.Enum(Kinds))

          def __init__(self, trainer, kinds):
              self.trainer = trainer
              self.kinds = kinds



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        trainer = request.form['trainer']
        kind = request.form['kind']
        if trainer =='' or kind == '':
            return render_template('/index.html', message = 'Please enter required fields')
        return render_template('success.html')

if __name__ == '__main__':
    app.run()


