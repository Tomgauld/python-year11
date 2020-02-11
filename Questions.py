answer = "y"
while answer == "y":
    score = 0
    answer = input("What is sound measured as?")
    if answer == "hz":
        print("You are correct!")
        score = score + 1
    else:
        print("You are incorrect! The answer was 'hz'")
        score = score + 0

    answer = input("How many pixels are in an image of 300x200?")
    if answer == "60000":
        print("You are correct!")
        score = score + 1
    else:
        print("You are incorrect! The answer was '60000' ")
        score = score + 0

    answer = input("Are all sounds caused by vibrations?")
    if answer == "yes":
        print("You are correct!")
        score = score + 1
    else:
        print("You are incorrect! The answer was 'yes'")
        score = score + 0

    answer = input("What waves are sound?")
    if answer == "soundwaves":
        print("You are correct!")
        score = score + 1
    else:
        print("You are incorrect!")
        score = score + 0

    answer = input("If there is a sample rate of 44.1kHz, how many times per second is the sample rate going ?")
    if answer == "44100":
        print("You are correct!")
        score = score + 1
    else:
        print("You are incorrect!")
        score = score + 0

    answer = input("What is: VOXXYX MRKCO?")
    if answer == "lennon chase":
        

        print("You correctly answered:")
        print(score)
        
    answer = input("Restart?")

while True:
    if answer in ("y", "n"):
        break
    print ("Invalid input.")
    if answer == "y":
        continue
    else:
        print ("Goodbye")
        break

