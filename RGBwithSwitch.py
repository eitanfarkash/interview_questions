# R = Red
# G = Green
# B = Blue

input_array = ['R', 'B', 'B', 'G', 'R', 'R', 'B', 'G', 'G', 'B']


# Given the function:

def switch(arr: list, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def order_by_RGB(input_list: list) -> None:
    index = 0
    index_r = 0
    index_b = len(input_list) - 1
    while index < index_b:
        if input_array[index] == "R":
            switch(input_array, index, index_r)
            index_r += 1
        if input_array[index] == "B":
            switch(input_array, index, index_b)
            index_b -= 1
            index -= 1
        index += 1


order_by_RGB(input_array)
print(f"\nThe ordered list = {input_array}\n")

# Please order the input array in the following way:
# Red at the start, Green in the middle, and Blue at the end.
# <-- (R)ed, (G)reen, (B)lue -->
