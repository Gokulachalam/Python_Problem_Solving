nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = float('-inf')
current_sum = 0
start = 0
end = 0
subarray_start = 0

for i in range(len(nums)):
    num = nums[i]
    if num > current_sum + num:
        current_sum = num
        subarray_start = i
    else:
        current_sum += num

    if current_sum > max_sum:
        max_sum = current_sum
        start = subarray_start
        end = i

max_subarray = nums[start:end+1]
print(f"Maximum sum of contiguous subarray: {max_sum}")
print(f"Elements of the subarray: {max_subarray}")
