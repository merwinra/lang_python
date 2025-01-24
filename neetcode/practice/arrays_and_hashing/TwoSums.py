"""
Two Sums
leetcode question link: https://leetcode.com/problems/valid-anagram/description/
"""
class TwoSums:
    def twoSums(this, nums: list[int], target: int) -> list[int]:
        indexMap = {}
        
        for i in range(len(nums)):
            indexMap[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexMap and indexMap[diff] != i:
                return [i, indexMap[diff]]
    
    def twoSumsV2(this, nums: list[int], target: int) -> list[int]:
        diffIndexMap = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in diffIndexMap:
                return [diffIndexMap[diff], i]
            
            diffIndexMap[num] = i
