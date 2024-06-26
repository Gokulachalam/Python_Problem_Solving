s = "aaaabbbc"
n = list(s)
# n = [1,1,2,2,3,4]
new=[]
e=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i] == n[j]:
            new.append(n[i])
for k in n:
    if k not in new:
        e.append(k)
print(e)