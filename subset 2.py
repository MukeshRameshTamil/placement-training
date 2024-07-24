class Solution(object):
    def subsetsWithDup(self, nums):
[List[int]]
      
        ret = []
        n = len(nums)
        nums.sort()
        def backtrack(index, combination):
            if combination not in ret:
                ret.append(combination)

            for i in range(index, n):
                subCombination = combination + [nums[i]]
                backtrack(i + 1, subCombination) 

        backtrack(0, [])
        return ret
