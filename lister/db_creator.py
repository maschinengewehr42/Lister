import sqlite3

class CreateDB():

	def __init__(self, action=None):
		self.action=action

	def create_db(self):
		while True:
			self.action=input('Имя БД: ')
			name_db=self.action+'.sqlite3'
			conn = sqlite3.connect(name_db)
			c = conn.cursor()
			c.execute("CREATE TABLE 'content' ('ID'	INTEGER PRIMARY KEY AUTOINCREMENT,'title' TEXT,'post' TEXT);")
			conn.commit(),c.close(),conn.close(),print('Готово')
			return

c_db=CreateDB()
c_db.create_db()