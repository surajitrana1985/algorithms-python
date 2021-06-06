"""
Write a recursive function that takes a list of numbers as an input
and returns the product of all the numbers in the list.
"""


def main():
    generated_list = []
    input_num = input("Enter numbers to add in list (press Enter to skip): ")
    while input_num != "":
        generated_list.append(int(input_num))
        input_num = input("Enter numbers to add in list (press Enter to skip): ")
    result = product_of_numbers(generated_list)
    print(f"""Product of all numbers in the list {generated_list} is: {result}""")


def product_of_numbers(list_input):
    if len(list_input) == 0:
        return 0
    if len(list_input) == 1:
        return list_input[0]
    else:
        return list_input[len(list_input) - 1] * product_of_numbers(list_input[0: len(list_input) - 1])


if __name__ == "__main__":
    main()
