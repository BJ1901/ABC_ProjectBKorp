from flask.blueprints import Blueprint
from flask import render_template
from models.lecturer import Lecturer
import datetime
from flask import request
from models.subject import Subject
from models.interval import Interval
from models.group import Group
from models.schedule import Schedule
from managers.dbService import DatabaseManager
from extensions import db

db_manager = DatabaseManager(db)

lecturers = Blueprint('lecturers', __name__,
                      template_folder='templates',
                      static_folder='static')


@lecturers.route('/')
def index():
    first = datetime.datetime.strptime("09.11.2020", "%d.%m.%Y")
    today = datetime.date.today()
    now = datetime.datetime.now()
    razn = ((now - first).days)

    if (razn // 7) % 2 == 0:
        todned = "Нечетная"
    else:
        todned = "Четная"
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    trv = ['9:30 - 11:05', '11:20 - 12:55', '13:10 - 14:45', '15:25 - 17:00']
    cur_group = "БФИ1801"
    group_id = db.session.query(Group.id).filter(Group.name == cur_group).first()[0]
    schedule = db.session.query(Schedule).filter(Schedule.group_id == group_id)
    return render_template('index.html', curdate=today.strftime('%d-%m-%Y'), todned=todned, cur_group=cur_group,
                           days=days, trvs=trv, lecturers=Lecturer.query.all(), subjects=Subject.query.all(),
                           intervals=Interval.query.all(), group_names=Group.query.all(), schedules=schedule)


@lecturers.route('/', methods=['post', 'get'])
def chooseGroup():
    if request.method == 'POST':
        cur_group = request.form.get('cur_group')

    first = datetime.datetime.strptime("09.11.2020", "%d.%m.%Y")
    today = datetime.date.today()
    now = datetime.datetime.now()
    razn = ((now - first).days)

    if (razn // 7) % 2 == 0:
        todned = "Нечетная"
    else:
        todned = "Четная"
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    trv = ['9:30 - 11:05', '11:20 - 12:55', '13:10 - 14:45', '15:25 - 17:00']
    message = ''
    group_id = db.session.query(Group.id).filter(Group.name == cur_group).first()[0]
    schedule = db.session.query(Schedule).filter(Schedule.group_id == group_id)

    return render_template('index.html', curdate=today.strftime('%d-%m-%Y'), cur_group=cur_group, todned=todned,
                           days=days, trvs=trv, lecturers=Lecturer.query.all(), subjects=Subject.query.all(),
                           intervals=Interval.query.all(), group_names=Group.query.all(), schedules=schedule)
