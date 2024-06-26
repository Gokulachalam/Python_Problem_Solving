from collections import Counter
s1 = "silent"
s2 = "listen"


c = Counter(s1)
c1 = Counter(s2)

is_anagram = False
if c==c1:
    is_anagram = True
if is_anagram:
    print("anagram")
else:
    print("not a anagram")
