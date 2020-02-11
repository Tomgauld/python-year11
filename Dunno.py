import random


print("rolling...")

def roll(a,b):
    a = int(random.randint(1,6))
    print("Your first Die is:", a)
    b = int(random.randint(1,6))
    print("Your second Die is:", b)
    score = (a + b)
    print ("Both your numbers added are:", int(score))


roll(0,0)

answer = input("Do you want to roll again?")
if answer == "yes":
    roll(0,0)
    


