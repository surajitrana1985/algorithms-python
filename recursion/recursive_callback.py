"""
Write a recursive function that takes an array and a callback function and returns True
if any value of that array returns True from that callback function otherwise returns False.
"""


# Callback Function
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False


# input
input_list = [1, 2, 3, 5]


def main():
    result = recursive_callback(input_list, isEven)
    print(result)


def recursive_callback(input_list, cb):
    if len(input_list) == 0:
        return False
    if cb(input_list[0]):
        return True
    else:
        return recursive_callback(input_list[1:], cb)


if __name__ == "__main__":
    main()
