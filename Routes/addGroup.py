from flask.blueprints import Blueprint
from flask import render_template
from flask import request
from managers.dbService import DatabaseManager
from extensions import db

db_manager = DatabaseManager(db)

addGroup = Blueprint('addGroup', __name__,
                     template_folder='templates',
                     static_folder='static')


@addGroup.route('/addGroup')
def getGroupTemplate():
    return render_template('addGroup.html')


@addGroup.route('/addGroup', methods=['post', 'get'])
def addGroupRoute():
    if request.method == 'POST':
        name = request.form.get('name')

    if name:
        message = "Correct data"
        db_manager.add_group(name=name)
    else:
        message = "Wrong data"

    return render_template('addGroup.html', message=message)
