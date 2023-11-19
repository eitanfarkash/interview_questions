"""
Question 8 (sort with 3 digits):
    Given a list "my_list" which contains only integers 0, 1, 2 for example: my_list=[1, 0, 2, 0, 0, 1, 2]
    And a method swap(my_list,i,j) which swaps the content of cells in index i and j in "my_list"

    You need to order "my_list", 0, then 1, then 2,
    for example: my_list=[0, 0, 0, 1, 1, 2, 2]
    using the given swap method.
"""
from typing import List


def swap(my_list, i, j):
    tmp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = tmp


def my_sort(my_list: List[int]):
    print("Before sort: my_list = {}".format(my_list))
    # your code goes here

    print("After sort: my_list = {}".format(my_list))


my_list1 = [0, 1, 2]
my_list2 = [2, 1, 0]
my_list3 = [1, 0, 2, 0, 0, 1, 2]
my_list4 = [0, 0, 0, 0]
my_list5 = [1, 1, 1, 1, 1]
my_list6 = [2, 1, 2, 2, 1, 2]
my_list7 = [0, 0, 2, 1, 0, 2]
my_sort(my_list=my_list1)


# def my_sort(my_list: List[int]):
#     print("Before sort: my_list = {}".format(my_list))
#     # your code goes here
#     low = 0
#     mid = 0
#     high = len(my_list) - 1
#     while mid <= high:
#         if my_list[mid] == 0:
#             swap(my_list, low, mid)
#             low += 1
#             mid += 1
#         elif my_list[mid] == 1:
#             mid += 1
#         elif my_list[mid] == 2:
#             swap(my_list, mid, high)
#             high -= 1
#
#     print("After sort: my_list = {}".format(my_list))
