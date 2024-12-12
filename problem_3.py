"""
day_3 : problem_3 

write a pyhton program that asks user to input a number and prints the multiplication table for that number from 1 to 10.
"""

def multiplication_table(input_number):
    for i in range(1,11):
        multi = input_number * i
        print(f"{input_number} * {i} = {multi}")

def main():
    input_number = int(input("Enter a number: "))
    multiplication_table(input_number)

if __name__ == "__main__":
    main()
