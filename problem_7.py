"""
Day_7 : problem_7

write a python program that calculates the factorial of a given positive integer.

Ask the user to input a positive integer.
calculate the factorial of given number
factorial of a number n is the product of all positive integers less than or equal to n.
5 ! = 120
if the user enters a non -positive number, display an appropriatemessage.
input : Enter a positive integer: 5
output : The factorial of 5 is 120
"""

def calculate_factorial(integer_input):
    if integer_input > 0:
        factorial = 1
        for number in range(integer_input,0,-1):
            factorial *= number
        return(f"the factorial of is {factorial}")        
    else:
        return None

def main():
    integer_input = int(input("Enter a positive integer:  "))

    if integer_input <= 0:
        print("please enter a positive numbers.")
    else:
        output = calculate_factorial(integer_input)
        print(f"The  factorial of {integer_input} is {output}")

if __name__ == "__main__":
    main()