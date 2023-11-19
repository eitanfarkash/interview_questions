def is_perm(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False
    return string_to_dict(string1) == string_to_dict(string2)
    # return sorted(string1) == sorted(string2)


def string_to_dict(str_to_dict: str) -> dict:
    my_dict = {}
    for letter in sorted(str_to_dict):  # no need to use sorted() - it is just for nicer printing
        # if letter not in my_dict:
        #     my_dict[letter] = 1
        # else:
        #     my_dict[letter] += 1
        my_dict[letter] = my_dict.get(letter, 0) + 1
    print(my_dict)
    # print(my_dict.keys(), my_dict.values(), my_dict.items())
    return my_dict


x = "aabbac"
y = "baaabc"
print(is_perm(x, y))
