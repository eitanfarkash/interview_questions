from itertools import combinations


# Array of numbers
a = [2, 4, 10, 3, 5]
K = 3

largest_even_sum = -1
for elements in combinations(range(len(a)), K):
    print(f"element = {elements}")
    temp_sum = sum([a[i] for i in elements])
    print(f"temp_sum = {temp_sum}")
    if temp_sum % 2 == 0 and temp_sum > largest_even_sum:
        largest_even_sum = temp_sum
    print(f"largest_even_sum = {largest_even_sum}")

print(largest_even_sum)

"""
def find_sum(arr, K):
    N = len(arr)
    if K > N:
        return -1

    max_even_sum = 0
    even_numbers = []
    odd_numbers = []

    # Create "even_numbers" and "odd_numbers" arrays, and sort them.
    for i in range(N):
        if arr[i] % 2:
            odd_numbers.append(arr[i])
        else:
            even_numbers.append(arr[i])

    odd_numbers.sort()
    even_numbers.sort()

    print(f"K = {K}")
    print(f"Odd_Numbers = {odd_numbers}\nEven_Numbers = {even_numbers}")

    i = len(even_numbers) - 1
    j = len(odd_numbers) - 1

    print(f" i = {i}, j = {j}")

    while K > 0:
        if K % 2 == 1:
            # We need to add the largest even number, if we don't have one, quit.
            if i >= 0:
                max_even_sum += even_numbers[i]
                i -= 1
            else:
                return -1
            K -= 1
        elif i >= 1 and j >= 1:
            # We need to add the largest possible pair of numbers, either even or odd.
            if (even_numbers[i] + even_numbers[i - 1] <=
                    odd_numbers[j] + odd_numbers[j - 1]):
                max_even_sum += odd_numbers[j] + odd_numbers[j - 1]
                j -= 2
            else:
                max_even_sum += even_numbers[i] + even_numbers[i - 1]
                i -= 2
            K -= 2

        elif i >= 1:
            # Handle special case where there are not enough odd numbers.
            max_even_sum += even_numbers[i] + even_numbers[i - 1]
            i -= 2
            K -= 2

        elif j >= 1:
            # Handle special case where there are not enough even numbers.
            max_even_sum += odd_numbers[j] + odd_numbers[j - 1]
            j -= 2
            K -= 2

    return max_even_sum


if __name__ == '__main__':
    arr = [2, 4, 10, 3, 5]
    K = 3
    print(find_sum(arr, K))
"""