n = [1,1,2,2,3,4]
unique = []
for i in n:
    count = n.count(i)
    if count ==1:
        unique.append(i)
print(unique)


