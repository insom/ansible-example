from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
