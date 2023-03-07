#------------ enumerate version O(n)
    
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if target == n:
                return i
            elif target < n:
                return i
        return len(nums)
#------------------ binary search version  O(log n),      reduces search interval by half at each iteration

