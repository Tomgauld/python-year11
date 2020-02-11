newItem = ""
ans = ""

XmasList = file = open("ChristmasList.txt", "r")

myList = []

for line in XmasList:
    myList.append(line)

print("Here is the list ",myList)

XmasList.close()

XmasList = file = open("ChristmasList.txt", "a")


ans = input("Would you like to add to the list? Y/N")
if ans == "Y" or ans == "y":
    newItem = input("What would you like to add?")
    
    myList.append(newItem)
    


for item in myList:
    XmasList.write(item+"\n")

XmasList.close()
XmasList.reset()