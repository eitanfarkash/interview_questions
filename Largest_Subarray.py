numbers = [-2, -3, 4, -1, -2, -3, 5, 9]

"""Find the largest sum of any contiguous subarray."""
best_sum = 0
current_sum = 0
start_index = 0
end_index = 0
tmp = 0

for i in range(len(numbers)):
    # print(f" num = {numbers[i]}")
    current_sum = max(0, current_sum + numbers[i])
    if current_sum == 0:
        tmp = i + 1
    if best_sum < current_sum:
        start_index = tmp
        end_index = i
    best_sum = max(best_sum, current_sum)

print(f"Max Sub array is: {best_sum}")
print(f"Start Index = {start_index}, End index = {end_index}")
print(f"Subarray is: {numbers[start_index:end_index + 1]}")
