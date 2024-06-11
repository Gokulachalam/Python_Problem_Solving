arr = [1,2,3,4,5]
d = 2

arr = [1,2,3,4,5,6,7]
d = 1
for i in range(d):
    po = arr.pop(0)
    arr.append(po)
print("left",arr)