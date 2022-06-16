class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # coded implementation direct # return num + num also works
        n = len(nums)
        ans = [0 for _ in range(2*n)]
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
            
        return ans