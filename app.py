

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from Routes.lectures import lecturers
from Routes.groups import groups
from Routes.addLecturer import addLecturer
from Routes.addNote import addNote
from Routes.addGroup import addGroup
from Routes.addSubject import addSubject

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.register_blueprint(lecturers)
app.register_blueprint(groups)
app.register_blueprint(addLecturer)
app.register_blueprint(addNote)
app.register_blueprint(addGroup)
app.register_blueprint(addSubject)

if __name__ == "__main__":

    app.run()
