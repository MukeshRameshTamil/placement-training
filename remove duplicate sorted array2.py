class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        
        while j < len(nums):
            count = 1
            
            while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                count += 1
                j += 1
            
            for x in range(min(count, 2)):
                nums[i] = nums[j]
                i += 1
            
            j += 1
        
        return i
