"""
Question 7:
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
    first_one = 0
    first_two = 0
    for i in range(0, len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            # print(f"List = {my_list}")
            if my_list[i] == 2:
                print(f"swapping {i} with {i + 1}, i = {i} ")
                swap(my_list, i, i + 1)
                first_two = i
                if my_list[i] == 1:
                    first_one = i
            else:  # my_list[i] = 1 and my_list[i+1] = 0
                swap(my_list, i, i + 1)
                first_one = i
        elif my_list[i] == 2:
            first_two = i
        elif my_list[i] == 1:
            first_one = i
        elif my_list[i] == 0 and my_list[i+1] == 1:
            pass




"""
def my_sort(my_list: List[int]):
    print("Before sort: my_list = {}".format(my_list))
    first_one = 0
    for i in range(0, len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            print(f"List = {my_list}")
            print(f"swapping {first_one} with {i + 1}, i = {i} ")
            swap(my_list, first_one, i + 1)
            first_one += 1
        elif my_list[i + 1] == 1 and my_list[i] == 0:
            first_one += i + 1


def my_sort(my_list: List[int]):
    print("Before sort: my_list = {}".format(my_list))
    first_one = 0
    for i in range(len(my_list) - 1):
        if my_list[i] == 0:
            first_one += 1
        elif my_list[i + 1] == 0:
            swap(my_list, first_one, i + 1)
            first_one += 1
"""

my_list1 = [0, 1]
my_list2 = [1, 0]
my_list3 = [1, 0, 0, 0, 1]
my_list4 = [0, 0, 0, 0]
my_list5 = [1, 1, 1, 1, 1, 0, 0]
my_list6 = [0, 1, 0, 1, 0]
my_list7 = [1, 1, 1, 0, 0]
my_list8 = [0, 0, 1, 1, 0]
my_list10 = [2, 1, 0, 2, 0, 1]

my_list = my_list10
my_sort(my_list)
print("After sort: my_list = {}".format(my_list))
