from typing import List


def removeElement(nums: List[int], val: int) -> int:
    nums[:] = [x for x in nums if x != val]
    return len(nums)

nums = [0,1,2,2,3,0,4,2]
print(removeElement(nums, 2))
