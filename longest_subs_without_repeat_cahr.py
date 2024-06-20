
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 



s = "abcabcbb"
max_len = 0
start = 0
max_subst = ""
for i in range(len(s)):
    if s[i] in s[start:i]:
        start = s[start:i].index(s[i])+start+1
    current_element = i-start+1

    if current_element>max_len:
        max_len=current_element
        max_subst = s[start:i+1]
print(max_subst)