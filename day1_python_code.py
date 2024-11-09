"""
prompt the user input an integer.
check if the number is even or odd.
print meassage saying:
"the number [number] is even."
"the number [number] is odd."

example :
input : 4
output : "the number 4 is even.

input : 7
output: the number 7 is odd.
"""

def is_even_or_odd(user_input):

    if user_input % 2 == 0:
        return (f"the number {user_input} is even.")
    else:
        return (f"the number {user_input} is odd.")


def main():
    user_input = int(input("give a number: "))
    output = is_even_or_odd(user_input)
    print(output)

if __name__ == "__main__":
    main()
