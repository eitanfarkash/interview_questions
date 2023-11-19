"""
Question 4:
    Implement function 'is_perm' which gets two strings 's1', 's2', and:
        returns True if 's1' is a permutation of 's2'
        returns False if 's1' is not a permutation of 's2'
"""

def dict_compare(dict1: dict, dict2: dict) -> bool:
    if len(dict1) != len(dict2):
        return False
    for x in dict1:
        if x in dict2 and dict1[x] == dict2[x]:
            pass
        else:
            return False
    return True

def string_to_dict(myString: str) -> dict:
    my_dict = {}
    for x in myString:
        if x in my_dict:
            my_dict[x] += 1
        else:
            my_dict[x] = 1
    return my_dict

def is_perm(string1: str, string2: str) -> bool:
    print(f"string1 = {string1}")
    print(f"string2 = {string2}")
    # Your code goes here
    d1 = string_to_dict(string1)
    d2 = string_to_dict(string2)

    return (dict_compare(d1, d2))


s1, s2 = ("abac", "abca")
s3, s4 = ("11abgm", "mgba11")
s5, s6 = ("abcd", "abce")
s7, s8 = ("aabbccdd", "bbccddaa")

print(is_perm(s7, s8))
