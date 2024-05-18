str = 'aeiou eaeaoo gokkwwtthg'
vowels = []
consonants = []
for char in str:
    if char =='a' or char =='e' or char =='i' or char =='o' or char == 'u':
        vowels.append(char)
    else:
        consonants.append(char)
print(vowels)
print(consonants)