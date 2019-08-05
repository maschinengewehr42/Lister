import sqlite3 #DB
import syshen as s #cls\dec

class ContentControl():

	def __init__(self, action=None, title=None, text=None):
		self.action=action
		self.title=title
		self.text=text

	def edt(self):
		while True:
			conn = sqlite3.connect('content_DB.sqlite3')
			c = conn.cursor()
			try:
				self.action=int(input("ID изменяемой записи: "))
			except ValueError:
				s.cls(), s.dec(), print('Ошибка'),s.dec(),input(),c.close(),conn.close()
				continue
			else:
				if self.action==0: break
				c.execute("SELECT ID FROM content WHERE ID == '%s';" % (self.action))
				if c.fetchone()==None: 
					s.cls(), s.dec(6), print('Ошибка'),s.dec(6),input(),c.close(),conn.close()
					continue
				else:
					self.title=input("Заголовок поста: ")
					if len(self.title)>30:
						s.cls(),s.dec(25),print('Слишком большой заголовок'),s.dec(25),input(),c.close(),conn.close()
						continue
					elif self.title=="0": return #####
					else: 
						self.text=input("Текст поста: ")
						if self.text!='0':
							c.execute("UPDATE content SET post='%s',title='%s' WHERE ID == %s;" % ( self.text,self.title,self.action,))
							conn.commit(),s.cls(),s.dec(6),print('Готово'),s.dec(6),input(),c.close(),conn.close()
							break
						else:
							break
			
	def add(self):
		while True:
			conn = sqlite3.connect('content_DB.sqlite3')
			c = conn.cursor()
			self.title=input("Заголовок поста: ")
			if len(self.title)>30:
				s.cls(),s.dec(25),print('Слишком большой заголовок'),s.dec(25),input(),c.close(),conn.close()
				continue
			elif self.title=="0": return #####
			else:
				self.text=input("Текст поста: ")
				c.execute("INSERT INTO content (title, post) VALUES ('%s', '%s')"%(self.title, self.text))
				conn.commit(),s.cls(),s.dec(6),print('Готово'),s.dec(6),input(),c.close(),conn.close()
				return

	def dlt(self):
		while True:
			conn = sqlite3.connect('content_DB.sqlite3')
			c = conn.cursor()
			try:
				self.action=int(input("ID удаляемой записи: "))
			except ValueError:
				s.cls(), s.dec(6), print('Ошибка'),s.dec(6),input(),c.close(),conn.close()
				continue
			else:
				if self.action==0: break
				c.execute("SELECT ID FROM content WHERE ID == '%s';" % (self.action))
				if c.fetchone()==None: 
					s.cls(), s.dec(6), print('Ошибка'),s.dec(6),input(),c.close(),conn.close()
					continue
				else:
					c.execute("UPDATE content SET post='удалённая запись' WHERE ID == %s;" % (self.action))
					conn.commit(),s.cls(),s.dec(6),print("Готово"),s.dec(6),input(),c.close(),conn.close()
					break

	def menu(self):
		while True:
			s.cls(),s.dec(), print("Меню редактора БД"),s.dec()
			self.action=input("1.Новая запись\n2.Удалить запись\n3.Изменить существующую запись\n\nВыполнить: ")
			if self.action=="1":
				s.cls(), self.add()
			elif self.action=="2":
				s.cls(), self.dlt()
			elif self.action=="3":
				s.cls(), self.edt()
			elif self.action=="0" or self.action=="exit":
				s.cls()
				self.action=input("Выход на предыдущую страницу? y/n: ")
				if self.action=="y" or self.action=="Y":				
					s.cls()	
					break
				elif self.action=="n" or self.action=="N":
					s.cls()
					continue
			elif self.action=="cls": s.cls() #####
			else: s.cls(), s.dec(6), print("Ошибка"), s.dec(6), input() #####
		return