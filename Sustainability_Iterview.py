#second largest elemnt with duplicates

n = [4,4,3,2,1,0]
s = set(n)
conv = list(s)
first_max = n[0]
for i in range(len(conv)):
    if conv[i]>first_max:
        first_max = conv[i]
print(first_max)

second_max = 1
for j in range(len(conv)):
    if conv[j] > second_max and conv[j]<first_max:
        second_max=conv[j]
print(second_max)