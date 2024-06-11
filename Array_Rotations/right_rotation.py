arr = [1,2,3,4,5]
d = 2
for i in range(d):
    po = arr.pop()    # Remove the last element from the array
    arr.insert(0, po) # Insert the removed element at the beginning of the array
print("right" ,arr)