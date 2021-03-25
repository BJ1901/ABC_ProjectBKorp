from extensions import db


class Schedule(db.Model):
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(30), nullable=False)
    chet = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    interval_id = db.Column(db.Integer, db.ForeignKey('interval.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturer.id'))
