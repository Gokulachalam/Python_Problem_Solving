arr = [1,3,7,5,99]
target = 100
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] ==  target:
            print(i,j)