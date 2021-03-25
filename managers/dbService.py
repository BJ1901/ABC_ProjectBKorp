from models.lecturer import Lecturer
from models.interval import Interval
from models.group import Group
from models.subject import Subject
from models.schedule import Schedule


class DatabaseManager:
    def __init__(self, db):
        self.db = db

    def add_lecturer(self, **kwargs):
        lecturer = Lecturer(name=kwargs["name"],
                            last_name=kwargs["last_name"],
                            surname=kwargs["surname"]
                            )
        self.db.session.add(lecturer)
        self.db.session.commit()

    def add_interval(self, **kwargs):
        interval = Interval(interval=kwargs["interval"],
                            )
        self.db.session.add(interval)
        self.db.session.commit()

    def add_group(self, **kwargs):
        group = Group(name=kwargs["name"],
                      )
        self.db.session.add(group)
        self.db.session.commit()

    def add_subject(self, **kwargs):
        subject = Subject(subject_name=kwargs["subject_name"],
                          )
        self.db.session.add(subject)
        self.db.session.commit()

    def add_schedule(self, **kwargs):
        schedule = Schedule(day=kwargs["day"],
                            chet=kwargs["chet"],
                            group_id=kwargs["group_id"],
                            interval_id=kwargs["interval_id"],
                            subject_id=kwargs["subject_id"],
                            lecturer_id=kwargs["lecturer_id"]
                            )
        self.db.session.add(schedule)
        self.db.session.commit()
