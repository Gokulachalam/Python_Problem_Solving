nums = [1,2,3,1,2,3]
new = []
k = 2
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            new.append(i)
            new.append(j)

print(new)



for m in range(len(new)):
    for l in range(len(new)):
        if new[l] - new[k] <=m:
            print("yes")

        else:
            print("no")

# for k in range(len(new)):
#     for l in range(k+1,new):
#         sub = sub - 
