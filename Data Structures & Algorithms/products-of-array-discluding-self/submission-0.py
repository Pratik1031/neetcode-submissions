class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))  # result list for storing prefix and postfix with default value 1 till length of nums

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1 ,-1,-1) :
            res[i] *= postfix
            postfix *= nums[i]

        print(res)  
        return res     