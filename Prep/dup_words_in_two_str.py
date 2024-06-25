
from collections import Counter
string1 = "apple banana mango orange"
string2 = "grape apple orange pineapple"
is_dup =- False
new=[]
s1 = string1.split()
s2 = string2.split()
c1 = Counter(s1)
c2 = Counter(s2) 
v1=[]
v2=[]
for key1,value1 in c1.items():
    v1.append(key1)
for key2,value2 in c2.items():
    v2.append(key2)

for i in range(len(v1)):
    for j in range(len(v2)):
        if v1[i] == v2[j]:
            is_dup=True
            new.append(v1[i])
if is_dup:
        print("yes duplicates")
else:
        print("no duplicates")
print(new)