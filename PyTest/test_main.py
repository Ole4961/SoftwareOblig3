import main

# These test tests for a year being a leap year
# Testing for if a year is divisible by 4 by not by 100

def testTrue4False100():
    assert main.isLeapYear(2008) == False
    assert main.isLeapYear(2001) == False

# Testing for if a year is divisible by 400
def testTrue400():
    assert main.isLeapYear(1600) == True
    assert main.isLeapYear(1967) == False


# These test tests for a year not being a leap year
# Testing for if a year is not divisible by 4
def testFalse4():
    assert main.isLeapYear(2000) == True
    assert main.isLeapYear(2003) == False

# Testing for if a year is divisible by 100 but not by 400
def testTrue100False400():
    assert main.isLeapYear(2000) == True
    assert main.isLeapYear(2009) == False
