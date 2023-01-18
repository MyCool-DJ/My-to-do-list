def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 

while True:
  menu = input("add or remove?: )
  if menu = "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.add(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(list)
    else:
      print("{item} was not in the list)
  printList()