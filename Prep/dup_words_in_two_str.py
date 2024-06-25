from collections import Counter
string1 = "apple banana mango orange"
string2 = "grape apple orange pineapple"
is_dup = False
new=[]
s1 = string1.split()
s2 = string2.split()

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            new.append(s1[i])
            is_dup=True
if is_dup:
        print("yes dup")
else:
        print("no dup")
           
print(new)