"""
day_5 : problem_5

write the python problem to count the number of the vowels in a give string.

prompt the user to input string
determine how many vowels ('a','e','i','o','u') are present in the string, counsidering both uppercase and lowercase characters
display the total number of vowels found.

input: Enter a string: OpenAI is awesome
output:the number of vowels in the string is : 9

"""

def count_of_vowels(string_input):

    vowels_list = ["a","e","i","o","u","A","E","I","O","U"]
    count = 0

    for word in string_input:
        if word in vowels_list:
            count +=1
    return count


def main():
    string_input = input("Enter a string: ")
    output = count_of_vowels(string_input)
    print(f"The number of vowels in the string is : {output}")

if __name__ == "__main__":
    main()