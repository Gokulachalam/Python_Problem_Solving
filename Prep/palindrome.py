string = "saas"
rev = ""
is_pal = False
for i in range(len(string)):
    rev = string[i]+rev
    if rev == string:
        is_pal = True
if is_pal:
    print("palindrome")
else:
    print("not a palindrome")