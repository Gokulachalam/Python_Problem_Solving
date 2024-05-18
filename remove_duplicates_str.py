str = "ggookkul"
duplicates = []
non_duplicates = []
for char in str:
    if str.count(char) > 1:
        duplicates.append(char)
    else:
        non_duplicates.append(char)
print(duplicates)
print(non_duplicates)
