
# Given an array of strings:
arr = ['acb', 'bca', 'abcd', 'dcba', 'cab', 'ta', 'at', 'bba']
# Output should be an array of strings which are permutations of each other
# ie:
#   abc -> ['acb', 'bca', 'cab']
#   abcd -> ['abcd', 'dcba']
#   at -> ['ta', 'at']
#   abb -> ['bba']

my_dict = {} # create a dictionary, key will be the sorted string, values will be a list of the original strings which are permutation of the key
for item in arr:
    sorted_item = ''.join(sorted(item)) #since sorted() returns a list - turn it back to string
    if sorted_item in my_dict:
        my_dict[sorted_item].append(item) 
    else:
        my_dict[sorted_item] = [item]

for key,val in my_dict.items():
    print(f"{key} -> {val}")
