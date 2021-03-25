from flask.blueprints import Blueprint
from flask import render_template
from models.interval import Interval

intervals = Blueprint('intervals', __name__,
                      template_folder='templates',
                      static_folder='static')


@intervals.route('/intervals')
def index():
    return render_template('intervals.html', intervals=Interval.query.all())
