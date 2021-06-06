"""
Write a recursive function that takes a number as an input and returns the factorial of that number.
"""


def main():
    input_number = int(input("Enter a number > 0 to get its factorial: "))
    if input_number > 0:
        result = get_factorial(input_number)
    else:
        result = None
    if result != None:
        print(f"""{input_number}! = {result}""")


def get_factorial(n):
    if n == 1:
        return 1
    return n * get_factorial(n - 1)


if __name__ == "__main__":
    main()
