# arr = [1,2,3,4,5]
# max = arr[0]
# min = arr[1]
# for i in range(len(arr)):
#     if arr[i] > max:
#         max = arr[i]
#     if arr[i] < min:
#         min = arr[i]
# print(max,min)


arr = [1,2,3,4,5]
max = arr[0]
min = arr[1]

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]
print(max)
print(min)