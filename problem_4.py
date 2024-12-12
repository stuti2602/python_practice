"""
day_4: problem_4

calculate the sum of odd number

Asks the user to input a positive inteher, n
calculate the sum of all odd numbers from 1to n(inclusive).
prints the result

input: Enter a positive integer: 10

output: The sum of odd numbers from 1 to 10 is 25
"""

def sum_of_odd(n):

    total = 0

    for number in range (1,n+1):
        if number % 2 != 0:
            total += number
    return total


def main():

    number_input = int(input("Enter a positive integer:  "))
    output = sum_of_odd(number_input)
    print(f"The sum of odd numbersfrom 1 to {number_input} is {output}")

if __name__== "__main__":
    main()
