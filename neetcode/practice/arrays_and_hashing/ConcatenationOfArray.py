"""
Concatenation of Array
leetcode question link: https://leetcode.com/problems/concatenation-of-array/description/
"""
# iteration using one pass
def concatenateArrays(nums: list[int]) -> list[int]:
    length = len(nums)
    ans = [0] * (2 * length)
    for i in range(length):
        ans[i] = ans[i + length] = nums[i]
    return ans

# iteration using two (x in the future) passes
def concatenateArrayV2(nums: list[int]) -> list[int]:
    length = len(nums)
    ans = []
    for i in range(2):
        for num in nums:
            ans.append(num)
    return ans

nums = [1, 2, 3, 2, 1]
print(concatenateArrays(nums))
print(concatenateArrayV2(nums))