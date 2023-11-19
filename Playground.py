# set1 = {"a", "b" , "c", 3}
# set2 = {"a", 2, 3, "c"}
#
# set3  = set1 & set2
# print (list(set3))a
#
#
# a = [1, 2, 3]
# print(sum(a))
#
# dct = {'a': 1, 'b': 2}
# # dct.clear()
# print(f"DCT is: {dct}")
# print(f"the dictionary is empty? {not (bool(dct))}")
#
# for d in dct.values():
#     print(f"d={d}")
#
# A = [1, 2, 5]
# print(A[-2:])
#
# even_numbers = []
# odd_numbers = []
# max_nums_array = []
# number_list = [1, 7, 8, 10, 11, 12]
# odd = [item for item in number_list if not item % 2]
# print(f"Odd list is: {odd}")

my_array = [4, 9, 5, -3, 15, -7, 9, -1, 1, 15, 1, 12, 50, -42]
my_num = 8
my_dict = {}
for x in my_array:
    my_dict[x] = my_dict.get(x, 0) + 1
for y in my_dict.keys():
    z = my_num - y
    if z in my_dict.keys() and my_dict[z] != "already visited":
        print(f"The 2 numbers that sums to {my_num} are {y} and {z}")
        my_dict[y] = "already visited"

z = "dsdab"
print(f"sorted z = {sorted(z)}")
