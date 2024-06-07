
# Example 1:

# Input: a = 12, b = 6
# Output: 4
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
# Example 2:

# Input: a = 25, b = 30
# Output: 2
# Explanation: The common factors of 25 and 30 are 1, 5.
 


a=25
b=30    

newa = []
newb = []

for i in range(1,a+1):
    if a % i ==0:
        newa.append(i)
        for j in range(1,b+1):
            if b%j==0:
                newb.append(j)
print(newa)
print(newb)

sim = []
for k in range(len(newa)):
    for m in range(len(newb)):
        if newa[k] == newb[m]:
            sim.append(newa[k])


se = set(sim)
print(se)
fin = list(se)
solution = len(fin)
print(solution)



