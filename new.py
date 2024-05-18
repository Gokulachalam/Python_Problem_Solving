
# Output: [24,12,8,6]


# array = [1, 2, 3, 4, 5]
# product  =1

# for i in range(len(array)):
#     cur = array[i]
#     for j in range(len(array)):
#         if i!=j:
#             if cur == array[j]:
#                 for k in array:
#                     product = product*k
#                     print(product)



# array = [1, 2, 3, 4, 5]
# product = 1

# for i in range(len(array)):
#     cur = array[i]
#     for j in range(len(array)):
#         if i != j:
#             if cur == array[j]:
#                 for k in array:
#                     product *= k
#                     print(product)


array = [1, 2, 3, 4, 5]
product = 1

for i in range(len(array)):
    cur = array[i]
    for j in range(len(array)):
        if i != j and cur == array[j]:  # Check for duplicates
            for k in array:
                product *= k
                print(product)
