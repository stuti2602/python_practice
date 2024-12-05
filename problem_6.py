"""
Day_6 : Problem_6

write a pyhton program that take a string as input and check if it is palindrome.

input : Enter a string : Madam
output : The string is a Palindrome.


def is_palindrome(input_string):
    right_pointer = (len(input_string)-1)
    left_pointer = 0
    palindrome = True

    while left_pointer < right_pointer:
        if input_string[right_pointer] == input_string[left_pointer]:
            right_pointer = -1
            left_pointer = 1
        else:
            palindrome = False
    return (f"The string is {palindrome} palindrome")

def main():
    input_string = input("Enter a string: ")
    output = is_palindrome(input_string)
    print(output)

if __name__ == "__main__":
    main()

"""

def is_palindrome(input_string):

    if input_string == input_string[::-1]:
        return True
    else:
        return False
    
def main():

    input_string = input("Enter a string input: ")
    output = is_palindrome(input_string)
    print(f"This string is palindrome: {output}")

if __name__ == "__main__":
    main()



