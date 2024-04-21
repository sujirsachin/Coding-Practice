from collections import OrderedDict
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    seen = []
    i = 0
    while i < len(nums):
        if nums[i] not in seen:
            seen.append(nums[i])
        i += 1
    nums.clear()
    nums.extend(seen)
    return len(nums)

# Solution 2
def remove_duplicates2(nums: List[int]) -> int:
    freq = OrderedDict()
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    nums.clear()
    nums.extend(list(freq.keys()))
    print(nums)
    return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates2(nums))
