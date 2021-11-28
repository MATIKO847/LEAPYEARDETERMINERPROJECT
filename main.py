# The code below takes the string input of the year and converts it to an integer
year = int(input("Which year do you want to check? "))
19
# The code below determines the diviscibilty of the input year by finding the remainder
div_by_4 = year % 4
div_by_100 = year % 100
div_by_400 = year % 100

if div_by_4 == 0:
    if div_by_100 != 0 :
        print("leap year")
    else :
        if div_by_400 == 0 :
            print("leap year")
        else :
            print("not leap year")
else :
    print("Not Leap year")
