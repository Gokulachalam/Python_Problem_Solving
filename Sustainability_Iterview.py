n = [4,4,3,2,1,0]
new = []
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i] == n[j]:
            new.append(n[i])
maxi = n[2]
res = [i for i in n if i not in new]




for k in range(len(res)):

    if res[k]>maxi:
        maxi = res[k]

print(maxi)