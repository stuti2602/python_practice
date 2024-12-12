"""
day_2 : problem_2 
Ask the user to input a list of numbers, seperated by spaces.
Convert the input into a list of intergers.
Calculate the sum of all numbers in the list.
Print the result in the format: "The sum of numbers is [sum]."
"""

def sum_of_list(convert_into_list):

    sum = 0

    for element in convert_into_list:
        sum += element
    return sum


def main():
    user_input = input("Enter a list of numbers seperated by spaces: ")
    convert_into_list = list(map(int,user_input.split()))
    result = sum_of_list(convert_into_list)
    print(f'The sum of numbers is {result}')

if __name__ == "__main__":
    main()

