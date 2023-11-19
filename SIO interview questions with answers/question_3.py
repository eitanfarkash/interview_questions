"""
Question 3:
    Implement function 'is_unique' which gets a string and:
        returns True if all the characters appears only once
        returns False if there are characters which appear more than once
"""


def is_unique(my_string: str) -> bool:
    print(f"my_string = {my_string}")
    letters = {}
    for x in my_string:
        if x in letters:
            # letters[x] += 1
            return False
        else:
            letters[x] = 1
    return True
    # your code goes here


s1 = "abac"
s2 = "abcdefg"
s3 = "bdghjkgl"
s4 = "aaa"

print(is_unique(my_string=s1))
