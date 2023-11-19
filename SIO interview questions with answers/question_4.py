"""
Question 4:
    Implement function 'is_perm' which gets two strings 's1', 's2', and:
        returns True if 's1' is a permutation of 's2'
        returns False if 's1' is not a permutation of 's2'
"""


def string_to_dict(myString: str) -> dict:
    my_dict = {}
    for x in myString:
        if x in my_dict:
            my_dict[x] += 1
        else:
            my_dict[x] = 1
    return my_dict


def is_perm(string1: str, string2: str) -> bool:
    print("string1 = {}".format(string1))
    print("string2 = {}".format(string2))
    # your code goes here
    dict1 = string_to_dict(string1)
    # dict2 = string_to_dict(string2)
    # print(f" dict1 = {sorted(dict1.items())}")
    # print(f" dict2 = {sorted(dict2.items())}")
    # return dict1 == dict2
    for i in string2:
        if i in dict1 and dict1[i] != 0:
            dict1[i] -= 1
        else:
            return False
    return True


s1, s2 = ("abac", "abca")
s3, s4 = ("11abgm", "mgba11")
s5, s6 = ("abcd", "abce")
s7, s8 = ("aabbccdd", "bbccddaa")

print(is_perm(s7, s8))
