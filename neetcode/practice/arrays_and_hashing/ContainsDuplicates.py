"""
Contains Duplicates
leetcode question link: https://leetcode.com/problems/contains-duplicate/description/
"""
class ContainsDuplcates:
    def doesContainDuplicates(nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
    
    def doesContainDuplicatesV2(nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False