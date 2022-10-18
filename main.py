
year = 2008


def isLeapYear(year):
    userInput = year
    # userInput = int(input("Which year do you wanna test: "))
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print("\nThe year " + str(year) + " is a leap year!")
        return True
    elif (year % 4 != 0 and year % 100 == 0 or year % 400 != 0):
        print("\nThe year " + str(year) + " isn't a leap year!")
        return False


isLeapYear(year)
