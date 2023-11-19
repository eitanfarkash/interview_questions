def evaluate(my_string: str) -> int:
    # print("my string = {}".format(my_string.split()))
    sum1 = 0
    sign = 1
    for x in my_string.split():
        if x == '-':
            sign = -1
        elif x == '+':
            sign = 1
        else:
            sum1 += sign * int(x)
    return sum1


# return eval(my_string)

s1 = "- 1 + 2 + 3 - 5 + 20 + 1"
print(f"Result = {evaluate(s1)}")
print(f"Results of EVAL function = {eval(s1)}")
s2 = [-1, 2, 3, -5, 20]
# w = sum(s2)
# print(f"sum = {w}")
# l1 = [2 ** x for x in range(11)]
# print(f"l1 = {l1}")
# l2 = [f"a{i}" for i in range(101)]
# # for i in range(1, 101):
# #     l2.append(f"a{i}")
# print(f"l2 = {l2}")
# l3 = l2[:10]
# print("l3 = {}".format(l3))
# l4 = l2[-15:]
# print(f"l4 = {l4}")
# l5 = l2[:]
# l2.insert(0, "Eitan")
# print(f"l2 = {l2}")
# print(f"l5 = {l5}")
