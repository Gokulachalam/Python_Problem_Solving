# Example 1:

# Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
# Output: 2.00000
# Explanation: After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.
# Example 2:

# Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
# Output: 4.00000
# Example 3:

# Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
# Output: 4.77778



class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        
        n = len(arr)
        remove_count = n // 20
        
        trimmed_arr = arr[remove_count : n - remove_count]
        
        mean = sum(trimmed_arr) / len(trimmed_arr)
        
        return mean