from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    numbers = {}
    i = 0
    for number in nums:
        if (target - number) in numbers:
            return [numbers[target - number], i]
        else:
            numbers[number] = i
        i = i + 1

nums = [2,7,11,15]
print(twoSum(nums,9))