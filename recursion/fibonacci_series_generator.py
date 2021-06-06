"""
The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
"""


def main():
    user_input = get_user_input()
    if user_input != -1:
        series = get_fibonacci_series(user_input)
        print(series)


def get_fibonacci_series(n):
    series = []
    # adding fibonacci result to an empty list
    for i in range(0, n + 1):
        series.append(generate_fibonacci(i))
    return series


def generate_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return generate_fibonacci(n - 1) + generate_fibonacci(n - 2)


def get_user_input():
    user_input = input("Enter a number to generate fibonacci series (Press enter to skip): ")
    if user_input == "" or user_input.isalpha():
        return -1
    else:
        return int(user_input)


if __name__ == "__main__":
    main()
