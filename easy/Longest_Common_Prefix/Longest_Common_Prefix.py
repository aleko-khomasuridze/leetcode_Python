
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""  # Return an empty string if the input list is empty.

        pref = ""  # Initialize an empty string to store the common prefix.

        for i in range(len(strs[0])):
            current_char = strs[0][i]

            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != current_char:
                    return pref  # Return the common prefix found so far.

            pref += current_char  # If all characters match, add the character to the common prefix.

        return pref  # Return the final common prefix.


# Test cases
solution = Solution()

test1 = ["flower", "flow", "flight"]
print("Longest Common Prefix for Test Case 1:", solution.longestCommonPrefix(test1))

test2 = ["dog", "car", "race"]
print("Longest Common Prefix for Test Case 2:", solution.longestCommonPrefix(test2))

test3 = ["apple", "banana", "cherry"]
print("Longest Common Prefix for Test Case 3:", solution.longestCommonPrefix(test3))
