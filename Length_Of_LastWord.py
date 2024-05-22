

# Input string
s = "Hello World  "

# Strip any trailing spaces
s = s.strip()
print(s)
# Split the string into words
words = s.split()
print(words)

print(len(words[0]))

# # Calculate the length of the last word
# if words:
#     length_of_last_word = len(words[-1])
#     print(length_of_last_word)
# else:
#     print(0)
