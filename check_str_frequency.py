from collections import Counter
s = "abaab"
is_c = False
c = Counter(s)

ne=[]
new=[]
for key,value in c.items():
    new.append(value)
same = new[0]

for i in range(len(new)):
    if new[i] == same:
        ne.append(new[i])
        if len(new) == len(ne):
            is_c = True
if is_c:
    print("yes")
else:
    print("no")

