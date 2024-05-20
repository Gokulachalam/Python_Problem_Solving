n = int(input("Enter the number of terms: "))

first = 0
second = 1

for i in range(n):
    print(first,end=' ')
    first,second = second,first+second
