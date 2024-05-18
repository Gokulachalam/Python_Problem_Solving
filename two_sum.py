# arr = [3,2,3]
# target = 6
# index = []
# for i in range(len(arr)-1):
#     if arr[i] + arr[i+1] == target:
#         index.append(i)
#         index.append(i+1)
#         print(index)
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Loop through the list with a step of 2
for i in range(0, len(my_list), 1):
    current_element = my_list[i]
    # Check if i+2 is within the bounds of the list
    if i + 2 < len(my_list):
        next_element = my_list[i + 1]
    else:
        next_element = None  # or some other way to handle the edge case
    
    print(f"Current: {current_element}, Next: {next_element}")
