#12 days of Christmas
def song(day):
    print("On the ", dayNum[day-1], " day of Christmas my true love gave to me ")
    for i in range(day,0,-1):
        print(i)
        print(lines[4-i])

    if day > 0:
        day = day+1
        song(day)

lines = ["A partridge in a pear tree","Two turtle doves", "Three French Hens", "Four Calling Birds", "Five Gold Rings"]
dayNum = ["1st", "2nd", "3rd", "4th"]
song(1)


        

    
