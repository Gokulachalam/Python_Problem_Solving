# Input : 97
# Output : Twisted Prime Number
# Explanation: 97 is a prime number
# and its reverse 79 is also a prime
# number.

# Input : 43
# Output : Not a Twisted Prime Number
# Explanation: 43 is a prime number
# but its reverse 34 is not a prime
# 





n = 11
s = str(n)
l = list(s)
rev = ''.join(l[::-1])
conv = int(rev)

is_org_prime = True
is_rev_prime = True

#
for i in range(2, n):
    if n % i == 0:
        is_org_prime = False
        break


for j in range(2, conv):
    if conv % j == 0:
        is_rev_prime = False
        break


if is_org_prime and is_rev_prime:
    print("yes it is a twisted prime number")
else:
    print("no it is not a twisted prime number")

        