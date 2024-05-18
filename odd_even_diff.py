
n = int(input("Enter the size of the array: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

even = []
odd = []
even_tot = 0
odd_tot = 0

for i in range(len(arr)):
    if arr[i]%2 ==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
even_tot = sum(even)
odd_tot = sum(odd)
# print(even_tot)
print(odd_tot-even_tot)


