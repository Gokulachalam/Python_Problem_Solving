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
n = 10
for number in range(2,n):
    is_prime = True
    for i in range(2,number):
        if number%i == 0:
            is_prime= False
            break
    if is_prime:
        print(number)