from flask.blueprints import Blueprint
from flask import render_template
from flask import request
from models.lecturer import Lecturer
from models.subject import Subject
from models.interval import Interval
from models.group import Group
from managers.dbService import DatabaseManager
from extensions import db

db_manager = DatabaseManager(db)

addNote = Blueprint('addNote', __name__,
                    template_folder='templates',
                    static_folder='static')


@addNote.route('/addNote')
def getNoteTemplate():
    return render_template('addNote.html', lecturers=Lecturer.query.all(), groups=Group.query.all(),
                           intervals=Interval.query.all(), subjects=Subject.query.all())


@addNote.route('/addNote', methods=['post', 'get'])
def addNoteRoute():
    if request.method == 'POST':
        interval = request.form.get('interval')
        chet = request.form.get('chet')
        day = request.form.get('day')
        subject = request.form.get('subject')
        lecturer = request.form.get('lecturer')
        group = request.form.get('group')

    if interval and subject and lecturer and group and chet and day:
        message = "Correct data"
        new_dict = {}
        new_dict["lect"] = lecturer
        new_dict["subj"] = subject
        new_dict["interv"] = interval
        new_dict["group"] = group
        new = lecturer.split()
        name = new[1]
        l_name = new[0]
        s_name = new[2]
        lecturer_id = db.session.query(Lecturer.id).filter(Lecturer.name == name, Lecturer.last_name == l_name,
                                                           Lecturer.surname == s_name).first()[0]
        group_id = db.session.query(Group.id).filter(Group.name == group).first()[0]
        subject_id = db.session.query(Subject.id).filter(Subject.subject_name == subject).first()[0]
        interval_id = db.session.query(Interval.id).filter(Interval.interval == interval).first()[0]
        db_manager.add_schedule(day=day, chet=chet, group_id=group_id, interval_id=interval_id, subject_id=subject_id,
                                lecturer_id=lecturer_id)
    else:
        message = "Wrong data"

    return render_template('addNote.html', message=message, prob=" ", lecturers=Lecturer.query.all(),
                           groups=Group.query.all(), intervals=Interval.query.all(), subjects=Subject.query.all())
