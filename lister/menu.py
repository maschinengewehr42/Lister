import syshen as s #cls\dec
from content_control import ContentControl
from content_view import ContentView

cc=ContentControl()
cv=ContentView()

class Menu():
	def __init__(self, action=None):
		self.action=action

	def menu(self):
		while True:
			s.cls(),s.dec(12), print("Главное меню"),s.dec(12)
			self.action=input("1.Редактор базы данных\n2.Справочник\n\nВыполнить: ")
			if self.action=="1":
				s.cls(), cc.menu() ##редактор БД##
				break
			elif self.action=="2":
				s.cls(), cv.menu()##справочник##
				break
			elif self.action=="0" or self.action=="exit":
				s.cls()
				self.action=input("Выход на начальную страницу страницу? y/n: ")
				if self.action=="y" or self.action=="Y":				
					s.cls()	
					break
				elif self.action=="n" or self.action=="N":
					s.cls()
					continue
			elif self.action=="cls": s.cls() #####
			else: s.cls(), s.dec(6), print("Ошибка"), s.dec(6), input()#####
		