
from collections import Counter
s = "anagrams"
t = "nagarams"
conv1 = list(s)
conv2 = list(t)

c = Counter(conv1)
c1 = Counter(conv2)

new=[]
new1=[]


for key , value in c.items():
    for keys , values in c1.items():
        new.append(key)
        new1.append(keys)
new.sort()
new1.sort() 
print(new)
print(new1)

if new==new1:
    print("yes")
else:
    print("no")