from collections import Counter
input_string = "this is a test string with test words and some words repeating"
new=[]
words = input_string.split()
c = Counter(words)
for key,value in c.items():
    if value>1:
        new.append(key)
print(new)