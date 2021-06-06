"""
Write a recursive function that will return the sum of all
the positive odd, even or all numbers in a dictionary which may contain more
dictionaries nested in it.

input:
{
  "a": 2,
  "b": {"x": 2, "y": {"foo": 3, "z": {"bar": 2}}},
  "c": {"p": {"h": 2, "r": 5}, "q": 'ball', "r": 5},
  "d": 1,
  "e": {"nn": {"lil": 2}, "mm": 'car'
}

"""
_dictionary_input = {
    "a": 2,
    "b": {"x": 2, "y": {"foo": 3, "z": {"bar": 2}}},
    "c": {"p": {"h": 2, "r": 5}, "q": 'ball', "r": 5},
    "d": 1,
    "e": {"nn": {"lil": 2}, "mm": 'car'}
}


def main():
    input_type = get_user_input()
    output = {}
    if input_type != "":
        output = get_searched_type_list(_dictionary_input, input_type, output)
        get_sum_list(output, input_type)


def get_sum_list(dict_input, input_type):
    sum_result = 0
    for element in dict_input[input_type]:
        sum_result += element
    print(f"""Sum of {input_type} numbers in dictionary, {dict_input} is: {sum_result}""")


def get_searched_type_list(dict_input, input_type, output):
    for key in dict_input:
        if isinstance(dict_input[key], dict):
            output = get_searched_type_list(dict_input[key], input_type, output)
        else:
            if type(dict_input[key]) == int:
                add_to_list(output, dict_input[key], input_type)
    return output


def add_to_list(output, value, input_type):
    if input_type == "even":
        value_add_even(value, output, input_type)
    elif input_type == "odd":
        value_add_odd(value, output, input_type)
    else:
        value_add_type(value, output, input_type)


def value_add_type(value, output, input_type):
    if input_type not in output:
        output[input_type] = [value]
    else:
        output[input_type].append(value)


def value_add_even(value, output, input_type):
    if value % 2 == 0:
        value_add_type(value, output, input_type)


def value_add_odd(value, output, input_type):
    if value % 2 != 0:
        value_add_type(value, output, input_type)


def get_user_input():
    user_input = input("Enter 'odd', 'even' or 'all' to search (Press anything else to skip): ")
    user_input = user_input.lower()
    if user_input == "odd" or user_input == "even" or user_input == "all":
        return user_input
    else:
        return ""


if __name__ == "__main__":
    main()
