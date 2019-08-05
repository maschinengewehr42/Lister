#01.07.2019 15:34 "drugpedia v0.01a create 'main' file"
#02.07.2019 23:26 "drugpedia v0.02a main upgrade"
#03.07.2019 23:46 "drugpedia v0.03a main upgrade"
#04.07.2019 13:43 "drugpedia v0.04a main upgrade"
#04.07.2019 20:08 "drugpedia v0.10a create 'content_control' file"
#07.07.2019 00:48 "drugpedia v0.12a create 'menu' file"
#09.07.2019 13:43 "drugpedia v0.14a menu and content_control upgrade"
#10.07.2019 00:23 "drugpedia v0.19a data base problem fixed"
#10.07.2019 00:54 "drugpedia v0.22a add method writed"
#13.07.2019 14:47 "drugpedia v0.25a edt method writed and other upgrade"
#13.07.2019 16:30 "drugpedia v0.30a create 'content_view' file and development started"
#14.07.2019 00:50 "drugpedia v0.5a upgrade a 'content_view' file and upgrade 'syshen' file"
#14.07.2019 05:39 "drugpedia v0.6a create a 'db_creator' file and code"
#15.07.2019 15:50 "drugpedia v0.7a upgrade 'content_view'"

import sqlite3 #DB
import syshen as s #cls\dec
from menu import Menu

class LoginSystem():

	def __init__(self, action=None, login=None, password=None, mail=None):
		self.action=action
		self.login=login
		self.password=password
		self.mail=mail

	def auth(self, login=None, password=None):
		while True:
			conn=sqlite3.connect('user_DB.sqlite3')
			c=conn.cursor()
			s.cls(),s.dec(11), print("Авторизация"),s.dec(11)
			self.login=input("логин: ")
			if self.login == "0" or self.login == "exit":
				self.home()
				break
			c.execute("SELECT mail FROM user WHERE mail == '%s';" % (self.login))
			if c.fetchone() == None: s.cls(), s.dec(6), print("Ошибка"), s.dec(6),inpu()#####
			else:
				self.password=input("пароль: ")
				c.execute("SELECT password FROM user WHERE password == '%s';" % (self.password))
				if c.fetchone() == None: s.cls(), s.dec(6), print("Ошибка"), s.dec(6),input() #####
				else:
					c.close(), conn.close()
					m.menu()
					
	def regs(self):
		while True:
			conn=sqlite3.connect('user_DB.sqlite3')
			c=conn.cursor()
			s.cls(),s.dec(11), print("Регистрация"),s.dec(11)
			self.mail=input("Почтовый адрес: ")
			if self.mail == "0":
				c.close(), conn.close()
				return
			self.login=input("Имя: ")
			if self.login == "0":
				c.close(), conn.close()
				return
			self.password=input("Пароль: ")
			if self.password == "0":
				c.close(), conn.close()
				return
			c.execute("INSERT INTO user (mail, name, password) VALUES ('%s', '%s', '%s')" %(self.mail, self.login, self.password))
			conn.commit()
			s.cls(), s.dec(14), print("запись сделана"), s.dec(14), input()
			c.close(), conn.close()
			self.home()
			break

	def home(self):
		while True:
			s.cls(),s.dec(8), print("Домашняя"),s.dec(8)
			self.action=input("1.Вход\n2.Регистрация\n\nВыполнить: ")
			if self.action=="1": #authentick
				s.cls(), self.auth(None)
				break
			elif self.action=="2": #register
				s.cls(), self.regs()
				break
			elif self.action=="0" or self.action=="exit":
				s.cls()
				self.action=input("Выход? y/n: ")
				if self.action=="y" or self.action=="Y":				
					s.cls()
					break
				elif self.action=="n" or self.action=="N":
					s.cls()
					continue
			elif self.action=="cls": s.cls() #####
			else: s.cls(), s.dec(6), print("Ошибка"), s.dec(6), input()#####
		return

m=Menu()
ls=LoginSystem()
ls.home()