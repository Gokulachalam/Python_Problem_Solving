# l_range = int(input("Enter Lower Range: "))
# u_range = int(input("Enter Upper Range: "))
# print("Prime numbers between", l_range, "and", u_range, "are:")
# for num in range(l_range, u_range + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)



num = int(input("Enter a number: "))
if num > 1:
    # Check for factors from 2 to num-1
    for i in range(num):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")



