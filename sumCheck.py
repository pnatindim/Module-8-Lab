# Patric Natindim
# March 12 2025

# Checks if the sum of two inputs is greater than, less than, or equal to 10

def sum_check():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    
    total = num1 + num2

    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")

sum_check()
