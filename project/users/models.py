from project import db


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(128), nullable=False, unique=True)
	email = db.Column(db.String(128), nullable=False, unique=True)

	def __init__(self, username, email, *args, **kwargs):
		self.username = username
		self.email = email
