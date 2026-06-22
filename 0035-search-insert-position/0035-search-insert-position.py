class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        # return len(nums)         # another solution
            elif i == len(nums)-1: # elif i == index 3 (last index position)
                return i+1