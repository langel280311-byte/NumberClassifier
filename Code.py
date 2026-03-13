# Function to check if the number is even or odd
def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to check if the number is positive or negative
def number_type(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Function to show the result
def show_result(number):
    even_odd = is_even(number)
    num_type = number_type(number)
    
    print("Number:", number)
    print("Even/Odd:", even_odd)
    print("Type:", num_type)

# Input number
num = int(input("Enter a number: "))

# Show result
show_result(num)
