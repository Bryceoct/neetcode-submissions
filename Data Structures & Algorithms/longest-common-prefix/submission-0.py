class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Iterates through each character of the first string
        for i in range(len(strs[0])):
            # Compares that character against every other string
            for j in range(1, len(strs)):
                # Checks for an invalid index or mismatched characters
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    # Returns all matching characters before index i
                    return strs[0][:i]
        # If no mismatch occurs, return the entire first string
        return strs[0]