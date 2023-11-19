"""
Given an array, permutation of R G and B (example arr=[G,G,R,R,B,R,R,G,B,R])
And a method switch(arr,i,j) which switches between index i and j in array arr)

*** You need to order this array so all R's will be first, G's will be second and B's will be last (example [R,R,G,G,
G,B,B,B,B]), using the given switch method.

"""
input_array = ['R', 'B', 'B', 'G', 'R', 'R', 'B', 'G', 'G', 'B']


# Given the function:

def switch(arr: list, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def order_by_RGB(input_list: list) -> None:
    index = 0
    index_r = 0
    index_b = len(input_list)-1
    while index < index_b:
        if input_list[index] == 'R':
            switch(input_list, index, index_r)
            index_r += 1
        if input_list[index] == 'B':
            switch(input_list, index, index_b)
            index_b -= 1
            index -=1
        index += 1




order_by_RGB(input_array)
print(f"\nThe ordered list = {input_array}\n")
