numbers = [-1,0] 
target = -1
new = []
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target:
            new.append(i+1)
            new.append(j+1)
print(new)