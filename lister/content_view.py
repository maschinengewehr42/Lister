import sqlite3 #DB
import syshen as s #cls\dec

class ContentView():

	def __init__(self, action=None):
		self.action=action

	def view(self):
		while True:
			conn=sqlite3.connect('content_DB.sqlite3')
			c=conn.cursor()
			c.execute("SELECT title FROM content;")
			db=c.fetchall()
			for i in range(1,len(db)+1):
				string=str(i)+'.'
				db_non_list=db[i-1]
				print(string,''.join(db_non_list))
				if i==len(db): break
			try:
				self.action=int(input("Выполнить: "))
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
					c.execute("SELECT title, post FROM content WHERE ID=='%s';"%(self.action))
					post=c.fetchone()
					s.cls(),s.dec(),print(post[0]),s.dec(),print(post[1]),s.dec(),c.close(),conn.close(),input()
					break		

	def menu(self):
		while True:
			s.cls(),s.dec(22), print("Меню просмотра записей"),s.dec(22)
			self.action=input("1.Смотреть записи\n\nВыполнить: ")
			if self.action=="1":
				s.cls(), self.view()
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