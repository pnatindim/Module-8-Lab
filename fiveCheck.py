# Patric Natindim
# March 12 2025

# Prints if the value 5 is in a list

def five_check():
    user_input = input("List of numbers: ")
    
    num_list = [int(item) for item in user_input.split()]
    
    if 5 in num_list:
        print("5 is in this list.")
    else:
        print("5 is not in this list.")

five_check()
