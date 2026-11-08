class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Brute Force 
        
        for i in range(len(nums)): # iterate through i.
            for j in range(i + 1, len(nums)): # iterate through j.
                if nums[i] + nums[j] == target: # calculate sum.
                    return [i, j] # return indices. 