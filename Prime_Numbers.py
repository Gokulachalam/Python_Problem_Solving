#to check a number is prine or not 
# n = 7
# is_prime = True

# for i in range(2,n):
#     if n%i ==0:
#         is_prime = False
#         break

# if is_prime:
#     print("prime")
# else:
#     print("not a prime")


#to print prime numbers within given range
# n = 10
# for number in range(2,n):
#     is_prime = True
#     for i in range(2,number):
#         if number%i == 0:
#             is_prime= False
#             break
#     if is_prime:
#         print(number)




a = 12
b = 6
newa = []
newb = []
for i in range(1,a+1):
    for b in range(1,b+1):
        if a[i]%i==0:
            print(i)