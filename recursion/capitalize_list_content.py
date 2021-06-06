"""
Write a recursive function that takes an array of words and returns an array that contains all the words capitalized.
If this is the input array:
['foo', 'bar', 'world', 'hello']
The output array should be:
['FOO', 'BAR', 'WORLD', 'HELLO']
"""


def main():
    input_list = ['foo', 'bar', 'world', 'hello']
    result_list = get_capitalized_list(input_list)
    print(f"""The capitalized version of {input_list} is: {result_list}""")


def get_capitalized_list(input_list):
    if len(input_list) == 0:
        return []
    else:
        return [input_list[0].upper()] + get_capitalized_list(input_list[1:])


if __name__ == "__main__":
    main()
