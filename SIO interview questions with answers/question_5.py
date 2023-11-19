"""
Question 5:
    Implement function 'evaluate' which gets a strings representing mathematical calculation for example:
    "5 + 3 + 12"
    or
    "- 1 + 9 - 3 + 5"
        The function should return the result of the calculation
        Assume the string is legal, and space always exist between sign and number.
"""


def evaluate(my_string: str) -> int:
    # print("my_string = {}".format(my_string))
    my_list = my_string.split(" ")
    sign = 1
    my_sum = 0
    for i in my_list:

        if i == '-':
            sign = -1
        elif i == '+':
            sign = 1
        else:
            my_sum += int(i) * sign
    return my_sum

    # your code goes here


s1 = "- 1 + 2 + 3 - 5"
s2 = "- 10 + 5 + 3 + 2"
s3 = "- 127 + 27 + 150 + 2"
s4 = "1 + 2 + 3 - 5"
print(f"{s4} = {evaluate(s4)}")

# def evaluate(my_string: str) -> int:
#     print("my_string = {}".format(my_string))
#     # your code goes here
#     my_list = my_string.split()
#     sign = 1
#     my_sum = 0
#     for c in my_list:
#         if c == "-":
#             sign = -1
#         elif c == "+":
#             sign = 1
#         else:
#             my_sum += int(c) * sign
#     return my_sum
