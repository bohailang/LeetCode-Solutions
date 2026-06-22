class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
        return i+1

        # empty_list = []
        # for i in range(len(nums)):
        #     if nums[i] not in empty_list:
        #         empty_list.append(nums[i])
        #     else:
        #         nums[i]="_"
        
        # while "_" in nums:
        #     nums.remove("_")

        # return len(nums)

                