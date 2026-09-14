class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) == 0):
            return False
        mode_cnt = {}
        for x in nums:
            mode_cnt[x] = 0
        for x in nums:
            mode_cnt[x] = mode_cnt[x] + 1;
        k = sorted(mode_cnt.values(), reverse = True)
        if(k[0] >= 2):
            return True
        else:
            return False
