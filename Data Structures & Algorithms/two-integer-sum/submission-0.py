class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # basic 
        for i in range(len(nums)): # nums length
            for j in range(i + 1, len(nums)): # (2,4)
                if nums[i] + nums[j] == target:
                    return [i, j]