class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
        
        while "_" in nums:
            nums.remove("_")

        return len(nums)
        