# Patric Natindim
# March 12 2025

# Checks if the input year is a leap year

def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

year_input = int(input("Year: "))

if leap_year(year_input):
    print("True")
else:
    print("False")
