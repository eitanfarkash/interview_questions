"""
Question 1:
    1.1 create a list 'l1' which contains the first 10 powers of 2
    1.2 create a list 'l2' which contains the strings: "a1", "a2", "a3",... "a100"
    1.3 create a list 'l3' which contains only the first 10 items from 'l2'
    1.4 create a list 'l4' which contains only the last 15 items from 'l2'
    1.5 create a list 'l5' which is a copy of 'l2'
Question 2:
    create a list which contains all letters from 'a' to 'z'
Question 3:
    Implement function 'is_unique' which gets a string and:
        returns True if all the characters appears only once
        returns False if there are characters which appear more than once
Question 4:
    Implement function 'is_perm' which gets two strings 's1', 's2', and:
        returns True if 's1' is a permutation of 's2'
        returns False if 's1' is not a permutation of 's2'
Question 5:
    Implement function 'sort_by_color' which gets a list of strings, the strings can be:
    "blue", "green", "red"
        The function should return the list sorted by color:
        "blue" then "green" then "red"
Question 6:
    Implement function 'evaluate' which gets a strings representing mathematical calculation for example:
    "5 + 3 + 12"
    or
    "- 1 + 9 - 3 + 5"
        The function should return the result of the calculation
"""
"""
Question 1:
    1.1 create a list 'l1' which contains the first 10 powers of 2
    1.2 create a list 'l2' which contains the strings: "a1", "a2", "a3",... "a100"
    1.3 create a list 'l3' which contains only the first 10 items from 'l2'
    1.4 create a list 'l4' which contains only the last 15 items from 'l2'
    1.5 create a list 'l5' which is a copy of 'l2'
"""
"""
l1 = [2**i for i in range (0,11)]
print("string is: {}".format(l1))

l2 = ["a{}".format(i) for i in range (0,101)]
print (l2)


s1 = " -1 + 2 + 3 - 5"
print(s1)
s2 = s1.split('+')
print(s2)
sum = 0
for i in s2:
    #print(i)
    #print(ord(i.strip()))
    sum = sum + int(i)
print(sum)

Question 5:
    Implement function 'sort_by_color' which gets a list of strings, the strings can be:
    "blue", "green", "red"
        The function should return the list sorted by color:
        "blue" then "green" then "red"
"""
"""
Question 6:
    Implement function 'sort_by_color' which gets a list of strings, the strings can be:
    "red", "green"
        The function should return the list sorted by color:
        "red" and then "green"
"""

from typing import List


def sort_by_color(list_colors: List[str]) -> List[str]:
    print("list_colors = {}".format(list_colors))
    d = {}

    for color in list_colors:
        if color in d:
            d[color] += 1
        else:
            d[color] = 1

    list_colors_sorted = ["red"] * d["red"] + ["green"] * d["green"] + ["blue"] * d["blue"]
    return list_colors_sorted


    # "list_colors" should be sorted as follows:
    # First "red" and then "green"
    # your code goes here


list_colors1 = ["blue", "green", "red", "green", "red", "blue", "green"]
list_colors2 = ["green", "green", "green", "red"]
list_colors3 = ["red", "red", "green", "green"]
list_colors4 = ["green", "green", "green", "green"]
list_colors5 = ["red", "red", "red", "red"]
print(sort_by_color(list_colors1))

# # Dictionary Methods
# # marks = {}.fromkeys(['Math', 'English', 'Science'], 3)
#
# # Output: {'English': 0, 'Math': 0, 'Science': 0}
# print(marks)
#
# # Output: ['English', 'Math', 'Science']
# print(list(sorted(marks.keys())))
#
# # for color, count in marks.items():
# #     print(f"Color = {color}, Count = {count}")
# #
# # for d in marks.items():
# #     print(f"d = {d}")
