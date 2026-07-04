class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        value_set = set(nums)
        ans = 0
        for num in nums:
            if num - 1 in value_set:
                continue
            cur_ans = 1
            cur_num = num + 1
            while cur_num in value_set:
                cur_ans += 1
                cur_num += 1
            ans = max(ans, cur_ans)
        return ans