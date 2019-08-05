import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def dec(x=10):
	string=x*'-'
	print(string)