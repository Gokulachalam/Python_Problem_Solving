from collections import Counter
str = "gokulachalam"
c = Counter(str)
n = []
m = []
print(c)

for key,value in c.items():
    n.append(key)
    m.append(value)


ma = max(m)
m.remove(ma)
fina = max(m)
print(fina)



for key , value in c.items():
    if fina == value:
        print(key)