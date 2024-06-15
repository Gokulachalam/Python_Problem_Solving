num = 1800
st = str(num)
l = list(st)
cop = l.copy()
for i in range(len(l)):
    if l[i] == '0':
        cop.remove(l[i])


first_rev = cop[::-1]
second_rev = first_rev[::-1]



if l == second_rev:
    print("true")

else:
    print("False")