"""
Remove Element
leetcode question: https://leetcode.com/problems/remove-element/description/
"""
def removeElement(nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [0,1,2,2,4,5,2]

print(removeElement(nums, 2))
print(nums)