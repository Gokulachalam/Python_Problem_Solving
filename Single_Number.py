

numbers = [2,1,2]

uni = []
seen = set()

for i in numbers:
    if i not in seen:
        seen.add(i)
        uni.append(i)
    else:
        uni.remove(i)

ans = int(uni[0])
print(ans)

