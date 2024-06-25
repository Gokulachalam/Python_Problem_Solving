from collections import Counter
input_string = "this is a good boy is a"
new=[]
is_dup=False
words = input_string.split()
c = Counter(words)
for key,value in c.items():
    if value>1:
        new.append(key)
        is_dup=True
if is_dup:
    print("yes dup")
else:
    print("no dup")

print(new)