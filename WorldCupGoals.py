mylist = ["England", "France", "Germany"]

while team != "x"
team = input("Enter a team name")
for i in range(0, len(mylist)):
    if team == mylist[i][0]:
        print("Total goals: ", mylist [i][0])
        

