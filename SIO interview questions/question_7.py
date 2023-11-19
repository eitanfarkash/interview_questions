"""
Question 7 (sort with 2 digits):
    Given a list "my_list" which contains only integers 0, 1 for example: my_list=[1, 0, 0, 0, 1]
    And a method swap(my_list,i,j) which swaps the content of cells in index i and j in "my_list"

    You need to order "my_list", 0, then 1,
    for example: my_list=[0, 0, 0, 1, 1]
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
    low = 0
    high = len(my_list) - 1
    while low < high:
        while my_list[low] == 0: 
            low += 1

        while my_list[high] == 1: 
            high -= 1

        if low < high:
            swap(my_list, low, high)
            low += 1
            high -= 1

    print("After sort: my_list = {}".format(my_list))


my_list1 = [0, 1]
my_list2 = [1, 0]
my_list3 = [1, 0, 0, 0, 1]
my_list4 = [0, 0, 0, 0]
my_list5 = [1, 1, 1, 1, 1]
my_list6 = [0, 1, 0, 1, 0]
my_sort(my_list=my_list6)


