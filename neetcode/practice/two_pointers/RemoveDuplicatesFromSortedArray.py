"""
Remove Duplicates from Sorted Array
leetcode question link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""
def removeDuplicates(nums: list[int]) -> int:
    distinct = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            nums[distinct] = nums[i]
            distinct += 1
    return distinct

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4]

print(removeDuplicates(nums))
print(nums)