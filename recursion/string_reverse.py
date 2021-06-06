"""
Write a recursive function that takes a string and reverse the string.
If the input is ‘amazing’, it should return ‘gnizama’.
"""


def main():
    input_word = (input("Enter a word to generate the reverse (press Enter to skip): "))
    if input_word != "":
        result = get_reverse(input_word)
        print(f"""The reverse of {input_word} is: {result}""")


def get_reverse(word):
    if len(word) == 1:
        return word
    return word[len(word) - 1] + get_reverse(word[: len(word) - 1])


if __name__ == "__main__":
    main()
