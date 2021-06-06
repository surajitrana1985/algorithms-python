"""
Write a function that takes a string and returns if the string is a palindrome.
As a reminder, if a string is equal to its reverse, it is called a palindrome.
Such as Madam, civic, kayak. If you reverse any of these words they stay the same.
"""


def main():
    input_word = input("Enter a word for palindrome check: ")
    is_palindrome = check_palindrome(input_word)
    if is_palindrome:
        print(f"""{input_word} is Palindrome.""")
    else:
        print(f"""{input_word} is not Palindrome!""")


def check_palindrome(word):
    if len(word) == 0:
        return True
    if word[0] != word[len(word) - 1]:
        return False
    return check_palindrome(word[1:-1])


if __name__ == "__main__":
    main()
