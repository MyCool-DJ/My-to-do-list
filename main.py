import os, time

myAgenda = []

def printList():
	print()
	for item in myAgenda:
		print(item)
	print()

while True:
	menu = input("add or remove item? ")
	if menu == "add":
		item = input("What's next on the Agenda? ")
		myAgenda.append(item)
	elif menu == "remove":
		item = input("What do you want to remove? ")
		myAgenda.remove(item)
	printList()

sleep.time(1.5)
os.system("clear")