from collections import Counter

# n = [0,1,2,2,4,4,1]
n = [10,10,10,2,2,1]

new = []
val=[]

for i in range(len(n)):
    if n[i]%2 ==0 and i!= 0:
        new.append(n[i])
print(new)


c = Counter(new)
for key , value in c.items():
    
    val.append(key)
    ma = max(val)
    
print(val)    
print(max(val))
