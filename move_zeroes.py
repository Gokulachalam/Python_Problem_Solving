# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

arr = [0, 1, 0, 3, 12]
non_zero_pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i],arr[non_zero_pos] = arr[non_zero_pos],arr[i]
        non_zero_pos+=1
print(arr)





