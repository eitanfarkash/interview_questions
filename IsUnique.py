"""
Question 3:
    Implement function 'is_unique' which gets a string and:
        returns True if all the characters appears only once
        returns False if there are characters which appear more than once
"""

def is_unique(my_string: str) -> bool:
    print(my_string)
    my_dict = {}
    for letter in my_string:
        if letter in my_dict:
            return False
        else:
            my_dict[letter] = 1
    return True


s1 = "abac"
s2 = "abcdefg"
s3 = "bdghjkgl"
s4 = "aaa"
s5 = "eitan"

print(is_unique(my_string=s5))
