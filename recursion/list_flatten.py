"""
Write a recursive function that takes an array that may contain
more arrays in it and returns an array with all values flattened.

Suppose this is the input array:
[[1], [2, 3], [4], [3, [2, 4]]]

The output should be:
[1, 2, 3, 4, 3, 2, 4]
"""

unflattened_list = [[1], [2, 3], [4], [3, [2, 4]], 5]


def main():
    flattened_list = []
    flattened_list = get_unflattened_list(unflattened_list, flattened_list)
    print(f"""Flattened form of list {unflattened_list} is: {flattened_list}""")


def get_unflattened_list(input_list, output_list):
    for element in input_list:
        if isinstance(element, list):
            output_list = get_unflattened_list(element, output_list)
        else:
            output_list.append(element)
    return output_list


if __name__ == "__main__":
    main()
