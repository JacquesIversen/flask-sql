from taskmanager import db


class Catagory(db.model):
    # Schema for the Catagory model
    id = db.column(db.Integer, primary_key=True)
    catagory_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="catagory", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string 
        return self.catagory_name


class Task(db.Model):
    # schema for the task model
    id = d.Column(db.Interger, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_describtion = db.Column(db.Column(db.text, nullable=False))
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    catagory_id = db.Column(db.Integer, db.ForeignKey("catagory.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string 
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.tesk_name, self.is_urgent
        )